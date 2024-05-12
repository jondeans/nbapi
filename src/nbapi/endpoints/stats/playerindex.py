from src.nbapi.endpoints.endpoints import StatsEndpoint
from src.nbapi.nbapi import CURRENT_SEASON


class PlayerIndex(StatsEndpoint):
    """Endpoint for `playerindex`."""

    _endpoint = "playerindex"
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
        "Season": CURRENT_SEASON,
        "TeamID": 0,
        "Weight": None,
    }
