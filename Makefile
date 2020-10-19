tests:
	poetry run pytest --cov=backend --cov-branch backend/tests
	poetry run black --check backend/
	poetry run isort -c backend/
	poetry run flake8 backend/
	poetry run coverage html

lint:
	poetry run black backend/
	poetry run isort backend/

build:
	cd frontend; yarn build

docs:
	rm -rf docs/_build/html docs/_build/doctrees
	poetry run sphinx-build -M html docs docs/_build

setup.py:
	dephell deps convert --from pyproject.toml --to setup.py

.PHONY: tests setup.py lint build docs
