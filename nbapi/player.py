"""Classes around Players and Lists of Players."""

from pathlib import Path

import datatable as dt
from datatable import f

import nbapi.core.logger as log
from nbapi.core.types import FilePath
from nbapi.endpoints.stats.playerindex import PlayerIndex

logger = log.get_logger(__name__)


class PlayerList:
    """Represents a list of player from NBA Stats."""

    def __init__(self):
        endpoint = PlayerIndex()

        logger.debug(f"ENDPOINT: {endpoint.get_endpoint()}")
        logger.debug(f"PARAMS: {endpoint.get_params()}")

        endpoint.get_request()
        self._data = endpoint.load_response()

    def find_player(self, query: str = None, by: str = None) -> dt.Frame:
        """Retrieve information for a single player."""
        if by == "id":
            return self._data[f.PERSON_ID == query, :]
        if by == "first":
            return self._data[f.PLAYER_FIRST_NAME == query, :]
        if by == "last":
            return self._data[f.PLAYER_LAST_NAME == query, :]

    def to_csv(self, directory: FilePath) -> None:
        """Save the full player table to disk."""
        directory = Path(directory)
        self._data.to_csv(str(directory / "playerindex.csv"))
        logger.info(f"Saved {self._data.nrows:,} records to {directory / 'playerindex.csv'}.")

    @property
    def data(self):
        """Get the player data table."""
        return self._data
