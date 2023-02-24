from nbapi.endpoints.endpoints import StatsEndpoint
from nbapi.nbapi import CURRENT_SEASON


class LeagueGameLog(StatsEndpoint):
    """Endpoint for `leaguegamelog`."""

    _endpoint = "7"
    _params = {
        "Counter": 1000,
        "DateFrom": None,
        "DateTo": None,
        "Direction": "DESC",
        "LeagueID": "00",
        "PlayerOrTeam": "P",  # TODO: "P" or "T" here
        "Season": CURRENT_SEASON,
        "SeasonType": "Regular Season",
        "Sorter": "DATE",
    }
