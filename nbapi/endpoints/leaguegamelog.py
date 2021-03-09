from nbapi.endpoints._base import Endpoint


class LeagueGameLog(Endpoint):
    _endpoint = "leaguegamelog"
    _params = {
        "Counter": 1000,
        "DateFrom": None,
        "DateTo": None,
        "Direction": "DESC",
        "LeagueID": "00",
        "PlayerOrTeam": "P",  # TODO: "P" or "T" here
        "Season": "2020-21",
        "SeasonType": "Regular Season",
        "Sorter": "DATE",
    }
