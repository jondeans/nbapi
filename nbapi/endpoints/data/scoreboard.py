from nbapi.endpoints.endpoints import DataEndpoint


class Scoreboard(DataEndpoint):
    """Endpoint for `scoreboard`."""

    _endpoint = "scoreboard"
    _params = {
        "Active": None,
        "AllStar": None,
        "College": None,
        "Country": None,
        "DraftPick": None,
        "DraftYear": None,
        "Height": None,
        "Historical": 1,
        "LeagueID": "00",
        "PlayerPosition": None,
        # TODO: Update the season?
        "Season": "2020-21",
        "TeamID": 0,
        "Weight": None,
    }
