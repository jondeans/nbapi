from nbapi.endpoints.endpoints import StatsEndpoint

import nbapi.core.logger as log

logger = log.get_logger(__name__)


class PlayerIndex(StatsEndpoint):
    _endpoint = "playerindex"
    _params = {
        "Active": None,
        "AllStar": None,
        "College": None,
        "Country": None,
        "DraftPick": None,
        "DraftYear": None,
        "Height": None,
        "Historical": 1,
        "LeagueID": "00",
        "PlayerPosition": None,
        # TODO: Update the season?
        "Season": "2020-21",
        "TeamID": 0,
        "Weight": None,
    }
