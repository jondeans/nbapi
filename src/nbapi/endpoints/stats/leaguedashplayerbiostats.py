from src.nbapi.endpoints.endpoints import StatsEndpoint
from src.nbapi.nbapi import CURRENT_SEASON


class LeagueDashPlayerBioStats(StatsEndpoint):
    """Endpoint for `leaguedashplayerbiostats`."""

    _endpoint = "leaguedashplayerbiostats"
    _params = {
        "College": None,
        "Conference": None,
        "Country": None,
        "DateFrom": None,
        "DateTo": None,
        "Division": None,
        "DraftPick": None,
        "DraftYear": None,
        "GameScope": None,
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
        "PlayerPosition": None,
        "Season": CURRENT_SEASON,
        "SeasonSegment": None,
        "SeasonType": "Regular Season",
        "ShotClockRange": None,
        "StarterBench": None,
        "TeamID": 0,
        "VsConference": None,
        "VsDivision": None,
        "Weight": None,
    }
