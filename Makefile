check:
	black nbapi --check
	isort -c nbapi
	flake8 nbapi

dev:
	pip install -r requirements-dev.txt
	pre-commit install

env:
	conda env create -f environment.yaml

fix:
	black nbapi
	isort nbapi

update-env:
	conda env update -f environment.yaml -prune

.PHONY: check dev env fix update-env
