"""Classes around Players and Lists of Players."""

from datatable import f

import nbapi.core.logger as log
from nbapi.core.result import Result
from nbapi.endpoints.playerindex import PlayerIndex

logger = log.get_logger(__name__)


class PlayerList(Result):
    """Represents a list of player from NBA Stats."""

    def __init__(self):
        player_index = PlayerIndex()
        logger.info(f"ENDPOINT: {player_index.get_endpoint()}")
        logger.info(f"PARAMS: {player_index.get_params()}")

        player_index.get_request()
        player_index.load_response()

        self._frame = player_index.get_table()

    def find_player(self, query=None, by=None):
        if by == "id":
            return self._frame[f.PERSON_ID == query, :]
        if by == "first":
            return self._frame[f.PLAYER_FIRST_NAME == query, :]
        if by == "last":
            return self._frame[f.PLAYER_LAST_NAME == query, :]
