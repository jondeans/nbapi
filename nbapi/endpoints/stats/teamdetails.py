from nbapi.endpoints.stats._base import Endpoint


class TeamDetails(Endpoint):
    _endpoint = "teamdetails"
    _params = {
        "TeamID": 0,
    }
