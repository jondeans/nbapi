from nbapi.endpoints.endpoints import StatsEndpoint

import nbapi.core.logger as log

logger = log.get_logger(__name__)


class TeamDetails(StatsEndpoint):
    _endpoint = "teamdetails"
    _params = {
        "TeamID": 0,
    }
