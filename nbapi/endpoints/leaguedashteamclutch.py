from nbapi.endpoints._base import Endpoint


class LeagueDashTeamClutch(Endpoint):
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
        "Season": "2020-21",
        "SeasonSegment": None,
        "SeasonType": "Regular Season",
        "ShotClockRange": None,
        "StarterBench": None,
        "TeamID": 0,
        "VsConference": None,
        "VsDivision": None,
    }
