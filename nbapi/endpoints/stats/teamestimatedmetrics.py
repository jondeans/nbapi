from nbapi.endpoints.endpoints import StatsEndpoint


class TeamEstimatedMetrics(StatsEndpoint):
    """Endpoint for `teamestimatedmetrics`."""

    _endpoint = "teamestimatedmetrics"
    _params = {
        "LeagueID": "00",
        "Season": "2020-21",
        "SeasonType": "Regular Season",
    }
