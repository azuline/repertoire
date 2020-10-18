tests:
	poetry run pytest --cov=backend backend/tests
	poetry run black --check -S -t py37 -l 89 backend/
	poetry run isort -c backend/
	poetry run flake8 backend/

setup.py:
	dephell deps convert --from pyproject.toml --to setup.py

lint:
	poetry run black -S -t py37 -l 89 backend/
	poetry run isort -c backend/

build:
	cd frontend; yarn build

.PHONY: tests setup.py lint build
