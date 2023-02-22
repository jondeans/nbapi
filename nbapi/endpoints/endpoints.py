"""Classes and helper functions for NBA Endpoints."""

from typing import Union

import requests
from datatable import dt

import nbapi.core.logger as log

logger = log.get_logger(__name__)


class Endpoint:
    """Base class for Endpoints."""

    def __init__(self, get_request: bool = False):
        self._base_url = None
        self._headers = {
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
            "x-nba-stats-token": "true"
        }
        self._timeout = 30

        self._endpoint = None
        self._response = None
        self._params = None

        if get_request:
            self.get_request()
        logger.debug(f"RESPONSE: {self._response}")

    def _check_endpoint_response(self, json: dict) -> bool:
        """Check that the response and parameters match what we submitted."""
        matches = True
        matches *= json["resource"] == self._endpoint
        matches *= json["parameters"] == self._params
        return matches

    def load_response(self, index: int = 0) -> Union[dt.Frame, None]:
        """Load the json response and return the table at `resultSet[index]`."""

        if not self._response:
            logger.warning(f"No response found for {self._endpoint!r}. Did you get your request yet?")
            return self._response

        endpoint_json = self._response.json()

        if self._check_endpoint_response(endpoint_json):
            logger.warning("Resource or parameters data does not match submission.")

        try:
            columns = endpoint_json["resultSets"][index]["headers"]
            data = endpoint_json["resultSets"][index]["rowSet"]
        except KeyError:
            try:
                columns = endpoint_json["resultSet"][index]["headers"]
                data = endpoint_json["resultSet"][index]["rowSet"]
            except KeyError:
                columns = endpoint_json["resultSets"]["headers"]
                data = endpoint_json["resultSets"]["rowSet"]
        return dt.Frame([dict(zip(columns, d)) for d in data])

    @property
    def endpoint(self) -> str:
        """Get the endpoint."""
        return self._endpoint

    @property
    def params(self) -> dict:
        """Get the parameters."""
        return self._params

    @property
    def url(self) -> str:
        """Get the url."""
        return self._response.url

    @property
    def response(self) -> dict:
        """Get the response json dictionary."""
        return self._response

    def update_params(self, params: dict) -> None:
        """Update the parameters dictionary.

        Args:
            params: Dictionary of parameter values to set or update.
        """
        self._params.update(params)

    def get_request(self):
        """Submit the GET request for the current endpoint."""
        # TODO: Can add a debug and cache option here.
        self._response = requests.get(
            self._base_url + self._endpoint,
            params=self._params,
            headers=self._headers,
            timeout=self._timeout,
        )


class DataEndpoint(Endpoint):
    """Base class for Data Endpoints."""

    _base_url = "http://data.nba.com/data/"


class StatsEndpoint(Endpoint):
    """Base class for Stats Endpoints."""

    _base_url = "http://stats.nba.com/stats/"
