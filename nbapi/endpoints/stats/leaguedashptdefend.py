from nbapi.endpoints.endpoints import StatsEndpoint

import nbapi.core.logger as log

logger = log.get_logger(__name__)


class LeagueDashPtDefend(StatsEndpoint):
    _endpoint = "leaguedashptdefend"
    _params = {
        "College": None,
        "Conference": None,
        "Country": None,
        "DateFrom": None,
        "DateTo": None,
        "DefenseCategory": "Overall",
        "Division": None,
        "DraftPick": None,
        "DraftYear": None,
        "GameSegment": None,
        "Height": None,
        "LastNGames": 0,
        "LeagueID": "00",
        "Location": None,
        "Month": 0,
        "OpponentTeamID": 0,
        "Outcome": None,
        "PORound": 0,
        "PerMode": "PerGame",
        "Period": 0,
        "PlayerExperience": None,
        "PlayerID": None,
        "PlayerPosition": None,
        "Season": "2020-21",
        "SeasonSegment": None,
        "SeasonType": "Regular Season",
        "StarterBench": None,
        "TeamID": 0,
        "VsConference": None,
        "VsDivision": None,
        "Weight": None,
    }
