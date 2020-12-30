from nbapi.endpoints._base import Endpoint


class LeagueGameLog(Endpoint):
    endpoint = "leaguegamelog"
    params = {
        "Counter": 1000,
        "DateFrom": "",
        "DateTo": "",
        "Direction": "DESC",
        "LeagueID": "00",
        "PlayerOrTeam": "P",  # TODO: "P" or "T" here
        "Season": "2020-21",
        "SeasonType": "Regular Season",
        "Sorter": "DATE",
    }
