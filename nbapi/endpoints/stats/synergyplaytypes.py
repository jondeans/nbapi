from nbapi.endpoints.endpoints import StatsEndpoint
from nbapi.nbapi import CURRENT_SEASON


class SynergyPlayTypes(StatsEndpoint):
    """Endpoint for `synergyplaytypes`."""

    _endpoint = "synergyplaytypes"
    _params = {
        "LeagueID": "00",
        "PerMode": "PerGame",
        "PlayType": "Isolation",
        "PlayerOrTeam": "P",  # TODO: P or T here
        "SeasonType": "Regular Season",
        "SeasonYear": CURRENT_SEASON,
        "TypeGrouping": "offensive",
    }
