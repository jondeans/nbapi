from nbapi.endpoints.endpoints import StatsEndpoint

import nbapi.core.logger as log

logger = log.get_logger(__name__)


class LeagueDashPtShot(StatsEndpoint):
    _endpoint = "leaguedashptshot"
    _params = {
        "CloseDefDistRange": None,
        "College": None,
        "Conference": None,
        "Country": None,
        "DateFrom": None,
        "DateTo": None,
        "Division": None,
        "DraftPick": None,
        "DraftYear": None,
        "DribbleRange": None,
        "GameSegment": None,
        "GeneralRange": "Overall",
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
        "PlayerPosition": None,
        "Season": "2020-21",
        "SeasonSegment": None,
        "SeasonType": "Regular Season",
        "ShotClockRange": None,
        "ShotDistRange": None,
        "StarterBench": None,
        "TeamID": 0,
        "TouchTimeRange": None,
        "VsConference": None,
        "VsDivision": None,
        "Weight": None,
    }
