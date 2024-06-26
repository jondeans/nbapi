"""Classes around Teams and Lists of Teams."""

import pkgutil
from pathlib import Path
from typing import Union

import pandas as pd

from src.nbapi.core.types import FilePath
from src.nbapi.endpoints.stats.commonteamroster import CommonTeamRoster
from src.nbapi.endpoints.stats.commonteamyears import CommonTeamYears
from src.nbapi.endpoints.stats.teamdetails import TeamDetails
from src.nbapi.endpoints.stats.teaminfocommon import TeamInfoCommon

from loguru import logger


def _get_team_abbrev(team_id: str) -> str:
    """Lookup team abbreviations."""
    team_data = pkgutil.get_data(__name__, "data/teams.tsv").decode()
    df = pd.DataFrame(team_data)
    return df.query(f"id == {team_id}")["abbr"][0, 0]


class TeamList:
    """Represents a list of teams from NBA Stats."""

    def __init__(self):
        endpoint = CommonTeamYears()

        logger.debug(f"ENDPOINT: {endpoint.endpoint}")
        logger.debug(f"PARAMS: {endpoint.params}")

        endpoint.get_request()
        self._data = endpoint.load_response()

    def find_team(self, query: str, by: str) -> pd.DataFrame:
        """Retrieve information for a single team."""
        if by == "id":
            return self._data.query(f"TEAM_ID == {query}")
        if by == "abbr":
            return self._data.query(f"ABBREVIATION == {query}")

    def to_csv(self, directory: FilePath) -> None:
        """Save full team table to disk."""
        directory = Path(directory)
        directory.expanduser().absolute().mkdir(parents=True, exist_ok=True)
        self._data.to_csv(str(directory / "teamlist_data.csv"))
        logger.info(f"Saved {self._data.nrows:,} records to {directory /  'teamlist_data.csv'}.")

    @property
    def data(self) -> pd.DataFrame:
        """Get the team info data table."""
        return self._data.copy()

    def get_active_teams(self) -> pd.DataFrame:
        """Get table with only active teams."""
        return self._data.query("MAX_YEAR == CURRENT_YEAR")


class TeamSummary:
    """Represents basic info on a single team from NBA Stats."""

    def __init__(self, team_id: Union[int, str], season: str = None):
        endpoint = TeamInfoCommon()

        endpoint.update_params({"TeamID": int(team_id)})
        if season is not None:
            endpoint.update_params({"Season": season})

        logger.debug(f"ENDPOINT: {endpoint.endpoint}")
        logger.debug(f"PARAMS: {endpoint.params}")

        endpoint.get_request()

        self._data = endpoint.load_response()
        self._ranks = endpoint.load_response(index=1)
        self._team_id = int(team_id)
        self._season = endpoint.params["Season"]

    def to_csv(self, directory: FilePath) -> None:
        """Save full summary and ranks tables to disk."""

        directory = Path(directory)
        directory.expanduser().absolute().mkdir(parents=True, exist_ok=True)

        team_abbr = _get_team_abbrev(self._team_id)
        prefix = f"teamsummary_{team_abbr}_{self._season}"

        self._data.to_csv(str(directory / (prefix + "_data.csv")))
        logger.info(f"Saved {self._data.nrows:,} records to {directory / (prefix + '_data.csv')}.")
        self._ranks.to_csv(str(directory / (prefix + "_ranks.csv")))
        logger.info(
            f"Saved {self._ranks.nrows:,} records to {directory / (prefix + '_ranks.csv')}."
        )

    @property
    def data(self) -> pd.DataFrame:
        """Get the team summary table."""
        return self._data.copy()

    @property
    def ranks(self) -> pd.DataFrame:
        """Get the team ranks."""
        return self._ranks.copy()


class TeamDetail:
    """Represents details on a single team from NBA Stats."""

    _params = None

    def __init__(self, team_id: Union[int, str]):
        endpoint = TeamDetails()
        endpoint.update_params({"TeamID": int(team_id)})

        logger.debug(f"ENDPOINT: {endpoint.endpoint}")
        logger.debug(f"PARAMS: {endpoint.params}")

        endpoint.get_request()
        self._background = endpoint.load_response()
        self._history = endpoint.load_response(index=1)
        self._social_sites = endpoint.load_response(index=2)
        self._awards_championships = endpoint.load_response(index=3)
        self._awards_conf = endpoint.load_response(index=4)
        self._awards_div = endpoint.load_response(index=5)
        self._hof = endpoint.load_response(index=6)
        self._retired = endpoint.load_response(index=7)
        self._team_id = int(team_id)

    def to_csv(self, directory: FilePath) -> None:
        """Save all tables to disk."""

        directory = Path(directory)
        directory.expanduser().absolute().mkdir(parents=True, exist_ok=True)

        team_abbr = _get_team_abbrev(self._team_id)
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
        self._awards_championships.to_csv(str(directory / (prefix + "_awards_championships.csv")))
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
        logger.info(f"Saved {self._hof.nrows:,} records to {directory / (prefix + '_hof.csv')}.")
        self._retired.to_csv(str(directory / (prefix + "_retired.csv")))
        logger.info(
            f"Saved {self._retired.nrows:,} records to {directory / (prefix + '_retired.csv')}."
        )

    @property
    def background(self) -> pd.DataFrame:
        """Get the background table."""
        return self._background.copy()

    @property
    def history(self) -> pd.DataFrame:
        """Get the history table."""
        return self._history.copy()

    @property
    def social_sites(self) -> pd.DataFrame:
        """Get the social-sites table."""
        return self._social_sites.copy()

    @property
    def awards_championships(self) -> pd.DataFrame:
        """Get the awards-championships table."""
        return self._awards_championships.copy()

    @property
    def awards_conf(self) -> pd.DataFrame:
        """Get the awards-conf table."""
        return self._awards_conf.copy()

    @property
    def awards_div(self) -> pd.DataFrame:
        """Get the awards-div table."""
        return self._awards_div.copy()

    @property
    def hof(self) -> pd.DataFrame:
        """Get the hall-of-fame table."""
        return self._hof.copy()

    @property
    def retired(self) -> pd.DataFrame:
        """Get the retired table."""
        return self._retired.copy()


class TeamCommonRoster:
    """Represents common-roster info on a single team from NBA Stats."""

    def __init__(self, team_id: Union[int, str], season: str = None):
        endpoint = CommonTeamRoster()

        endpoint.update_params({"TeamID": int(team_id)})
        if season is not None:
            endpoint.update_params({"Season": season})

        logger.debug(f"ENDPOINT: {endpoint.endpoint}")
        logger.debug(f"PARAMS: {endpoint.params}")

        endpoint.get_request()
        self._roster = endpoint.load_response()
        self._coaches = endpoint.load_response(index=1)
        self._team_id = int(team_id)
        self._season = endpoint.params["Season"]

    def to_csv(self, directory: FilePath) -> None:
        """Save all tables to disk."""

        directory = Path(directory)
        directory.expanduser().absolute().mkdir(parents=True, exist_ok=True)

        team_abbr = _get_team_abbrev(self._team_id)
        prefix = f"teamcommonroster_{team_abbr}_{self._season}"

        self._roster.to_csv(str(directory / (prefix + "_roster.csv")))
        logger.info(
            f"Saved {self._roster.nrows:,} records to {directory / (prefix + '_roster.csv')}."
        )
        self._coaches.to_csv(str(directory / (prefix + "_coaches.csv")))
        logger.info(
            f"Saved {self._coaches.nrows:,} records to {directory / (prefix + '_coaches.csv')}."
        )

    @property
    def roster(self) -> pd.DataFrame:
        """Get the roster table."""
        return self._roster.copy()

    @property
    def coaches(self) -> pd.DataFrame:
        """Get the coaches table."""
        return self._coaches.copy()
