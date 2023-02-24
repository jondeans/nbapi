from nbapi.endpoints.endpoints import StatsEndpoint
from nbapi.nbapi import CURRENT_SEASON


class LeagueDashTeamStats(StatsEndpoint):
    """Endpoint for `leaguedashteamstats`."""

    _endpoint = "leaguedashteamstats"
    _params = {
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
    }
