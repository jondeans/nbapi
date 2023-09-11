from src.nbapi.endpoints.endpoints import DataEndpoint
from src.nbapi.nbapi import CURRENT_SEASON


class Scoreboard(DataEndpoint):
    """Endpoint for `scoreboard`."""

    _endpoint = "scoreboard"
    _params = {
        "Active": None,
        "AllStar": None,
        "College": None,
        "Country": None,
        "DraftPick": None,
        "DraftYear": None,
        "Height": None,
        "Historical": 1,
        "LeagueID": "00",
        "PlayerPosition": None,
        # TODO: Update the season?
        "Season": CURRENT_SEASON,
        "TeamID": 0,
        "Weight": None,
    }
