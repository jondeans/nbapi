from nbapi.endpoints._base import Endpoint


class CommonTeamYears(Endpoint):
    _endpoint = "commonteamyears"
    _params = {"LeagueID": "00"}
