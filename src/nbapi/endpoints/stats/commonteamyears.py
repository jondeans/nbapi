from src.nbapi.endpoints.endpoints import StatsEndpoint


class CommonTeamYears(StatsEndpoint):
    """Endpoint for `commonteamyears`."""

    _endpoint = "commonteamyears"
    _params = {"LeagueID": "00"}
