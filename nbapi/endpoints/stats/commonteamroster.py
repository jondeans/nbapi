from nbapi.endpoints.endpoints import StatsEndpoint

import nbapi.core.logger as log

logger = log.get_logger(__name__)


class CommonTeamRoster(StatsEndpoint):
    _endpoint = "commonteamroster"
    _params = {
        "TeamID": 0,
        "LeagueID": "00",
        "Season": "2020-21",
    }
