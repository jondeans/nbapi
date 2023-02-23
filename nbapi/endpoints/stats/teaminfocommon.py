from nbapi.endpoints.endpoints import StatsEndpoint


class TeamInfoCommon(StatsEndpoint):
    """Endpoint for `teaminfocommon`."""

    _endpoint = "teaminfocommon"
    _params = {
        "TeamID": 0,
        "Season": "2020-21",
        "LeagueID": "00",
        "SeasonType": "Regular Season",
    }
