from nbapi.endpoints._base import Endpoint


class TeamEstimatedMetrics(Endpoint):
    endpoint = "teamestimatedmetrics"
    params = {
        "LeagueID": "00",
        "Season": "2020-21",
        "SeasonType": "Regular Season",
    }
