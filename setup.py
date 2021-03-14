from setuptools import find_packages, setup

import nbapi

PACKAGENAME = "nbapi"
VERSION = nbapi.__version__

INSTALL_REQUIRES = [
    "datatable",
    "pandas",
    "pip",
    "python>=3.8",
    "requests",
    "requests-cache",
    "setuptools",
]

setup(
    name=PACKAGENAME,
    version=VERSION,
    description="Python interface to NBA Stats API.",
    url="http://github.com/jondeans/nbapi",
    author="jondeans",
    keywords="nba sports",
    packages=find_packages(exclude=["docs", "tests*"]),
    zip_safe=False,
    install_requires=INSTALL_REQUIRES,
)
