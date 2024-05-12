"""Custom logging handlers for nbapi."""

import logging
import os
import sys
from typing import Union


def get_logger(logger_name: str = None) -> logging.Logger:
    """Creates a custom logger for handling messages from `nbapi` to `stderr`.

    The logger name hierarchy is analogous to the Python package hierarchy, and
    identical to it if you organise your loggers on a per-module basis using the
    recommended construction `logging.getLogger(__name__)`. That’s because in a module,
    `__name__` is the module’s name in the Python package namespace.

    Args:
        logger_name: Name to assign to the logger, e.g. `__name__` or `__file__`.
    Returns:
        Logger
    """

    ch = logging.StreamHandler(stream=sys.stdout)
    ch.setFormatter(CustomFormatter())
    logging.basicConfig(handlers=[ch])
    logger = logging.getLogger(logger_name)
    return logger


def set_verbosity(level: Union[str, int, bool] = logging.WARNING) -> None:
    """Sets logging level for the `nbapi` module.

    Valid strings = ["WARNING", "INFO", "DEBUG", "ERROR", "CRITICAL"]
    Valid ints = [0, 10, 20, 30, 40, 50]

    logging.DEBUG if verbose==True
    logging.WARNING if verbose==False

    Args:
        level: Logging level. ["WARNING", "INFO", "DEBUG", "ERROR", "CRITICAL"]
            You can pass `int` representations of these levels.
            You can a boolean True = "INFO" / False = "WARNING"
    """

    level = os.environ.get("LOGLEVEL", level)

    top_logger = get_logger("nbapi")

    if isinstance(level, bool):
        if level:
            top_logger.setLevel(logging.DEBUG)
        else:
            top_logger.setLevel(logging.WARNING)
    elif isinstance(level, str):
        if level in ["WARNING", "INFO", "DEBUG", "ERROR", "CRITICAL"]:
            top_logger.setLevel(level)
    elif isinstance(level, int):
        if level in [0, 10, 20, 30, 40, 50]:
            top_logger.setLevel(level)


class CustomFormatter(logging.Formatter):
    """Custom colored log output."""

    gray = "\x1b[38;20m"
    yellow = "\x1b[33;20m"
    red = "\x1b[31;20m"
    white_on_red = "\x1b[31;47m"
    reset = "\x1b[0m"

    format = "  %(asctime)s | %(levelname)8s | %(message)s"

    datefmt = "%H:%M:%S"

    FORMATS = {
        logging.INFO: gray + format + reset,
        logging.DEBUG: gray + format + reset,
        logging.WARNING: yellow + format + reset,
        logging.ERROR: red + format + reset,
        logging.CRITICAL: white_on_red + format + reset,
    }

    def format(self, record):
        """Custom format records."""
        log_format = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_format)
        return formatter.format(record)
