from nbapi.endpoints._base import Endpoint


class SynergyPlayTypes(Endpoint):
    endpoint = "synergyplaytypes"
    params = {
        "LeagueID": "00",
        "PerMode": "PerGame",
        "PlayType": "Isolation",
        "PlayerOrTeam": "P",  # TODO: P or T here
        "SeasonType": "Regular Season",
        "SeasonYear": "2020-21",
        "TypeGrouping": "offensive",
    }
