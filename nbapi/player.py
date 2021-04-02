"""Classes around Players and Lists of Players."""

from pathlib import Path

from datatable import f

import nbapi.core.logger as log
from nbapi.endpoints.playerindex import PlayerIndex

logger = log.get_logger(__name__)


class PlayerList:
    """Represents a list of player from NBA Stats."""

    def __init__(self):
        endpoint = PlayerIndex()

        logger.info(f"ENDPOINT: {endpoint.get_endpoint()}")
        logger.info(f"PARAMS: {endpoint.get_params()}")

        endpoint.get_request()
        self._index = endpoint.load_response(idx=0)

    def find_player(self, query=None, by=None):
        if by == "id":
            return self._index[f.PERSON_ID == query, :]
        if by == "first":
            return self._index[f.PLAYER_FIRST_NAME == query, :]
        if by == "last":
            return self._index[f.PLAYER_LAST_NAME == query, :]

    def to_csv(self, directory=None):
        directory = Path(directory)
        self._index.to_csv(str(directory / "playerindex.csv.gz"))

    def get_index(self):
        return self._index
