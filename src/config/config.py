AUTH_CONFIG = {
    'bearer_token': 'our-bearer-token-here'
}

GENERAL_CONFIG = {
    'write': True,
    'print': False,
    'output_path': 'outputs',
    'file_name': 'tweets',
    'extension': 'json',
    'max_tweets_per_file': 10000,
    'max_tweets_to_fetch': 1000,
}

API_CONFIG = {
    'query': 'query-entered-here',
    'start_time': '2018-01-01T00:00:00Z',
    'end_time': '2018-01-01T00:19:00Z',
    'max_results': 500,
    'search_endpoint': "https://api.twitter.com/2/tweets/search/all"
}
