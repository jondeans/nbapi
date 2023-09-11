VENV = venv
PYTHON_VERSION = 3.11
PYTHON = $(VENV)/bin/python
PIP = $(VENV)/bin/pip

.PHONY: check
check:
	black src/ --check
	ruff check src/
# 	isort -c src/
# 	flake8 src/

.PHONY: clean
clean:
	rm -rf $(VENV)

venv:
	python -m venv $(VENV)
	$(PIP) install -U pip

.PHONY: fix
fix:
	black src/
	ruff src/
# 	isort src/

.PHONY: install
install: venv
	$(PIP) install -e .

.PHONY: install-dev
install-dev: venv
	$(PIP) install -e ".[dev]"

.PHONY: test
test:
	$(PYTHON) -m pytest tests
