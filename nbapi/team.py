"""Classes around Teams and Lists of Teams."""

import pkgutil
from pathlib import Path
from typing import Union

import datatable as dt
from datatable import f

import nbapi.core.logger as log
from nbapi.core.constants import CURRENT_YEAR
from nbapi.core.types import FilePath
from nbapi.endpoints.stats.commonteamroster import CommonTeamRoster
from nbapi.endpoints.stats.commonteamyears import CommonTeamYears
from nbapi.endpoints.stats.teamdetails import TeamDetails
from nbapi.endpoints.stats.teaminfocommon import TeamInfoCommon

logger = log.get_logger(__name__)


def _get_team_abbrev(team_id: str) -> str:
    """Lookup team abbreviations."""
    team_data = pkgutil.get_data(__name__, "data/teams.tsv").decode()
    df = dt.Frame(team_data)
    return df[f.id == team_id, "abbr"][0, 0]


class TeamList:
    """Represents a list of teams from NBA Stats."""

    def __init__(self):
        endpoint = CommonTeamYears()

        logger.debug(f"ENDPOINT: {endpoint.get_endpoint()}")
        logger.debug(f"PARAMS: {endpoint.get_params()}")

        endpoint.get_request()

        self._data = endpoint.load_response()

    def find_team(self, query: str = None, by: str = None) -> dt.Frame:
        """Retrieve information for a single team."""
        if by == "id":
            return self._data[f.TEAM_ID == query, :]
        if by == "abbr":
            return self._data[f.ABBREVIATION == query, :]

    def to_csv(self, directory: FilePath) -> None:
        """Save full team table to disk."""
        directory = Path(directory)
        self._data.to_csv(str(directory / "teamlist_data.csv"))
        logger.info(
            f"Saved {self._data.nrows:,} records to {directory /  'teamlist_data.csv'}."
        )

    @property
    def data(self) -> dt.Frame:
        """Get the team info data table."""
        return self._data

    def get_active_teams(self) -> dt.Frame:
        """Get table with only active teams."""
        return self._data[f.MAX_YEAR == CURRENT_YEAR, :]


class TeamSummary:
    """Represents basic info on a single team from NBA Stats."""

    _params = None

    def __init__(self, team_id: Union[int, str], season: str):
        endpoint = TeamInfoCommon()

        if team_id:
            endpoint.update_params({"TeamID": int(team_id)})
        if season:
            endpoint.update_params({"Season": season})

        logger.debug(f"ENDPOINT: {endpoint.get_endpoint()}")
        logger.debug(f"PARAMS: {endpoint.get_params()}")

        endpoint.get_request()
        self._data = endpoint.load_response()
        self._ranks = endpoint.load_response(index=1)
        self._params = endpoint.get_params()

    def to_csv(self, directory: FilePath) -> None:
        """Save full summary and ranks tables to disk."""

        directory = Path(directory)

        team_abbr = _get_team_abbrev(self._params["TeamID"])

        prefix = f"teamsummary_{team_abbr}_{self._params['Season']}"

        self._data.to_csv(str(directory / (prefix + "_data.csv")))
        logger.info(
            f"Saved {self._data.nrows:,} records to {directory / (prefix + '_data.csv')}."
        )
        self._ranks.to_csv(str(directory / (prefix + "_ranks.csv")))
        logger.info(
            f"Saved {self._ranks.nrows:,} records to {directory / (prefix + '_ranks.csv')}."
        )

    @property
    def data(self) -> dt.Frame:
        """Get the team summary table."""
        return self._data

    @property
    def ranks(self) -> dt.Frame:
        """Get the team ranks."""
        return self._ranks


class TeamDetail:
    """Represents details on a single team from NBA Stats."""

    _params = None

    def __init__(self, team_id: Union[int, str]):
        endpoint = TeamDetails()

        if team_id:
            endpoint.update_params({"TeamID": int(team_id)})

        logger.debug(f"ENDPOINT: {endpoint.get_endpoint()}")
        logger.debug(f"PARAMS: {endpoint.get_params()}")

        endpoint.get_request()
        self._background = endpoint.load_response()
        self._history = endpoint.load_response(index=1)
        self._social_sites = endpoint.load_response(index=2)
        self._awards_championships = endpoint.load_response(index=3)
        self._awards_conf = endpoint.load_response(index=4)
        self._awards_div = endpoint.load_response(index=5)
        self._hof = endpoint.load_response(index=6)
        self._retired = endpoint.load_response(index=7)
        self._params = endpoint.get_params()

    def to_csv(self, directory: FilePath) -> None:
        """Save all tables to disk."""

        directory = Path(directory)

        team_abbr = _get_team_abbrev(self._params["TeamID"])

        prefix = f"teamdetails_{team_abbr}"

        self._background.to_csv(str(directory / (prefix + "_background.csv")))
        logger.info(
            f"Saved {self._background.nrows:,} records to {directory / (prefix + '_background.csv')}."
        )
        self._history.to_csv(str(directory / (prefix + "_history.csv")))
        logger.info(
            f"Saved {self._history.nrows:,} records to {directory / (prefix + '_history.csv')}."
        )
        self._social_sites.to_csv(str(directory / (prefix + "_social_sites.csv")))
        logger.info(
            f"Saved {self._social_sites.nrows:,} records to {directory / (prefix + '_social_sites.csv')}."
        )
        self._awards_championships.to_csv(
            str(directory / (prefix + "_awards_championships.csv"))
        )
        logger.info(
            f"Saved {self._awards_championships.nrows:,} records to {directory / (prefix + '_awards_championships.csv')}."
        )
        self._awards_conf.to_csv(str(directory / (prefix + "_awards_conf.csv")))
        logger.info(
            f"Saved {self._awards_conf.nrows:,} records to {directory / (prefix + '_awards_conf.csv')}."
        )
        self._awards_div.to_csv(str(directory / (prefix + "_awards_div.csv")))
        logger.info(
            f"Saved {self._awards_div.nrows:,} records to {directory / (prefix + '_awards_div.csv')}."
        )
        self._hof.to_csv(str(directory / (prefix + "_hof.csv")))
        logger.info(
            f"Saved {self._hof.nrows:,} records to {directory / (prefix + '_hof.csv')}."
        )
        self._retired.to_csv(str(directory / (prefix + "_retired.csv")))
        logger.info(
            f"Saved {self._retired.nrows:,} records to {directory / (prefix + '_retired.csv')}."
        )

    @property
    def background(self) -> dt.Frame:
        """Get the background table."""
        return self._background

    @property
    def history(self) -> dt.Frame:
        """Get the history table."""
        return self._history

    @property
    def social_sites(self) -> dt.Frame:
        """Get the social-sites table."""
        return self._social_sites

    @property
    def awards_championships(self) -> dt.Frame:
        """Get the awards-championships table."""
        return self._awards_championships

    @property
    def awards_conf(self) -> dt.Frame:
        """Get the awards-conf table."""
        return self._awards_conf

    @property
    def awards_div(self) -> dt.Frame:
        """Get the awards-div table."""
        return self._awards_div

    @property
    def hof(self) -> dt.Frame:
        """Get the hall-of-fame table."""
        return self._hof

    @property
    def retired(self) -> dt.Frame:
        """Get the retired table."""
        return self._retired


class TeamCommonRoster:
    """Represents common-roster info on a single team from NBA Stats."""

    _params = None

    def __init__(self, team_id: Union[int, str], season: str):
        endpoint = CommonTeamRoster()

        if team_id is not None:
            endpoint.update_params({"TeamID": int(team_id)})
        if season is not None:
            endpoint.update_params({"Season": season})

        logger.debug(f"ENDPOINT: {endpoint.get_endpoint()}")
        logger.debug(f"PARAMS: {endpoint.get_params()}")

        endpoint.get_request()
        self._roster = endpoint.load_response()
        self._coaches = endpoint.load_response(index=1)
        self._params = endpoint.get_params()

    def to_csv(self, directory: FilePath) -> None:
        """Save all tables to disk."""

        directory = Path(directory)
        team_abbr = _get_team_abbrev(self._params["TeamID"])

        prefix = f"teamcommonroster_{team_abbr}_{self._params['Season']}"

        self._roster.to_csv(str(directory / (prefix + "_roster.csv")))
        logger.info(
            f"Saved {self._roster.nrows:,} records to {directory / (prefix + '_roster.csv')}."
        )
        self._coaches.to_csv(str(directory / (prefix + "_coaches.csv")))
        logger.info(
            f"Saved {self._coaches.nrows:,} records to {directory / (prefix + '_coaches.csv')}."
        )

    @property
    def roster(self) -> dt.Frame:
        """Get the roster table."""
        return self._roster

    @property
    def coaches(self) -> dt.Frame:
        """Get the coaches table."""
        return self._coaches
