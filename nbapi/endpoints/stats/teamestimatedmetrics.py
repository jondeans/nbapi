from nbapi.endpoints.endpoints import StatsEndpoint

import nbapi.core.logger as log

logger = log.get_logger(__name__)


class TeamEstimatedMetrics(StatsEndpoint):
    _endpoint = "teamestimatedmetrics"
    _params = {
        "LeagueID": "00",
        "Season": "2020-21",
        "SeasonType": "Regular Season",
    }
