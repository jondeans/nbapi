from nbapi.endpoints.endpoints import StatsEndpoint
from nbapi.nbapi import CURRENT_SEASON


class LeagueDashPlayerClutch(StatsEndpoint):
    """Endpoint for `leaguedashplayerclutch`."""

    _endpoint = "leaguedashplayerclutch"
    _params = {
        "AheadBehind": "Ahead or Behind",
        "ClutchTime": "Last 5 Minutes",
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
        "Weight": None,
    }
