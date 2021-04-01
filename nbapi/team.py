"""Classes around Teams and Lists of Teams."""

from datatable import f

import nbapi.core.logger as log
from nbapi.core.result import Result
from nbapi.endpoints.commonteamyears import CommonTeamYears
from nbapi.endpoints.teaminfocommon import TeamInfoCommon

logger = log.get_logger(__name__)


class TeamList(Result):
    """Represents a list of teams from NBA Stats."""

    def __init__(self):
        team_index = CommonTeamYears()
        logger.info(f"ENDPOINT: {team_index.get_endpoint()}")
        logger.info(f"PARAMS: {team_index.get_params()}")

        team_index.get_request()
        team_index.load_response()

        self._frame = team_index.get_table()

    def find_team(self, query=None, by=None):
        if by == "id":
            return self._frame[f.TEAM_ID == query, :]
        if by == "abbr":
            return self._frame[f.ABBREVIATION == query, :]


class TeamSummary(Result):
    """Represents basic info on a single team from NBA Stats."""

    def __init__(self, team_id=None, season=None):
        team_index = TeamInfoCommon()

        if team_id is not None:
            team_index.update_params({"TeamID": int(team_id)})
        if season is not None:
            team_index.update_params({"Season": season})

        logger.info(f"ENDPOINT: {team_index.get_endpoint()}")
        logger.info(f"PARAMS: {team_index.get_params()}")

        team_index.get_request()
        team_index.load_response()

        self._frame = team_index.get_table()
