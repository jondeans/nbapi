from nbapi.endpoints.endpoints import StatsEndpoint

import nbapi.core.logger as log

logger = log.get_logger(__name__)


class PlayerGameLogs(StatsEndpoint):
    _endpoint = "playergamelogs"
    _params = {
        "DateFrom": None,
        "DateTo": None,
        "GameSegment": None,
        "LastNGames": 0,
        "LeagueID": "00",
        "Location": None,
        "MeasureType": "Base",
        "Month": 0,
        "OppTeamID": 0,
        "Outcome": None,
        "PORound": 0,
        "PerMode": "Totals",
        "Period": 0,
        "PlayerID": None,
        "SeasonSegment": None,
        "SeasonType": "Regular Season",
        "SeasonYear": "2020-21",
        "ShotClockRange": None,
        "TeamID": None,
        "VsConference": None,
        "VsDivision": None,
    }
