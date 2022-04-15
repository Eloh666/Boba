import asyncio

from config.config import GENERAL_CONFIG, AUTH_CONFIG, API_CONFIG
from utils.clients.httpClient import HttpClient, HTTPClientException
from utils.data.data_parser import DataParser
from utils.data.data_writer import DataWriterFactory


class SearchApiWrapper:
    def __init__(self, parser: DataParser, http_client: HttpClient, writer: DataWriterFactory):
        # self.writer = writer
        self.parser = parser
        self.http_client = http_client
        self.writer = writer

    async def fetch(self):
        tweets = []
        iterations = 0

        try:
            # Load first request
            print('Loading first batch')
            tweets, next_token = await self._fetch()
            fetched_tweets = len(tweets)

            while next_token or fetched_tweets < GENERAL_CONFIG['desired_amount']:
                # Sleep to avoid hitting limits TODO: verify 15m limit
                await asyncio.sleep(1)
                iterations += 1

                # Loads next batch
                print(f'Loading batch {iterations}')
                new_tweets, next_token = await self._fetch(next_token)
                tweets = [*tweets, *new_tweets]
                fetched_tweets += len(new_tweets)
                print(f'Batch complete - {GENERAL_CONFIG["max_tweets_to_fetch"]} tweets loaded')
                if not next_token:
                    print('Data load complete - no next page')

                if print(GENERAL_CONFIG['print']):
                    print(new_tweets)

                # Stores data when/if
                if GENERAL_CONFIG['write'] and len(tweets) >= GENERAL_CONFIG['max_tweets_per_file']:
                    self._write(tweets)
                    tweets = []
            else:
                self._write(tweets)

        except Exception as e:
            print(e)
        finally:
            self._write(tweets)

    async def _fetch(self, next_token=None):
        request_params = {
            **API_CONFIG,
            'pagination_token': next_token,
        } if next_token else API_CONFIG

        try:
            data = await self.http_client.request(
                endpoint=API_CONFIG['search_endpoint'],
                params=request_params,
                headers=AUTH_CONFIG,
            )
            return self.parser.parse(data)
        except HTTPClientException as e:
            print(f'Something went wrong with the request: {e}')

    def _write(self, data):
        self.writer.write_new(data)
