from src.nbapi.endpoints.endpoints import StatsEndpoint
from src.nbapi.nbapi import CURRENT_SEASON


class LeagueDashPlayerStats(StatsEndpoint):
    """Endpoint for `leaguedashplayerstats`."""

    _endpoint = "leaguedashplayerstats"
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
        "MeasureType": "Base",
        "Month": 0,
        "OpponentTeamID": 0,
        "Outcome": None,
        "PORound": 0,
        "PaceAdjust": "N",
        "PerMode": "PerGame",
        "Period": 0,
        "PlayerExperience": None,
        "PlayerPosition": None,
        "PlusMinus": "N",
        "Rank": "N",
        "Season": CURRENT_SEASON,
        "SeasonSegment": None,
        "SeasonType": "Regular Season",
        "ShotClockRange": None,
        "StarterBench": None,
        "TeamID": 0,
        "TwoWay": 0,
        "VsConference": None,
        "VsDivision": None,
        "Weight": None,
    }
