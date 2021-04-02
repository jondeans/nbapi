from nbapi.endpoints._base import Endpoint


class CommonTeamRoster(Endpoint):
    _endpoint = "commonteamroster"
    _params = {
        "TeamID": 0,
        "LeagueID": "00",
        "Season": "2020-21",
    }
