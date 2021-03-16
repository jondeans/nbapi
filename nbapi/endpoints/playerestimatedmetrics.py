from nbapi.endpoints._base import Endpoint


class PlayerEstimatedMetrics(Endpoint):
    _endpoint = "playerestimatedmetrics"
    _params = {
        "LeagueID": "00",
        "Season": "2020-21",
        "SeasonType": "Regular Season",
    }
