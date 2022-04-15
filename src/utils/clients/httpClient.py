import asyncio
import logging

import aiohttp


class HTTPClientException(Exception):
    pass


logger = logging.getLogger(__name__)
MAX_REQUESTS = 1


class HttpClient:
    # limits max concurrent requests
    def __init__(self):
        self.semaphore = asyncio.Semaphore(MAX_REQUESTS)

    async def request(self, endpoint, method="GET", params={}, json="", headers={},
                      auth=None, verify=False):
        """
        Aiohttp fetch request wrapper
        """
        logging.info("{} request towards: {}".format(method, endpoint))
        async with aiohttp.ClientSession(
                connector=aiohttp.TCPConnector(verify_ssl=verify),
        ) as session:
            async with self.semaphore, session.request(
                    method=method,
                    url=endpoint,
                    params=params,
                    json=json,
                    auth=auth,
                    headers=headers,
            ) as resp:
                logging.info("Server responded with: {}".format(resp.status))
                response, status_code = await resp.json(), resp.status

                if status_code != 200:
                    logger.error("RH Call failed: {}: {}".format(status_code, response))

                    # Raise the appropriate exception
                    raise HTTPClientException()
                return response
