from nbapi.endpoints.endpoints import StatsEndpoint

import nbapi.core.logger as log

logger = log.get_logger(__name__)


class CommonTeamYears(StatsEndpoint):
    _endpoint = "commonteamyears"
    _params = {"LeagueID": "00"}
