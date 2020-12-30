from nbapi.endpoints._base import Endpoint


class LeagueHustleStatsPlayer(Endpoint):
    endpoint = "leaguehustlestatsplayer"
    params = {
        "College": "",
        "Conference": "",
        "Country": "",
        "DateFrom": "",
        "DateTo": "",
        "Division": "",
        "DraftPick": "",
        "DraftYear": "",
        "Height": "",
        "LeagueID": "00",
        "Location": "",
        "Month": 0,
        "OpponentTeamID": 0,
        "Outcome": "",
        "PORound": 0,
        "PerMode": "PerGame",
        "PlayerExperience": "",
        "PlayerPosition": "",
        "Season": "2020-21",
        "SeasonSegment": "",
        "SeasonType": "Regular Season",
        "TeamID": 0,
        "VsConference": "",
        "VsDivision": "",
        "Weight": "",
    }
