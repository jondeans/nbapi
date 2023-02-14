from nbapi.endpoints.endpoints import StatsEndpoint

import nbapi.core.logger as log

logger = log.get_logger(__name__)


class SynergyPlayTypes(StatsEndpoint):
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
