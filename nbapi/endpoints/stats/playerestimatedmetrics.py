from nbapi.endpoints.endpoints import StatsEndpoint
from nbapi.nbapi import CURRENT_SEASON


class PlayerEstimatedMetrics(StatsEndpoint):
    """Endpoint for `playerestimatedmetrics`."""

    _endpoint = "playerestimatedmetrics"
    _params = {
        "LeagueID": "00",
        "Season": CURRENT_SEASON,
        "SeasonType": "Regular Season",
    }
