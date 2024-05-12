VENVDIR=.venv
VENV=$(VENVDIR)/bin
VENVPYTHON=$(VENV)/python
VENVPIP=$(VENV)/pip

venv: $(VENV)/activate
$(VENV)/activate: pyproject.toml
	test -d $(VENVDIR) || python3 -m venv $(VENVDIR)
	$(VENVPIP) install -U pip
	$(VENVPIP) install -e .
	touch $(VENV)/activate

.PHONY: install-dev
install-dev: venv
	$(VENVPIP) install -e ".[dev]"

.PHONY: clean
clean:
	rm -rf $(VENVDIR)

.PHONY: check
check:
	$(VENV)/ruff check src/ tests/
	$(VENV)/ruff format --check src/ tests/

.PHONY: fix
fix:
	$(VENV)/ruff check --fix src/ tests/
	$(VENV)/ruff format src/ tests/

.PHONY: test
test:
	$(VENVPYTHON) -m pytest tests