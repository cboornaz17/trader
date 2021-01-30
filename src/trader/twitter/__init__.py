import requests


class Twitter:
    search_endpoint = "https://api.twitter.com/2/tweets/search/recent"

    def __init__(self, bearer):
        self.bearer_token = bearer

    @property
    def headers(self):
        return {'Authorization': "Bearer {}".format(self.bearer_token)}

    def search_tweets(self, query: str, max_results: int = 100, start_time: str = None, end_time: str = None):
        """
        search for recent tweets

        :param start_time: YYYY-MM-DDTHH:mm:ssZ
        :param end_time: YYYY-MM-DDTHH:mm:ssZ
        """
        params = {
            'query': query,
            'max_results': max_results,
            'tweet.fields': 'entities'
        }

        if start_time is not None:
            params['start_time'] = start_time
        if end_time is not None:
            params['end_time'] = end_time

        return requests.get(self.search_endpoint, params=params, headers=self.headers)
