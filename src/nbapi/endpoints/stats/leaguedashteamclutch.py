from src.nbapi.endpoints.endpoints import StatsEndpoint
from src.nbapi.nbapi import CURRENT_SEASON


class LeagueDashTeamClutch(StatsEndpoint):
    """Endpoint for `leaguedashteamclutch`."""

    _endpoint = "leaguedashteamclutch"
    _params = {
        "AheadBehind": "Ahead or Behind",
        "ClutchTime": "Last 5 Minutes",
        "Conference": None,
        "DateFrom": None,
        "DateTo": None,
        "Division": None,
        "GameScope": None,
        "GameSegment": None,
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
        "PointDiff": 5,
        "Rank": "N",
        "Season": CURRENT_SEASON,
        "SeasonSegment": None,
        "SeasonType": "Regular Season",
        "ShotClockRange": None,
        "StarterBench": None,
        "TeamID": 0,
        "VsConference": None,
        "VsDivision": None,
    }
