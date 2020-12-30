from nbapi.endpoints._base import Endpoint


class LeagueDashOppPtShot(Endpoint):
    endpoint = "leaguedashoppptshot"
    params = {
        "CloseDefDistRange": "",
        "Conference": "",
        "DateFrom": "",
        "DateTo": "",
        "Division": "",
        "DribbleRange": "",
        "GameSegment": "",
        "GeneralRange": "Overall",
        "LastNGames": 0,
        "LeagueID": "00",
        "Location": "",
        "Month": 0,
        "OpponentTeamID": 0,
        "Outcome": "",
        "PORound": 0,
        "PerMode": "PerGame",
        "Period": 0,
        "Season": "2020-21",
        "SeasonSegment": "",
        "SeasonType": "Regular Season",
        "ShotClockRange": "",
        "ShotDistRange": "",
        "TeamID": 0,
        "TouchTimeRange": "",
        "VsConference": "",
        "VsDivision": "",
    }
