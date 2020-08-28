# repertoire

A release-oriented music server. Work in progress.

Stack:

- Backend: Python (Flask)
- Frontend: JavaScript (React)

## State of the Project

Goal: MVP

Frontend is fully mocked up (design may change). It lacks the backend request
logic and a few parts dependent upon that logic.

Backend currently being written.

## Installation

1. Copy `.env.sample` to `.env` and set the variables (can leave unchanged).
2. Install Python backend with `pip install -e .` (to a virtualenv if you'd
   like).
3. Create the database with TODO.
4. Compile React frontend in 'frontend/' with `yarn build`.
5. Run with TODO.

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
