from nbapi.endpoints._base import Endpoint


class LeaguePlayerOnDetails(Endpoint):
    endpoint = "leagueplayerondetails"
    params = {
        "DateFrom": "",
        "DateTo": "",
        "GameSegment": "",
        "LastNGames": 0,
        "LeagueID": "00",
        "Location": "",
        "MeasureType": "Opponent",
        "Month": 0,
        "OpponentTeamID": 0,
        "Outcome": "",
        "PaceAdjust": "N",
        "PerMode": "Per100Possessions",
        "Period": 0,
        "PlusMinus": "N",
        "Rank": "N",
        "Season": "2020-21",
        "SeasonSegment": "",
        "SeasonType": "Regular Season",
        "TeamID": 0,
        "VsConference": "",
        "VsDivision": "",
    }
