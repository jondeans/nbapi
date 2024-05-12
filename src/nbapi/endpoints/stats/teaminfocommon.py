from src.nbapi.endpoints.endpoints import StatsEndpoint
from src.nbapi.nbapi import CURRENT_SEASON


class TeamInfoCommon(StatsEndpoint):
    """Endpoint for `teaminfocommon`."""

    _endpoint = "teaminfocommon"
    _params = {
        "TeamID": 0,
        "Season": CURRENT_SEASON,
        "LeagueID": "00",
        "SeasonType": "Regular Season",
    }
