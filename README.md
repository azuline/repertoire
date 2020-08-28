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

1. Configure the backend (see [Configuration](##Configuration)).
2. Install Python backend in `backend/` with `pip install -e .` (to a
   virtualenv if you'd like).
3. Create the database with TODO.
4. Compile React frontend in 'frontend/' with `yarn build`.
5. Run with TODO.

## Configuration

Configuration of the backend is handled with environment variables. These are
set in the `.env` file located in the root directory of the project.

To configure the backend, copy `.env.sample` to `.env` and alter the variables
as desired. The following list describes what each variable does.

- `DATABASE_PATH` - Location to store the SQLite database.
- `COVER_ART_DIR` - Location to store cover arts of the library.
- `LOGS_DIR` - Location to write backend service logs.
- `PID_PATH` - Location to write the backend daemon PID file.
- `MUSIC_DIRS` - A colon-delimited list of directories to look for music in.
  _Warning: Does not support directories with colons in their path._

Regarding the paths to use, one can use the root directory of the project if
there is no better option (i.e. `/path/to/repertoire`).

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
