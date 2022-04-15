import asyncio

from src.search_api_wrapper import SearchApiWrapper
from src.utils.clients.httpClient import HttpClient
from src.utils.data.data_parser import DataParser
from src.utils.data.data_writer import DataWriterFactory

from config.config import GENERAL_CONFIG

if __name__ == "__main__":
    api_wrapper = SearchApiWrapper(
        parser=DataParser(),
        http_client=HttpClient(),
        writer=DataWriterFactory(
            GENERAL_CONFIG['output_path'],
            GENERAL_CONFIG['file_name'],
            GENERAL_CONFIG['extension'],
        ),
    )

    asyncio.run(api_wrapper.fetch())
