tests:
	cd backend; \
		poetry run pytest --cov=. --cov-branch tests/; \
		poetry run black --check .; \
		poetry run isort -c .; \
		poetry run flake8 .; \
		poetry run coverage html

lint:
	cd backend; \
		poetry run black .; \
		poetry run isort .
	cd frontend; \
		yarn lint

build:
	cd frontend; yarn build

docs:
	rm -rf docs/_build/html docs/_build/doctrees
	cd backend; poetry run sphinx-build -M html ../docs ../docs/_build

setup.py:
	cd backend; dephell deps convert --from pyproject.toml --to setup.py

.PHONY: tests setup.py lint build docs
