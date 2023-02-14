from nbapi.endpoints.endpoints import StatsEndpoint

import nbapi.core.logger as log

logger = log.get_logger(__name__)


class TeamInfoCommon(StatsEndpoint):
    _endpoint = "teaminfocommon"
    _params = {
        "TeamID": 0,
        "Season": "2020-21",
        "LeagueID": "00",
        "SeasonType": "Regular Season",
    }
