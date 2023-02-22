from nbapi.endpoints.endpoints import StatsEndpoint


class TeamDetails(StatsEndpoint):
    """Endpoint for `teamdetails`."""

    _endpoint = "teamdetails"
    _params = {
        "TeamID": 0,
    }
