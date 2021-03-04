# repertoire

[![Backend](https://img.shields.io/github/workflow/status/azuline/repertoire/Backend?label=backend)](https://github.com/azuline/repertoire/actions?query=workflow%3ABackend)
[![Frontend](https://img.shields.io/github/workflow/status/azuline/repertoire/Frontend?label=frontend)](https://github.com/azuline/repertoire/actions?query=workflow%3AFrontend)
[![Documentation Status](https://readthedocs.org/projects/repertoire/badge/?version=latest)](https://readthedocs.org/projects/repertoire/builds)
[![Docker](https://img.shields.io/docker/cloud/build/blissful/repertoire)](https://hub.docker.com/r/blissful/repertoire)
[![Codecov](https://img.shields.io/codecov/c/github/azuline/repertoire?token=98M8XQLWLH)](https://codecov.io/gh/azuline/repertoire)

A music server for cataloguing and exploring large music libraries.

Visit [the documentation](https://repertoire.readthedocs.io) to get started!

**Unreleased WIP Edition - No Stable Upgrade Path**

**Beta Soon^TM**

## Background

This project is a sandbox project, in the sense that we are using it to
experiment with cool new ideas and technologies. Feature work is a second
priority to extracting educational value out of this codebase. This does not
mean that feature work will not occur! But expect it to be slow.

On the flip side, we treat codebase health as a top priority. We take care to
keep complexity low, to squash the systematic causes of bugs, to document the
project thoroughly, and to have a quality developer workflow.

Given the nature of this project, unexpected PRs will likely not be accepted.
If you wish to make a PR, please open an issue ticket first or comment on an
existing ticket to coordinate with maintainers.

## Security

Only the latest version is supported with security updates. No security updates
will be backported.

Report vulnerabilities to `blissful at sunsetglow.net`.

## License

```
repertoire :: a music server for cataloguing and exploring large music libraries

Copyright (C) 2021 blissful

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

### Scratchpad

Since GQL API can create release, need to have functions to scan its tracks for
cover art and/or upload art.
