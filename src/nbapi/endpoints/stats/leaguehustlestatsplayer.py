from src.nbapi.endpoints.endpoints import StatsEndpoint
from src.nbapi.nbapi import CURRENT_SEASON


class LeagueHustleStatsPlayer(StatsEndpoint):
    """Endpoint for `leaguehustlestatsplayer`."""

    _endpoint = "leaguehustlestatsplayer"
    _params = {
        "College": None,
        "Conference": None,
        "Country": None,
        "DateFrom": None,
        "DateTo": None,
        "Division": None,
        "DraftPick": None,
        "DraftYear": None,
        "Height": None,
        "LeagueID": "00",
        "Location": None,
        "Month": 0,
        "OpponentTeamID": 0,
        "Outcome": None,
        "PORound": 0,
        "PerMode": "PerGame",
        "PlayerExperience": None,
        "PlayerPosition": None,
        "Season": CURRENT_SEASON,
        "SeasonSegment": None,
        "SeasonType": "Regular Season",
        "TeamID": 0,
        "VsConference": None,
        "VsDivision": None,
        "Weight": None,
    }
