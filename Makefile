check:
	black . --check
	isort -c .
	flake8 .

env:
	conda env create --file environment.yml

fix:
	black .
	isort .

test:
	python -m pytest tests

.PHONY: check env fix test
