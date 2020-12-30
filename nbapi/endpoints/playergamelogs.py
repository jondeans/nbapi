from nbapi.endpoints._base import Endpoint


class PlayerGameLogs(Endpoint):
    endpoint = "playergamelogs"
    params = {
        "DateFrom": "",
        "DateTo": "",
        "GameSegment": "",
        "LastNGames": 0,
        "LeagueID": "00",
        "Location": "",
        "MeasureType": "Base",
        "Month": 0,
        "OppTeamID": 0,
        "Outcome": "",
        "PORound": 0,
        "PerMode": "Totals",
        "Period": 0,
        "PlayerID": "",
        "SeasonSegment": "",
        "SeasonType": "Regular Season",
        "SeasonYear": "2020-21",
        "ShotClockRange": "",
        "TeamID": "",
        "VsConference": "",
        "VsDivision": "",
    }
