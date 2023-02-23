"""Dictionaries and Enums used throughout the project."""

from datetime import datetime
from enum import Enum

_curr_date = datetime.today()
_curr_month = _curr_date.month
_curr_year = _curr_date.year

if _curr_month >= 7:
    CURRENT_SEASON = f"{_curr_year}-{(_curr_year+1) % 100}"
    CURRENT_YEAR = _curr_year
else:
    CURRENT_SEASON = f"{_curr_year-1}-{_curr_year % 100}"
    CURRENT_YEAR = _curr_year - 1


class DefaultBlank:
    """Class with default empty string."""
    Default = ""


class DefaultN:
    """Class of Y/N with default N."""
    Y = "Y"
    N = "N"
    Default = N


class DefaultZero:
    """Class of '0'/'1' default '0'."""
    Zero = "0"
    One = "1"
    Default = "0"


class League:
    """League enum."""
    NBA = "00"
    ABA = "01"
    Default = NBA


class PerMode:
    """PerMode values, default PerGame."""
    Totals = "Totals"
    PerGame = "PerGame"
    MinutesPer = "MinutesPer"
    Per48 = "Per48"
    Per40 = "Per40"
    Per36 = "Per36"
    PerMinute = "PerMinute"
    PerPossession = "PerPossession"
    PerPlay = "PerPlay"
    Per100Possessions = "Per100Possessions"
    Per100Plays = "Per100Plays"
    Default = PerGame


class SeasonType:
    """SeasonType values, default Regular."""
    Regular = "Regular Season"
    Playoffs = "Playoffs"
    Default = Regular


class MeasureType:
    """MeasureType values, default Base."""
    Base = "Base"
    Advanced = "Advanced"
    Misc = "Misc"
    FourFactors = "Four Factors"
    Scoring = "Scoring"
    Opponent = "Opponent"
    Usage = "Usage"
    Default = Base


class PtMeasureType:
    """PtMeasureType values."""
    SpeedDistance = "SpeedDistance"


class GroupQuantity:
    """GroupQuantity values."""
    Default = 5


class Outcome(DefaultBlank):
    """Outcome values, default ''."""
    Win = "W"
    Loss = "L"


class Location(DefaultBlank):
    """Location values, default ''."""
    Home = "Home"
    Away = "Away"


class SeasonSegment(DefaultBlank):
    """SeasonSegment values, default ''."""
    EntireSeason = ""
    PreAllStar = "Pre All-Star"
    PostAllStar = "Post All-Star"


class DateFrom(DefaultBlank):
    """DateFrom values, default ''."""
    pass


class DateTo(DefaultBlank):
    """DateTo values, default ''."""
    pass


class VsConference(DefaultBlank):
    """VsConference values, default ''."""
    All = ""
    East = "East"
    West = "West"


class VsDivision(DefaultBlank):
    """VsDivision values, default ''."""
    All = ""
    Atlantic = "Atlantic"
    Central = "Central"
    Northwest = "Northwest"
    Pacific = "Pacific"
    Southeast = "Southeast"
    Southwest = "Southwest"


class GameSegment(DefaultBlank):
    """GameSegment values, default ''."""
    EntireGame = ""
    FirstHalf = "First Half"
    SecondHalf = "Second Half"
    Overtime = "Overtime"


class ClutchTime(DefaultBlank):
    """ClutchTime values, default ''."""
    Last5Min = "Last 5 Minutes"
    Last4Min = "Last 4 Minutes"
    Last3Min = "Last 3 Minutes"
    Last2Min = "Last 2 Minutes"
    Last1Min = "Last 1 Minutes"
    Last30Sec = "Last 30 Seconds"
    Last10Sec = "Last 10 Seconds"


class AheadBehind(DefaultBlank):
    """AheadBehind values, default ''."""
    AheadOrBehind = "Ahead or Behind"
    AheadOrTied = "Ahead or Tied"
    BehindOrTied = "Behind or Tied"


class PlusMinus(DefaultN):
    """PlusMinus values, default N."""
    pass


class PaceAdjust(DefaultN):
    """PaceAdjust values, default N."""
    pass


class Rank(DefaultN):
    """Rank values, default N."""
    pass


class OpponentTeamID(DefaultZero):
    """OpponentTeamID values, default '0'."""
    pass


class Period(DefaultZero):
    """Period values, default '0'."""
    AllQuarters = "0"
    FirstQuarter = "1"
    SecondQuarter = "2"
    ThirdQuarter = "3"
    FourthQuarter = "4"


class LastNGames(DefaultZero):
    """LastNGames values, default '0'."""
    pass


class PlayoffRound(DefaultZero):
    """PlayoffRound values, default '0'."""
    All = "0"
    QuarterFinals = "1"
    SemiFinals = "2"
    ConferenceFinals = "3"
    Finals = "4"


class Month(DefaultZero):
    """Month values, default '0'."""
    All = "0"
    October = "1"
    November = "2"
    December = "3"
    January = "4"
    February = "5"
    March = "6"
    April = "7"
    May = "8"
    June = "9"
    July = "10"
    August = "11"
    September = "12"


class RangeType(DefaultZero):
    """RangeType values, default '0'."""
    pass


class StartRange(DefaultZero):
    """StartRange values, default '0'."""
    pass


class EndRange(DefaultZero):
    """EndRange values, default '0'."""
    pass


class StatCategory(Enum):
    """StatCategory enum."""
    PTS = "PTS"
    FGM = "FGM"
    FGA = "FGA"
    FG_PCT = "FG%"
    FG3M = "3PM"
    FG3A = "3PA"
    FG3_PCT = "3P%"
    FTM = "FTM"
    FTA = "FTA"
    FT_PCT = "FT%"
    OREB = "OREB"
    DREB = "DREB"
    REB = "REB"
    AST = "AST"
    STL = "STL"
    BLK = "BLK"
    TOV = "TOV"
    EFF = "EFF"
    AST_TOV = "AST/TO"
    STL_TOV = "STL/TOV"
    PF = "PF"
    Default = PTS


class Scope(Enum):
    """Scope enum."""
    AllPlayers = "S"
    Rookies = "Rookies"
    Default = AllPlayers


class PlayerScope(Enum):
    """PlayerScope enum."""
    # TODO: Why is this it's own thing?
    AllPlayers = "All Players"
    Rookies = "Rookie"
    Default = AllPlayers


class PlayerOrTeam(Enum):
    """PlayerOrTeam enum."""
    Player = "Player"
    Team = "Team"
    Default = Player


class GameScope(Enum):
    """GameScope enum."""
    Season = "Season"
    Last10 = "Last 10"
    Yesterday = "Yesterday"
    Finals = "Finals"
    Default = Season


class Conference(VsConference):
    """Conference values."""
    pass


class Division(VsDivision):
    """Division values."""
    pass


class TeamID(DefaultZero):
    """TeamID values, default '0'."""
    pass


class GameID(DefaultBlank):
    """GameID values, default ''."""
    pass


class RookieYear(DefaultBlank):
    """RookieYear values, default ''."""
    pass


class PlayerExperience(DefaultBlank):
    """PlayerExperience values, default ''."""
    Rookie = "Rookie"
    Sophomore = "Sophomore"
    Veteran = "Veteran"


class PlayerPosition(DefaultBlank):
    """PlayerPosition values, default ''."""
    Forward = "F"
    Center = "C"
    Guard = "G"


class StarterBench(DefaultBlank):
    """StarterBench values, default ''."""
    Starters = "Starters"
    Bench = "Bench"


class DraftYear(DefaultBlank):
    """DraftYear values, default ''."""
    pass


class DraftPick(DefaultBlank):
    """DraftPick values, default ''."""
    FirstRound = "1st+Round"
    SecondRound = "2nd+Round"
    FirstPick = "1st+Pick"
    Lottery = "Lottery+Pick"
    Top5 = "Top+5+Pick"
    Top10 = "Top+10+Pick"
    Top15 = "Top+15+Pick"
    Top20 = "Top+20+Pick"
    Top25 = "Top+25+Pick"
    Picks11Thru20 = "Picks+11+Thru+20"
    Picks21Thru30 = "Picks+21+Thru+30"
    Undrafted = "Undrafted"


class College(DefaultBlank):
    """College values, default ''."""
    pass


class Country(DefaultBlank):
    """Country values, default ''."""
    pass


class Height(DefaultBlank):
    """Height values, default ''.

    Example:
        for greater than 6ft8 api call should be GT+6-8
        for lower than 7ft3 api call should be LT+7-3
    """
    pass


class Weight(DefaultBlank):
    """Weight values, default ''.

    Example:
        for greater than 225lbs api call should be GT+225lbs
    """
    pass


class Counter(Enum):
    """Counter enum."""
    Default = "1000"


class Sorter(Enum):
    """Sorter enum."""
    PTS = "PTS"
    FGM = "FGM"
    FGA = "FGA"
    FG_PCT = "FG_PCT"
    FG3M = "FG3M"
    FG3A = "FG3A"
    FG3_PCT = "FG3_PCT"
    FTM = "FTM"
    FTA = "FTA"
    FT_PCT = "FT_PCT"
    OREB = "OREB"
    DREB = "DREB"
    AST = "AST"
    STL = "STL"
    BLK = "BLK"
    TOV = "TOV"
    REB = "REB"
    Default = PTS


class Direction(Enum):
    """Direction enum."""
    DESC = "DESC"
    ASC = "ASC"
    Default = DESC
