""""""
from datetime import datetime

import logger as log
import requests

logger = log.get_logger(__name__)

# TODO: setup cache with a time to expire?

TODAY = datetime.today()
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


def _get_json_endpoint(endpoint, params):
    """Retrieves the endpoint w/params as JSON.

    # TODO: can pass 'referer' to change our headers...

    Args:
        endpoint: Endpoint to be called from NBA Stats API.
        params: Parameters to be passed to API.

    Returns:
        json
    """

    r = requests.get(BASE_URL + endpoint, params=params, headers=HEADERS)
    logger.info(r.url)
    logger.info(r.raise_for_status())
    logger.info(r.json())

    return r.json()


def _parse_json_endpoint(endpoint_json, idx=0):
    """

    Args:
        endpoint_json: Endpoint JSON output from `_get_json_endpoint`.
        idx: Index where the data is located.

    Returns:
        dictionary
    """

    # TODO: if HAS_PANDAS can return a DataFrame?
    #   or should we just return a DataFrame friendly structure?

    try:
        columns = endpoint_json["resultSets"][0]["headers"]
        data = endpoint_json["resultSets"][0]["rowSet"]
    except KeyError:
        try:
            columns = endpoint_json["resultSet"][0]["headers"]
            data = endpoint_json["resultSet"][0]["rowSet"]
        except KeyError:
            columns = endpoint_json["resultSets"]["headers"]
            data = endpoint_json["resultSets"]["rowSet"]

    return [dict(zip(columns, d)) for d in data]
