from setuptools import find_namespace_packages, setup

PACKAGENAME = "nbapi"
VERSION = "0.0.1"
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
    url="git@github.com:jondeans/nbapi.git",
    author="@jondeans",
    license="",
    packages=find_namespace_packages(),
    zip_safe=False,
    install_requires=INSTALL_REQUIRES,
)
