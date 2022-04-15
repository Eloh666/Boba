install:
	pip install -r requirements.txt

install-dev: install
	pip install -e ".[dev]"

lint:
	black -l 150 --check src config tests

run:
	python3 src/main.py

freeze:
	CUSTOM_COMPILE_COMMAND="make freeze" pip-compile --output-file requirements.txt setup.py

freeze-upgrade:
	CUSTOM_COMPILE_COMMAND="make freeze" pip-compile --upgrade --output-file requirements.txt setup.py

.PHONY: install install-dev lint unit component coverage test run run-dev freeze freeze-upgrade
