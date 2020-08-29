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

1. Install backend with `pip install -e .` (to a virtualenv if you'd like).
2. Configure the backend (see [Configuration](##Configuration)).
3. Compile frontend in `frontend/` with `yarn build`.

Or, as a set of shell commands,

```sh
$ pip install -e .
$ cp .env.sample .env
$ nano .env  # Set `DATA_PATH`.
$ repertoire config  # Configure the backend.
$ cd frontend
$ yarn build
$ cd ..
$ repertoire
```

## Configuration

Backend configuration and data is stored in a data directory (`DATA_PATH`). The
location of this directory is set in the `.env` file located in the root
directory of the project. The `.env.sample` file is a sample skeleton for the
`.env` file.

A good default `DATA_PATH` is `/path/to/repertoire/data`.

Once `DATA_PATH` is set, the backend can be configured with the shell command
`repertoire config`. This will open the config file in `EDITOR`.

A sample configuration file is as follows:

```ini
[repertoire]
; A JSON-encoded list of directories to index music files from.
music_directories = ["/path/one", "/path/two"]
; The interval (in hours) in between indexes of the `music_directories`.
; Supports integers between 0 and 24, inclusive.
index_interval = 1440
```

_Note: Comments in the real config will be stripped by the backend._

## Development

Run the debug backend server with

```
$ FLASK_DEBUG=1 FLASK_APP=backend/web/wsgi.py python -m flask run
```

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
