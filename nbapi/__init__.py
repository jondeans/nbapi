"""nbapi"""

from datetime import timedelta

__title__ = "nbapi"
__version__ = "v0.0.1"
__author__ = "jondeans"
__email__ = "jrdeans@gmail.com"
__summary__ = "Python interface to NBA Stats API."
__uri__ = "git@github.com:jondeans/nbapi.git"
__license__ = "All rights reserved."

CACHE_EXPIRE_MINUTES = 10

# Set up requests-cache, if available
HAS_REQUESTS_CACHE = True
try:
    from requests_cache import install_cache

    install_cache("nbapi_cache", expire_after=timedelta(minutes=CACHE_EXPIRE_MINUTES))
except ModuleNotFoundError as err:
    HAS_REQUESTS_CACHE = False
    print(err)
