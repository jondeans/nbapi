from setuptools import find_packages, setup

import nbapi

PACKAGENAME = "nbapi"
VERSION = nbapi.__version__

INSTALL_REQUIRES = [
    "pandas",
    "pip",
    "python>=3.8",
    "requests",
    "setuptools",
]

setup(
    name=PACKAGENAME,
    version=VERSION,
    description="Python interface to NBA Stats API.",
    url="http://github.com/jondeans/nbapi",
    author="Jon Deans",
    packages=find_packages(),
    zip_safe=False,
    install_requires=INSTALL_REQUIRES,
)
