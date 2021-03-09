"""Dictionaries and Enums used throughout the project."""

from datetime import datetime
from enum import Enum

_curr_date = datetime.today()
_curr_month = _curr_date.month
_curr_year = _curr_date.year

if _curr_month >= 7:
    CURRENT_SEASON = f"{_curr_year}-{(_curr_year+1) % 100}"
else:
    CURRENT_SEASON = f"{_curr_year-1}-{_curr_year % 100}"


class DefaultBlank:
    Default = ""


class DefaultN:
    Y = "Y"
    N = "N"
    Default = N


class DefaultZero:
    Zero = "0"
    One = "1"
    Default = "0"


class League:
    NBA = "00"
    ABA = "01"
    Default = NBA


class PerMode:
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
    Regular = "Regular Season"
    Playoffs = "Playoffs"
    Default = Regular


class MeasureType:
    Base = "Base"
    Advanced = "Advanced"
    Misc = "Misc"
    FourFactors = "Four Factors"
    Scoring = "Scoring"
    Opponent = "Opponent"
    Usage = "Usage"
    Default = Base


class PtMeasureType:
    SpeedDistance = "SpeedDistance"


class GroupQuantity:
    Default = 5


class Outcome(DefaultBlank):
    Win = "W"
    Loss = "L"


class Location(DefaultBlank):
    Home = "Home"
    Away = "Away"


class SeasonSegment(DefaultBlank):
    EntireSeason = ""
    PreAllStar = "Pre All-Star"
    PostAllStar = "Post All-Star"


class DateFrom(DefaultBlank):
    pass


class DateTo(DefaultBlank):
    pass


class VsConference(DefaultBlank):
    All = ""
    East = "East"
    West = "West"


class VsDivision(DefaultBlank):
    All = ""
    Atlantic = "Atlantic"
    Central = "Central"
    Northwest = "Northwest"
    Pacific = "Pacific"
    Southeast = "Southeast"
    Southwest = "Southwest"


class GameSegment(DefaultBlank):
    EntireGame = ""
    FirstHalf = "First Half"
    SecondHalf = "Second Half"
    Overtime = "Overtime"


class ClutchTime(DefaultBlank):
    Last5Min = "Last 5 Minutes"
    Last4Min = "Last 4 Minutes"
    Last3Min = "Last 3 Minutes"
    Last2Min = "Last 2 Minutes"
    Last1Min = "Last 1 Minutes"
    Last30Sec = "Last 30 Seconds"
    Last10Sec = "Last 10 Seconds"


class AheadBehind(DefaultBlank):
    AheadOrBehind = "Ahead or Behind"
    AheadOrTied = "Ahead or Tied"
    BehindOrTied = "Behind or Tied"


class PlusMinus(DefaultN):
    pass


class PaceAdjust(DefaultN):
    pass


class Rank(DefaultN):
    pass


class OpponentTeamID(DefaultZero):
    pass


class Period(DefaultZero):
    AllQuarters = "0"
    FirstQuarter = "1"
    SecondQuarter = "2"
    ThirdQuarter = "3"
    FourthQuarter = "4"


class LastNGames(DefaultZero):
    pass


class PlayoffRound(DefaultZero):
    All = "0"
    QuarterFinals = "1"
    SemiFinals = "2"
    ConferenceFinals = "3"
    Finals = "4"


class Month(DefaultZero):
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
    pass


class StartRange(DefaultZero):
    pass


class EndRange(DefaultZero):
    pass


class StatCategory(Enum):
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
    AllPlayers = "S"
    Rookies = "Rookies"
    Default = AllPlayers


class PlayerScope(Enum):
    # TODO: Why is this it's own thing?
    AllPlayers = "All Players"
    Rookies = "Rookie"
    Default = AllPlayers


class PlayerOrTeam(Enum):
    Player = "Player"
    Team = "Team"
    Default = Player


class GameScope(Enum):
    Season = "Season"
    Last10 = "Last 10"
    Yesterday = "Yesterday"
    Finals = "Finals"
    Default = Season


class Conference(VsConference):
    pass


class Division(VsDivision):
    pass


class TeamID(DefaultZero):
    pass


class GameID(DefaultBlank):
    pass


class RookieYear(DefaultBlank):
    pass


class PlayerExperience(DefaultBlank):
    Rookie = "Rookie"
    Sophomore = "Sophomore"
    Veteran = "Veteran"


class PlayerPosition(DefaultBlank):
    Forward = "F"
    Center = "C"
    Guard = "G"


class StarterBench(DefaultBlank):
    Starters = "Starters"
    Bench = "Bench"


class DraftYear(DefaultBlank):
    pass


class DraftPick(DefaultBlank):
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
    pass


class Country(DefaultBlank):
    pass


class Height(DefaultBlank):
    """
    Example:
    for greater than 6ft8 api call should be GT+6-8
    for lower than 7ft3 api call should be LT+7-3
    """

    pass


class Weight(DefaultBlank):
    """
    Example:
    for greater than 225lbs api call should be GT+225lbs
    """

    pass


class Counter(Enum):
    Default = "1000"


class Sorter(Enum):
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
    DESC = "DESC"
    ASC = "ASC"
    Default = DESC
