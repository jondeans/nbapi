"""Classes and helper functions for NBA Endpoints."""

from typing import Union

import requests
import pandas as pd

from src import nbapi as log

logger = log.get_logger(__name__)


class Endpoint:
    """Base class for Endpoints."""

    _endpoint: str = None
    _response: str = None
    _params: dict = dict()
    _timeout: int = 30
    _base_url: str = None
    _headers: dict = {
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

    def __init__(self, get_request: bool = False):
        if get_request:
            self.get_request()
        logger.debug(f"RESPONSE: {self.response}")

    def _check_endpoint_response(self, json: dict) -> bool:
        """Check that the response and parameters match what we submitted."""
        matches = True
        matches *= json["resource"] == self._endpoint
        matches *= json["parameters"] == self._params
        return bool(matches)

    def load_response(self, index: int = 0) -> Union[pd.DataFrame, None]:
        """Load the json response and return the table at `resultSet[index]`."""

        if not self._response:
            logger.warning(
                f"No response found for {self._endpoint!r}. Did you get your request yet?"
            )
            return self._response

        endpoint_json = self._response.json()

        if not self._check_endpoint_response(endpoint_json):
            logger.warning("Endpoint or Parameters do not match submission.")

        results = endpoint_json.get("resultSets", endpoint_json.get("resultSet"))
        if isinstance(results, list) and index is not None:
            results = results[index]
        col_names = results["headers"]
        data = results["rowSet"]
        return pd.DataFrame([dict(zip(col_names, d)) for d in data])

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
        #   currently just using requests-cache to reduce frequency of calls.
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
