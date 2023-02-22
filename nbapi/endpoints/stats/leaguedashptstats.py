from nbapi.endpoints.endpoints import StatsEndpoint


class LeagueDashPtStats(StatsEndpoint):
    """Endpoint for `leaguedashptstats`."""

    _endpoint = "leaguedashptstats"
    _params = {
        "College": None,
        "Conference": None,
        "Country": None,
        "DateFrom": None,
        "DateTo": None,
        "Division": None,
        "DraftPick": None,
        "DraftYear": None,
        "GameScope": None,
        "Height": None,
        "LastNGames": 0,
        "LeagueID": "00",
        "Location": None,
        "Month": 0,
        "OpponentTeamID": 0,
        "Outcome": None,
        "PORound": 0,
        "PerMode": "PerGame",
        "PlayerExperience": None,
        "PlayerOrTeam": "Player",  # TODO: Player or Team here
        "PlayerPosition": None,
        "PtMeasureType": "Drives",
        "Season": "2020-21",
        "SeasonSegment": None,
        "SeasonType": "Regular Season",
        "StarterBench": None,
        "TeamID": 0,
        "VsConference": None,
        "VsDivision": None,
        "Weight": None,
    }
