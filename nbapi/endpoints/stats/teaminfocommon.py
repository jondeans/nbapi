from nbapi.endpoints.stats._base import Endpoint


class TeamInfoCommon(Endpoint):
    _endpoint = "teaminfocommon"
    _params = {
        "TeamID": 0,
        "Season": "2020-21",
        "LeagueID": "00",
        "SeasonType": "Regular Season",
    }
