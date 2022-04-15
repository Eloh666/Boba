class DataParser:
    def parse(self, response):
        data = response.json.get('data', [])
        tweets = [self._parse_tweet(entry) for entry in data]
        return tweets, response.get('meta', 'next_token')

    def _parse_tweet(self, tweet):
        return {
            # add other fields here
            'author_id': tweet.get('author_id'),
            'created_at': tweet.get('created_at'),
            'id': tweet.get('id'),
            'text': tweet.get('text'),
        }
