"""Custom logging handlers."""

import logging


def get_logger(logger_name, level=logging.INFO) -> logging.Logger:
    """Creates a custom logger for handling messages.

    The logger name hierarchy is analogous to the Python package hierarchy, and
    identical to it if you organise your loggers on a per-module basis using the
    recommended construction `logging.getLogger(__name__)`. That’s because in a module,
    `__name__` is the module’s name in the Python package namespace.

    Args:
        logger_name: Name to assign to the logger, e.g. `__name__` or `__file__`.
        level: Level of logging to return.
    Returns:
        logger
    """
    logging.basicConfig(
        level=level,
        format="%(levelname)8s : %(asctime)s : %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )
    return logging.getLogger(logger_name)


def set_verbosity(verbose=False):
    """Sets logging level for the module.

    logging.DEBUG if verbose==True
    logging.WARNING if verbose==False

    Args:
        verbose: Boolean flag to set logging level to DEBUG if True.
    """

    top_logger = logging.getLogger("nbapi")
    if verbose:
        top_logger.setLevel(logging.DEBUG)
    else:
        top_logger.setLevel(logging.WARNING)
