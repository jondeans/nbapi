from pathlib import Path

import pkg_resources
from setuptools import setup

with Path("requirements.txt").open() as reqs:
    install_requires = [str(req) for req in pkg_resources.parse_requirements(reqs)]

with Path("requirements-dev.txt").open() as reqs:
    install_requires_dev = [str(req) for req in pkg_resources.parse_requirements(reqs)]

setup(install_requires=install_requires, extras_requires={"dev": install_requires_dev})
