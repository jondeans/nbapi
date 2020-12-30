from nbapi.endpoints._base import Endpoint


class LeagueDashTeamShotLocations(Endpoint):
    endpoint = "leaguedashteamshotlocations"
    params = {
        "Conference": "",
        "DateFrom": "",
        "DateTo": "",
        "DistanceRange": "5ft Range",
        "Division": "",
        "GameScope": "",
        "GameSegment": "",
        "LastNGames": 0,
        "LeagueID": "00",
        "Location": "",
        "MeasureType": "Base",
        "Month": 0,
        "OpponentTeamID": 0,
        "Outcome": "",
        "PORound": 0,
        "PaceAdjust": "N",
        "PerMode": "PerGame",
        "Period": 0,
        "PlayerExperience": "",
        "PlayerPosition": "",
        "PlusMinus": "N",
        "Rank": "N",
        "Season": "2020-21",
        "SeasonSegment": "",
        "SeasonType": "Regular Season",
        "ShotClockRange": "",
        "StarterBench": "",
        "TeamID": 0,
        "VsConference": "",
        "VsDivision": "",
    }
