from nbapi.endpoints.endpoints import StatsEndpoint


class LeagueDashTeamShotLocations(StatsEndpoint):
    """Endpoint for `leaguedashteamshotlocations`."""

    _endpoint = "leaguedashteamshotlocations"
    _params = {
        "Conference": None,
        "DateFrom": None,
        "DateTo": None,
        "DistanceRange": "5ft Range",
        "Division": None,
        "GameScope": None,
        "GameSegment": None,
        "LastNGames": 0,
        "LeagueID": "00",
        "Location": None,
        "MeasureType": "Base",
        "Month": 0,
        "OpponentTeamID": 0,
        "Outcome": None,
        "PORound": 0,
        "PaceAdjust": "N",
        "PerMode": "PerGame",
        "Period": 0,
        "PlayerExperience": None,
        "PlayerPosition": None,
        "PlusMinus": "N",
        "Rank": "N",
        "Season": "2020-21",
        "SeasonSegment": None,
        "SeasonType": "Regular Season",
        "ShotClockRange": None,
        "StarterBench": None,
        "TeamID": 0,
        "VsConference": None,
        "VsDivision": None,
    }
