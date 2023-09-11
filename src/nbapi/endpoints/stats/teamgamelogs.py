from src.nbapi.endpoints.endpoints import StatsEndpoint
from src.nbapi.nbapi import CURRENT_SEASON


class TeamGameLogs(StatsEndpoint):
    """Endpoint for `teamgamelogs`."""

    _endpoint = "teamgamelogs"
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
        "SeasonYear": CURRENT_SEASON,
        "ShotClockRange": None,
        "TeamID": None,
        "VsConference": None,
        "VsDivision": None,
    }
