#!/usr/bin/env python3

from jinja2 import Environment, FileSystemLoader
from pathlib import Path

SRC = Path(__file__).absolute().parent
WORKFLOWS = SRC.parent / "workflows"

# Define data

backend_data = dict(
    jobs=[
        dict(
            id="test",
            name="Test",
            steps=[
                dict(
                    name="Run tests",
                    run="poetry run pytest --cov-report=xml --cov=. --cov-branch tests/",
                ),
                dict(
                    name="Upload coverage",
                    run="bash <(curl -s https://codecov.io/bash) -cF python",
                ),
            ],
        ),
        dict(
            id="type_check",
            name="Type check",
            steps=[
                dict(
                    name="Download mypy cache",
                    uses="actions/download-artifact@v2",
                    with_=dict(name=".mypy_cache"),
                ),
                dict(name="Run type check", run="make typecheck"),
                dict(
                    name="Upload mypy cache",
                    uses="actions/download-artifact@v2",
                    with_=dict(name=".mypy_cache", path=".mypy_cache"),
                ),
            ],
        ),
        dict(
            id="lint_check",
            name="Lint check",
            steps=[dict(name="Run lint check", run="make lintcheck")],
        ),
        dict(
            id="schema",
            name="Schema",
            steps=[
                dict(name="Generate schema", run="make schema"),
                dict(name="Diff", run="git diff"),
                dict(
                    name="Compare",
                    run="bash -c '[[ -z $(git status -s) ]] || (exit 1)'",
                ),
            ],
        ),
        dict(
            id="setupfiles",
            name="Setup files",
            steps=[
                dict(name="Generate setup files", run="make setupfiles"),
                dict(name="Diff", run="git diff"),
                dict(
                    name="Compare",
                    run="bash -c '[[ -z $(git status -s) ]] || (exit 1)'",
                ),
            ],
        ),
    ],
)

frontend_data = dict(
    jobs=[
        dict(
            id="type_check",
            name="Type check",
            steps=[dict(name="Run type check", run="CI=true yarn tsc")],
        ),
        dict(
            id="lint_check",
            name="Lint check",
            steps=[
                dict(
                    name="Run lint check",
                    run="CI=true yarn eslint src/ --ext .ts,.tsx --max-warnings=0",
                )
            ],
        ),
        dict(
            id="gql_codegen",
            name="GraphQL Codegen",
            steps=[
                dict(name="Run codegen", run="CI=true yarn codegen"),
                dict(name="Diff", run="git diff"),
                dict(
                    name="Compare",
                    run="bash -c '[[ -z $(git status -s) ]] || (exit 1)'",
                ),
            ],
        ),
    ],
)

# Generate workflows.

env = Environment(loader=FileSystemLoader(SRC), trim_blocks=True, lstrip_blocks=True)

print("Writing backend workflows...")

with (WORKFLOWS / "backend.yml").open("w") as fp:
    fp.write(env.get_template("backend.yml").render(backend_data))
    fp.truncate()

print("Writing frontend workflows...")

with (WORKFLOWS / "frontend.yml").open("w") as fp:
    fp.write(env.get_template("frontend.yml").render(frontend_data))
    fp.truncate()

print("Done!")
