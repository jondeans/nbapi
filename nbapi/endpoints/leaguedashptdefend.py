from nbapi.endpoints._base import Endpoint


class LeagueDashPtDefend(Endpoint):
    endpoint = "leaguedashptdefend"
    params = {
        "College": "",
        "Conference": "",
        "Country": "",
        "DateFrom": "",
        "DateTo": "",
        "DefenseCategory": "Overall",
        "Division": "",
        "DraftPick": "",
        "DraftYear": "",
        "GameSegment": "",
        "Height": "",
        "LastNGames": 0,
        "LeagueID": "00",
        "Location": "",
        "Month": 0,
        "OpponentTeamID": 0,
        "Outcome": "",
        "PORound": 0,
        "PerMode": "PerGame",
        "Period": 0,
        "PlayerExperience": "",
        "PlayerID": "",
        "PlayerPosition": "",
        "Season": "2020-21",
        "SeasonSegment": "",
        "SeasonType": "Regular Season",
        "StarterBench": "",
        "TeamID": 0,
        "VsConference": "",
        "VsDivision": "",
        "Weight": "",
    }
