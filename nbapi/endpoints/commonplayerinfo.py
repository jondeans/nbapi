from nbapi.endpoints._base import Endpoint


class CommonPlayerInfo(Endpoint):
    _endpoint = "commonplayerinfo"
    _params = {
        "PlayerID": None,
    }
