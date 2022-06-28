from nbapi.endpoints.endpoints import StatsEndpoint

import nbapi.core.logger as log

logger = log.get_logger(__name__)


class LeagueDashOppPtShot(StatsEndpoint):
    _endpoint = "leaguedashoppptshot"
    _params = {
        "CloseDefDistRange": None,
        "Conference": None,
        "DateFrom": None,
        "DateTo": None,
        "Division": None,
        "DribbleRange": None,
        "GameSegment": None,
        "GeneralRange": "Overall",
        "LastNGames": 0,
        "LeagueID": "00",
        "Location": None,
        "Month": 0,
        "OpponentTeamID": 0,
        "Outcome": None,
        "PORound": 0,
        "PerMode": "PerGame",
        "Period": 0,
        "Season": "2020-21",
        "SeasonSegment": None,
        "SeasonType": "Regular Season",
        "ShotClockRange": None,
        "ShotDistRange": None,
        "TeamID": 0,
        "TouchTimeRange": None,
        "VsConference": None,
        "VsDivision": None,
    }
