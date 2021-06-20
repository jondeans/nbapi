"""Classes around Teams and Lists of Teams."""

import pkgutil
from pathlib import Path

import datatable as dt
from datatable import f

import nbapi.core.logger as log
from nbapi.endpoints.stats.commonteamroster import CommonTeamRoster
from nbapi.endpoints.stats.commonteamyears import CommonTeamYears
from nbapi.endpoints.stats.teamdetails import TeamDetails
from nbapi.endpoints.stats.teaminfocommon import TeamInfoCommon

logger = log.get_logger(__name__)


class TeamList:
    """Represents a list of teams from NBA Stats."""

    def __init__(self):
        endpoint = CommonTeamYears()

        logger.info(f"ENDPOINT: {endpoint.get_endpoint()}")
        logger.info(f"PARAMS: {endpoint.get_params()}")

        endpoint.get_request()
        self._info = endpoint.load_response(idx=0)

    def find_team(self, query=None, by=None):
        if by == "id":
            return self._info[f.TEAM_ID == query, :]
        if by == "abbr":
            return self._info[f.ABBREVIATION == query, :]

    def to_csv(self, directory=None):
        directory = Path(directory)
        self._info.to_csv(str(directory / "teamlist_info.csv"))

    def get_info(self):
        return self._info


class TeamSummary:
    """Represents basic info on a single team from NBA Stats."""

    _params = None

    def __init__(self, team_id=None, season=None):
        endpoint = TeamInfoCommon()

        if team_id is not None:
            endpoint.update_params({"TeamID": int(team_id)})
        if season is not None:
            endpoint.update_params({"Season": season})

        logger.info(f"ENDPOINT: {endpoint.get_endpoint()}")
        logger.info(f"PARAMS: {endpoint.get_params()}")

        endpoint.get_request()
        self._info = endpoint.load_response(idx=0)
        self._ranks = endpoint.load_response(idx=1)
        self._params = endpoint.get_params()

    def to_csv(self, directory=None):
        directory = Path(directory)
        team_abbr = _get_team_abbrev(self._params["TeamID"])

        prefix = f"teamsummary_{team_abbr}_{self._params['Season']}"

        self._info.to_csv(str(directory / (prefix + "_info.csv")))
        logger.info(
            f"Saved {self._info.nrows:,} records to {directory / (prefix + '_info.csv')}."
        )
        self._ranks.to_csv(str(directory / (prefix + "_ranks.csv")))
        logger.info(
            f"Saved {self._ranks.nrows:,} records to {directory / (prefix + '_ranks.csv')}."
        )

    def get_info(self):
        return self._info

    def get_ranks(self):
        return self._ranks


class TeamDetail:
    """Represents details on a single team from NBA Stats."""

    _params = None

    def __init__(self, team_id=None):
        endpoint = TeamDetails()

        if team_id is not None:
            endpoint.update_params({"TeamID": int(team_id)})

        logger.info(f"ENDPOINT: {endpoint.get_endpoint()}")
        logger.info(f"PARAMS: {endpoint.get_params()}")

        endpoint.get_request()
        self._background = endpoint.load_response(idx=0)
        self._history = endpoint.load_response(idx=1)
        self._social_sites = endpoint.load_response(idx=2)
        self._awards_championships = endpoint.load_response(idx=3)
        self._awards_conf = endpoint.load_response(idx=4)
        self._awards_div = endpoint.load_response(idx=5)
        self._hof = endpoint.load_response(idx=6)
        self._retired = endpoint.load_response(idx=7)
        self._params = endpoint.get_params()

    def to_csv(self, directory=None):
        directory = Path(directory)
        team_abbr = _get_team_abbrev(self._params["TeamID"])

        prefix = f"teamdetails_{team_abbr}"

        self._background.to_csv(str(directory / (prefix + "_background.csv")))
        self._history.to_csv(str(directory / (prefix + "_history.csv")))
        self._social_sites.to_csv(str(directory / (prefix + "_social_sites.csv")))
        self._awards_championships.to_csv(
            str(directory / (prefix + "_awards_championships.csv"))
        )
        self._awards_conf.to_csv(str(directory / (prefix + "_awards_conf.csv")))
        self._awards_div.to_csv(str(directory / (prefix + "_awards_div.csv")))
        self._hof.to_csv(str(directory / (prefix + "_hof.csv")))
        self._retired.to_csv(str(directory / (prefix + "_retired.csv")))

    def get_background(self):
        return self._background

    def get_history(self):
        return self._history

    def get_social_site(self):
        return self._social_sites

    def get_awards_championship(self):
        return self._awards_championships

    def get_awards_conf(self):
        return self._awards_conf

    def get_awards_div(self):
        return self._awards_div

    def get_hof(self):
        return self._hof

    def get_retired(self):
        return self._retired


class TeamCommonRoster:
    """Represents common roster info on a single team from NBA Stats."""

    _params = None

    def __init__(self, team_id=None, season=None):
        endpoint = CommonTeamRoster()

        if team_id is not None:
            endpoint.update_params({"TeamID": int(team_id)})
        if season is not None:
            endpoint.update_params({"Season": season})

        logger.info(f"ENDPOINT: {endpoint.get_endpoint()}")
        logger.info(f"PARAMS: {endpoint.get_params()}")

        endpoint.get_request()
        self._roster = endpoint.load_response(idx=0)
        self._coaches = endpoint.load_response(idx=1)
        self._params = endpoint.get_params()

    def to_csv(self, directory=None):
        directory = Path(directory)
        team_abbr = _get_team_abbrev(self._params["TeamID"])

        prefix = f"teamcommonroster_{team_abbr}_{self._params['Season']}"

        self._roster.to_csv(str(directory / (prefix + "_roster.csv")))
        self._coaches.to_csv(str(directory / (prefix + "_coaches.csv")))

    def get_roster(self):
        return self._roster

    def get_coaches(self):
        return self._coaches


def _get_team_abbrev(team_id):
    data = pkgutil.get_data(__name__, "data/teams.tsv").decode()
    df = dt.Frame(data)
    return df[f.id == team_id, "abbr"][0, 0]
