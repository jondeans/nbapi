"""Classes and helper functions for NBA Endpoints."""

import requests
from datatable import dt

import nbapi.core.logger as log

logger = log.get_logger(__name__)


class Endpoint:
    """Base class for Endpoints."""

    def __init__(self, get_request=False):
        self.endpoint = None
        self.response = None
        self.params = None

        if get_request:
            self.get_request()
        logger.info(f"RESPONSE: {self._response}")

    def load_response(self, idx=0):
        if self._response is None:
            logger.warning(f"WARNING: No response found for {self._endpoint!r}. Did you get your request yet?")
            return self._response

        endpoint_json = self._response.json()

        if (
            endpoint_json["resource"] != self._endpoint
            or endpoint_json["parameters"] != self._params
        ):
            logger.warning("Resource or parameters data does not match submission.")

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
        return dt.Frame([dict(zip(columns, d)) for d in data])

    def get_endpoint(self):
        return self._endpoint

    def get_url(self):
        return self._response.url

    def get_response(self):
        return self._response

    def get_params(self):
        return self._params

    def update_params(self, params):
        """Update the parameters dictionary.

        Args:
            params: Dictionary of parameter values to set / update for this endpoints.
        """
        self._params.update(params)

    def get_request(self):
        # TODO: Can add a debug and cache option here.
        self._response = requests.get(
            BASE_URL + self._endpoint,
            params=self._params,
            headers=HEADERS,
            timeout=TIMEOUT,
        )


class DataEndpoint(Endpoint):
    """Base class for Endpoints."""

    _base_url = "http://data.nba.com/data/"
    _headers = {"Accept": "application/json, text/plain, */*",
        "Accept-Encoding": "gzip, deflate, br", "Accept-Language": "en-US,en;q=0.5",
        "Connection": "keep-alive", "Host": "stats.nba.com", "Referer": "https://stats.nba.com",
        "Sec-Fetch-Mode": "cors", "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.16; rv:84.0) Gecko/20100101 Firefox/84.0",
        "x-nba-stats-origin": "stats", "x-nba-stats-token": "true", }
    _timeout = 30


class StatsEndpoint(Endpoint):
    """Base class for Endpoints."""

    _base_url = "http://stats.nba.com/stats/"
    _headers = {"Accept": "application/json, text/plain, */*",
        "Accept-Encoding": "gzip, deflate, br", "Accept-Language": "en-US,en;q=0.5",
        "Connection": "keep-alive", "Host": "stats.nba.com", "Referer": "https://stats.nba.com",
        "Sec-Fetch-Mode": "cors", "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.16; rv:84.0) Gecko/20100101 Firefox/84.0",
        "x-nba-stats-origin": "stats", "x-nba-stats-token": "true", }
    _timeout = 30
