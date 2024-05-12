"""nbapi"""

from datetime import timedelta

CACHE_EXPIRE_MINUTES = 10

# Set up requests-cache, if available
HAS_REQUESTS_CACHE = True
try:
    from requests_cache import install_cache

    install_cache(
        "nbapi_cache",
        expire_after=timedelta(minutes=CACHE_EXPIRE_MINUTES),
        use_temp=True,
        backend="filesystem",
    )
except ModuleNotFoundError as err:
    HAS_REQUESTS_CACHE = False
    print(err)
