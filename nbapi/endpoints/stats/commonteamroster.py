from nbapi.endpoints.endpoints import StatsEndpoint


class CommonTeamRoster(StatsEndpoint):
    """Endpoint for `commonteamroster`."""

    _endpoint = "commonteamroster"
    _params = {
        "TeamID": 0,
        "LeagueID": "00",
        "Season": "2020-21",
    }
