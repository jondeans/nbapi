"""Classes and helper functions for NBA Stats Endpoints."""

import requests

BASE_URL = "http://stats.nba.com/stats/"
HEADERS = {
    "Accept": "application/json, text/plain, */*",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-US,en;q=0.5",
    "Connection": "keep-alive",
    "Host": "stats.nba.com",
    "Referer": "https://stats.nba.com",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.16; rv:84.0) Gecko/20100101 Firefox/84.0",
    "x-nba-stats-origin": "stats",
    "x-nba-stats-token": "true",
}


class Endpoint:
    """Base class for Endpoints."""

    endpoint = None
    params = None
    headers = HEADERS

    response = None

    def __init__(self, get_request=False):
        if get_request:
            self.response = self.get_request()

    def load_response(self, idx=0):
        # TODO: Load data tables specific to this endpoint, into this object, here.

        # TODO: if HAS_PANDAS can return a DataFrame?
        #   or should we just return a DataFrame friendly structure?

        endpoint_json = self.response.json()

        try:
            columns = endpoint_json["resultSets"][idx]["headers"]
            data = endpoint_json["resultSets"][idx]["rowSet"]
        except KeyError:
            try:
                columns = endpoint_json["resultSet"][idx]["headers"]
                data = endpoint_json["resultSet"][idx]["rowSet"]
            except KeyError:
                columns = endpoint_json["resultSets"]["headers"]
                data = endpoint_json["resultSets"]["rowSet"]

        return [dict(zip(columns, d)) for d in data]
        pass

    def get_url(self):
        return self.response.url()

    def get_response(self):
        return self.response

    def get_json(self):
        return self.response.json()

    def get_params(self):
        return self.params

    def update_params(self, params):
        """Update the parameters dictionary.

        Args:
            params: Dictionary of parameter values to set / update for this endpoints.
        """
        self.params.update(params)

    def get_request(self):
        return requests.get(
            BASE_URL + self.endpoint, params=self.params, headers=HEADERS
        )
