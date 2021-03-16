"""Classes around Players and Lists of Players."""

from datatable import f

import nbapi.logger as log
from nbapi.endpoints.playerindex import PlayerIndex

logger = log.get_logger(__name__)


class PlayerList:
    """Represents a list of player from NBA Stats."""

    _player_frame = None

    @classmethod
    def from_playerindex(cls):
        player_index = PlayerIndex()
        logger.info(f"ENDPOINT: {player_index.get_endpoint()}")
        logger.info(f"PARAMS: {player_index.get_params()}")

        player_index.get_request()
        player_index.load_response()

        cls._player_frame = player_index.get_table()
        return cls()

    def find_player(self, query=None, by=None):
        if by == "id":
            return self._player_frame[f.PERSON_ID == query, :]
        if by == "first":
            return self._player_frame[f.PLAYER_FIRST_NAME == query, :]
        if by == "last":
            return self._player_frame[f.PLAYER_LAST_NAME == query, :]
