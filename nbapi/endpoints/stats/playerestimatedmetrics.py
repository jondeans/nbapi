from nbapi.endpoints.endpoints import StatsEndpoint


class PlayerEstimatedMetrics(StatsEndpoint):
    """Endpoint for `playerestimatedmetrics`."""

    _endpoint = "playerestimatedmetrics"
    _params = {
        "LeagueID": "00",
        "Season": "2020-21",
        "SeasonType": "Regular Season",
    }
