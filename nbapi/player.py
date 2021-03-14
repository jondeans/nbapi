"""Classes around Players and Lists of Players."""

from datatable import dt, f

import nbapi.logger as log
from nbapi.endpoints.playerindex import PlayerIndex

logger = log.get_logger(__name__)


class PlayerNotFoundException(Exception):
    """Exception raised when a player is not found in NBA Stats."""

    def __init__(self, player):
        self.player = player

    def __str__(self):
        return f"Player '{self.player}' not found."


class Player:
    """Represents a player from NBA Stats."""

    _json = None
    player_id = None
    last_name = None
    first_name = None
    player_slug = None
    position = None
    height = None
    weight = None
    # date_of_birth = None
    # shoots = None
    curr_team_id = None
    curr_team = None
    curr_team_city = None
    curr_team_slug = None
    curr_team_is_defunct = None
    curr_team_abbr = None
    curr_team_jersey_number = None
    draft_year = None
    draft_round = None
    draft_number = None
    roster_status = None
    career_from = None
    career_to = None

    def __init__(self, first=None, last=None):
        self.first_name = first
        self.last_name = last

        if last:
            self.player_slug = f"{first}-{last}".lower()
        else:
            self.player_slug = first.lower()

    @classmethod
    def from_dict(cls, player_index_json):
        cls._json = player_index_json
        cls.player_id = player_index_json.get("PERSON_ID")
        cls.last_name = player_index_json.get("PLAYER_LAST_NAME")
        cls.first_name = player_index_json.get("PLAYER_FIRST_NAME")
        cls.player_slug = player_index_json.get("PLAYER_SLUG")
        cls.position = player_index_json.get("POSITION")
        cls.height = player_index_json.get("HEIGHT")
        cls.weight = player_index_json.get("WEIGHT")
        # Team Data
        cls.curr_team_id = player_index_json.get("TEAM_ID")
        cls.curr_team = player_index_json.get("TEAM_NAME")
        cls.curr_team_city = player_index_json.get("TEAM_CITY")
        cls.curr_team_slug = player_index_json.get("TEAM_SLUG")
        cls.curr_team_is_defunct = player_index_json.get("IS_DEFUNCT")
        cls.curr_team_abbr = player_index_json.get("TEAM_ABBREVIATION")
        cls.curr_team_jersey_number = player_index_json.get("JERSEY_NUMBER")
        # Career Data
        cls.draft_year = player_index_json.get("DRAFT_YEAR")
        cls.draft_round = player_index_json.get("DRAFT_ROUND")
        cls.draft_number = player_index_json.get("DRAFT_NUMBER")
        cls.roster_status = player_index_json.get("ROSTER_STATUS")
        cls.career_from = player_index_json.get("FROM_YEAR")
        cls.career_to = player_index_json.get("TO_YEAR")
        return cls

    def __str__(self):
        return self.player_slug


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
