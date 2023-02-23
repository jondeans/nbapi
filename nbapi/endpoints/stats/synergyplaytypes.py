from nbapi.endpoints.endpoints import StatsEndpoint


class SynergyPlayTypes(StatsEndpoint):
    """Endpoint for `synergyplaytypes`."""

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
