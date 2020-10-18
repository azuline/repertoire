# repertoire

[![Build Status](https://travis-ci.org/azuline/repertoire.svg?branch=master)](https://travis-ci.org/azuline/repertoire)

A release-oriented music server. Work in progress!

![example](_github/example.png)

Stack: Python (w/ Flask) and React (JS).

State: Barely usable.

## Installation

1. Install backend with `pip install -e .` (to a virtualenv if you'd like).
2. Configure the backend (see [Configuration](##Configuration)).
3. Compile frontend in `frontend/` with `yarn build`.
4. Generate an authentication token with `repertoire token`.
5. Run!

Or, as a set of shell commands,

```sh
$ pip install -e .
$ cp .env.sample .env
$ nano .env  # Set `DATA_PATH`.
$ repertoire config  # Configure the backend.
$ cd frontend
$ yarn build
$ cd ..
$ repertoire token  # Remember this token.
$ repertoire start  # Start the daemon.
```

## Command Line

```
Usage: repertoire [OPTIONS] COMMAND [ARGS]...

  A release-oriented music server.

Options:
  --help  Show this message and exit.

Commands:
  config  Edit the application config.
  index   Index the music in the music dirs.
  start   Start the backend daemon.
  status  Show the backend daemon status.
  stop    Stop the backend daemon.
  token   Generate an authentication token.
```

## Configuration

Backend configuration and data is stored in a data directory, determined by the
`DATA_PATH` environment variable. This environment variable should be set in
the `.env` file located in the project root. A good default value for
`DATA_PATH` is `/path/to/repertoire/data`.

Once `DATA_PATH` is set, the backend can be configured with the shell command
`repertoire config`. This will open the config file in your `$EDITOR`.

A sample configuration file is as follows:

```ini
[repertoire]
; A JSON-encoded list of directories to index music files from.
music_directories = ["/path/one", "/path/two"]
; The interval (in hours) in between indexes of the `music_directories`.
; Supports integers between 0 and 24, inclusive.
index_interval = 24
```

_Note: Comments in the real config will be stripped._

## Development

Run the debug backend server with

```
$ FLASK_DEBUG=1 FLASK_APP=backend/web/app.py python -m flask run
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
