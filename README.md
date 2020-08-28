# repertoire

A release-oriented music server. Work in progress.

Stack:

- Backend: Rust (Rocket) + Python scripts
- Frontend: JavaScript (React)

## State of the Project

Goal: MVP

Frontend is fully mocked up (design may change). It lacks the backend request
logic and a few parts dependent upon that logic.

Backend currently consists of a database and Python script to populate it. The
API is currently in the process of being written.

## Installation

1. Copy `.env.sample` to `.env`.
2. Set the `DATABASE_URL` envvar in `.env`.
3. Install diesel's CLI tool.
4. Create the database with `diesel migration run`.
5. Install Python dependencies for `scripts/`.
6. Index a directory of music (or multiple) with `scripts/indexer.py`.
7. Compile React frontend in 'frontend/' with `yarn build`.
8. Compile backend with TODO.
9. Run with TODO.

## License

```
repertoire :: a release-oriented music server

Copyright (C) 2020 azuline

This program is free software: you can redistribute it and/or modify it under
the terms of the GNU Affero General Public License as published by the Free
Software Foundation, either version 3 of the License, or (at your option) any
later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY
WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A
PARTICULAR PURPOSE.  See the GNU Affero General Public License for more
details.

You should have received a copy of the GNU Affero General Public License along
with this program.  If not, see <https://www.gnu.org/licenses/>.
```
