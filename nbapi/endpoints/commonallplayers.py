from nbapi.endpoints._base import Endpoint


class CommonAllPlayers(Endpoint):
    _endpoint = "commonallplayers"
    _params = {
        "LeagueID": "00",
        "Season": "2020-21",
    }
