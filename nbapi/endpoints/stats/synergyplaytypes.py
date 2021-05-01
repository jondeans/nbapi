from nbapi.endpoints.stats._base import Endpoint


class SynergyPlayTypes(Endpoint):
    _endpoint = "synergyplaytypes"
    _params = {
        "LeagueID": "00",
        "PerMode": "PerGame",
        "PlayType": "Isolation",
        "PlayerOrTeam": "P",  # TODO: P or T here
        "SeasonType": "Regular Season",
        "SeasonYear": "2020-21",
        "TypeGrouping": "offensive",
    }
