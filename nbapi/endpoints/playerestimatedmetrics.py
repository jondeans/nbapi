from nbapi.endpoints._base import Endpoint


class PlayerEstimatedMetrics(Endpoint):
    endpoint = "playerestimatedmetrics"
    params = {
        "LeagueID": "00",
        "Season": "2020-21",
        "SeasonType": "Regular Season",
    }
