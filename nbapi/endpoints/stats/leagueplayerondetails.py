from nbapi.endpoints.endpoints import StatsEndpoint


class LeaguePlayerOnDetails(StatsEndpoint):
    """Endpoint for `leagueplayerondetails`."""

    _endpoint = "leagueplayerondetails"
    _params = {
        "DateFrom": None,
        "DateTo": None,
        "GameSegment": None,
        "LastNGames": 0,
        "LeagueID": "00",
        "Location": None,
        "MeasureType": "Opponent",
        "Month": 0,
        "OpponentTeamID": 0,
        "Outcome": None,
        "PaceAdjust": "N",
        "PerMode": "Per100Possessions",
        "Period": 0,
        "PlusMinus": "N",
        "Rank": "N",
        "Season": "2020-21",
        "SeasonSegment": None,
        "SeasonType": "Regular Season",
        "TeamID": 0,
        "VsConference": None,
        "VsDivision": None,
    }
