from nbapi.endpoints.endpoints import StatsEndpoint

import nbapi.core.logger as log

logger = log.get_logger(__name__)


class LeagueGameLog(StatsEndpoint):
    _endpoint = "7"
    _params = {
        "Counter": 1000,
        "DateFrom": None,
        "DateTo": None,
        "Direction": "DESC",
        "LeagueID": "00",
        "PlayerOrTeam": "P",  # TODO: "P" or "T" here
        "Season": "2020-21",
        "SeasonType": "Regular Season",
        "Sorter": "DATE",
    }
