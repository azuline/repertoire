# repertoire

[![CI](https://img.shields.io/github/workflow/status/azuline/repertoire/CI)](https://github.com/azuline/repertoire/actions)
[![Documentation Status](https://readthedocs.org/projects/repertoire/badge/?version=latest)](https://repertoire.readthedocs.io/en/latest/?badge=latest)
[![codecov](https://img.shields.io/codecov/c/github/azuline/repertoire?token=98M8XQLWLH)](https://codecov.io/gh/azuline/repertoire)
[![Discord](https://img.shields.io/discord/780852818835013653?color=blueviolet&label=Discord)](https://discord.gg/yaXtjgMzCe)

A release-oriented music server. Work in progress!

Visit [the documentation](https://repertoire.readthedocs.io) to get started!

## Screenshots

![example](docs/_static/scrot1.png)

![example](docs/_static/scrot2.png)

![example](docs/_static/scrot3.png)

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

## Scratchpad

We are binding TypeScript to version 4.0.3 right now because CRA is broken with
the newest version. Will unbind when it is fixed.

Since GQL API can create release, need to have functions to scan its tracks for
cover art and/or upload art.
