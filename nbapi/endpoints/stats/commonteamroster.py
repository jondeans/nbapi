from nbapi.endpoints.endpoints import StatsEndpoint
from nbapi.nbapi import CURRENT_SEASON


class CommonTeamRoster(StatsEndpoint):
    """Endpoint for `commonteamroster`."""

    _endpoint = "commonteamroster"
    _params = {
        "TeamID": 0,
        "LeagueID": "00",
        "Season": CURRENT_SEASON,
    }
