# repertoire

A release-oriented music server. Work in progress.

Stack:

- Backend: Rust (Rocket) + Python scripts
- Frontend: JavaScript (React)

## Installation

1. Set the `DATABASE_URL` envvar in `.env`.
2. Install diesel's CLI tool.
3. Create the database with `diesel migration run`.
4. Install Python dependencies for `scripts/`.
5. Index a directory of music (or multiple) with `scripts/indexer.py`.
6. Compile React frontend in 'frontend/' with TODO.
7. Compile backend with TODO.
8. Run with TODO.
