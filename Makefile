lint:
	black -S -t py37 -l 89 backend/
	isort -c backend/
	flake8 backend/

.PHONY: lint
