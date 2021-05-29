#!/usr/bin/env python3

from pathlib import Path

from jinja2 import Environment, FileSystemLoader

SRC = Path(__file__).absolute().parent
WORKFLOWS = SRC.parent / "workflows"

# Define data

backend_data = {
    "Test": """
      - name: Run tests
        run: poetry run pytest -n auto --cov-report=xml --cov=. --cov-branch src/
      - name: Upload coverage
        run: bash <(curl -s https://codecov.io/bash) -cF python
        """,
    "Type check": """
      - name: Cache mypy cache
        id: cache-mypy
        uses: actions/cache@v2
        with:
          path: backend/.mypy_cache
          key: "${{ runner.os }}-mypy-${{ github.sha }}"
          restore-keys: "${{ runner.os }}-mypy-"
      - name: Run type check
        run: make typecheck
        """,
    "Lint check": """
      - name: Run lint check
        run: make lintcheck
        """,
    "Schema": """
      - name: Generate schema
        run: make schema
      - name: Diff
        run: git diff
      - name: Status
        run: git status
      - name: Compare
        run: bash -c '[[ -z $(git status -s) ]] || (exit 1)'
        """,
    "Setup files": """
      - name: Generate setup files
        run: make setupfiles
      - name: Diff
        run: git diff
      - name: Status
        run: git status
      - name: Compare
        run: bash -c '[[ -z $(git status -s) ]] || (exit 1)'
         """,
}

frontend_data = {
    "Test": """
      - name: Run tests
        run: yarn jest --coverage
      - name: Upload coverage
        run: bash <(curl -s https://codecov.io/bash) -cF typescript
        """,
    "Type check": """
      - name: Run type check
        run: yarn tsc
        """,
    "Lint check": """
      - name: Run lint check
        run: yarn eslint src/ --ext .ts,.tsx --max-warnings=0
        """,
    "GraphQL Codegen": """
      - name: Run codegen
        run: yarn codegen
      - name: Diff
        run: git diff
      - name: Status
        run: git status
      - name: Compare
        run: bash -c '[[ -z $(git status -s) ]] || (exit 1)'
        """,
    "Chromatic": """
      - name: Upload storybook
        uses: chromaui/action@v1
        with:
          projectToken: ${{ secrets.CHROMATIC_PROJECT_TOKEN }}
    """,
}


def convert_data(data):
    return dict(
        jobs=[
            {
                "id": key.lower().replace(" ", "_"),
                "name": key,
                "steps": value.strip(),
                # A little hack.
                "fetch_all": key == "Chromatic",
            }
            for key, value in data.items()
        ]
    )


# Generate workflows.

env = Environment(loader=FileSystemLoader(SRC), trim_blocks=True, lstrip_blocks=True)

print("Writing backend workflows...")

with (WORKFLOWS / "backend.yml").open("w") as fp:
    fp.write(env.get_template("backend.yml").render(convert_data(backend_data)))
    fp.truncate()

print("Writing frontend workflows...")

with (WORKFLOWS / "frontend.yml").open("w") as fp:
    fp.write(env.get_template("frontend.yml").render(convert_data(frontend_data)))
    fp.truncate()

print("Done!")
