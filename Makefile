tests:
	pytest --cov=backend backend/tests

setup.py:
	dephell deps convert --from pyproject.toml --to setup.py

lint:
	black -S -t py37 -l 89 backend/
	isort -c backend/
	flake8 backend/

build:
	cd frontend; yarn build

.PHONY: tests setup.py lint build
