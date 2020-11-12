tests:
	poetry run pytest --cov=. --cov-branch tests/
	poetry run mypy src/
	poetry run black --check .
	poetry run isort -c .
	poetry run flake8 .
	poetry run coverage html

check:
	poetry run mypy src/

lint:
	poetry run black .
	poetry run isort .

docs:
	rm -rf ../docs/_build/html ../docs/_build/doctrees
	poetry run sphinx-build -M html ../docs ../docs/_build

setup.py:
	dephell deps convert --from pyproject.toml --to setup.py

.PHONY: tests check lint docs setup.py
