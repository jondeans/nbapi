from nbapi.endpoints._base import Endpoint


class TeamEstimatedMetrics(Endpoint):
    _endpoint = "teamestimatedmetrics"
    _params = {
        "LeagueID": "00",
        "Season": "2020-21",
        "SeasonType": "Regular Season",
    }
