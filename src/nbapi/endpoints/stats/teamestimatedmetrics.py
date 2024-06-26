from src.nbapi.endpoints.endpoints import StatsEndpoint
from src.nbapi.nbapi import CURRENT_SEASON


class TeamEstimatedMetrics(StatsEndpoint):
    """Endpoint for `teamestimatedmetrics`."""

    _endpoint = "teamestimatedmetrics"
    _params = {
        "LeagueID": "00",
        "Season": CURRENT_SEASON,
        "SeasonType": "Regular Season",
    }
