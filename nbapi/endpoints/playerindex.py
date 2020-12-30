from nbapi.endpoints._base import Endpoint


class PlayerIndex(Endpoint):
    endpoint = "playerindex"
    params = {
        "Active": "",
        "AllStar": "",
        "College": "",
        "Country": "",
        "DraftPick": "",
        "DraftYear": "",
        "Height": "",
        "Historical": 1,
        "LeagueID": "00",
        "PlayerPosition": "",
        # TODO: Update the season?
        "Season": "2020-21",
        "TeamID": 0,
        "Weight": "",
    }
