.. _development:

Development
===========

This page covers getting set up to develop repertoire.

The development setup process is different from the production installation
process. You do not need to go through the production installation process
before starting the development setup process. Many parts of the installation
process are actually not relevant to development.

This page assumes you have a Linux system and shell. It uses the Poetry and
Yarn package managers to install everything directly onto your computer.

Setup
-----

First, clone the repository from GitHub. If you intend to develop, it is more
convenient to set up SSH authentication and clone via SSH, with ``$ git clone
git@github.com:azuline/repertoire.git``. Cloning via HTTP with ``$ git clone
https://github.com/azuline/repertoire.git`` is still an option though.

Before starting, please make sure you:

#. Have a recent enough version of SQLite. See :ref:`installation_sqlite`.
#. Have Python 3.9.1 and NodeJS 15.8.0 installed, either through your system
   package manager or through pyenv and nvm. See :ref:`installation_py_js`.

We split the setup into two parts: backend and frontend. 

Backend
^^^^^^^

The Python backend uses Poetry to manage its dependencies and environment.
See https://python-poetry.org/docs/#installation for instructions on installing
with Poetry.

After installing Poetry:

#. Change directory to ``repertoire/backend/``.
#. Install the backend with ``$ poetry install``.
#. Activate the Poetry virtual environment with ``$ poetry shell``.
#. Copy ``.env.sample`` to ``.env`` (``$ cp .env.sample .env``), and edit
   ``.env`` such that ``DATA_PATH=../_data``.
#. Configure the backend with ``$ repertoire config``. Set the value of the
   ``music_directories`` key to ``["../_testlib"]``.
#. Index the test library with ``$ repertoire index``.
#. Run the debug backend webserver with ``$ make debug``.

Or, as a set of shell commands:

.. code-block:: sh

   $ cd repertoire/backend
   $ poetry install
   $ poetry shell
   $ cp .env.sample .env
   $ nano .env             # Set `DATA_PATH=../_data` on the first line.
   $ repertoire config     # Set `music_directories = ["../_testlib"]`.
   $ repertoire index      # Index the test library.
   $ QUART_DEBUG=1 QUART_APP="src.webserver.app:create_app()" quart run

Frontend
^^^^^^^^

The Typescript frontend uses Yarn to manage its dependencies and
environment. See https://yarnpkg.com/getting-started/install for installation
instructions.

After installing Yarn:

- Change directory to ``repertoire/frontend``.
- Run ``$ yarn install`` to install the dependencies.
- Run ``$ yarn start`` to start the development server.

Or, as a set of shell commands:

.. code-block:: sh

   $ cd repertoire/frontend
   $ yarn install
   $ yarn start

.. _development_commands:

Development Commands
--------------------

On the backend, we use a Makefile to provide some basic developer commands.

.. code-block:: sh

   $ make debug       # Run the debug backend server.
   $ make test        # Run the tests. Generate HTML coverage report.
   $ make testseq     # Same as test, but with sequential execution. Per-test dots.
   $ make typecheck   # Run mypy type checker.
   $ make lint        # Lint the backend.
   $ make docs        # (Re)generate the documentation into `docs/_build`.
   $ make schema      # (Re)generate `schema.sql`.
   $ make setupfiles  # (Re)generate `setup.py` & `requirements.txt`.

On the frontend, developer commands are defined under the ``package.json``
``scripts`` key.

.. code-block:: sh

   $ yarn test        # Run the test suite (currently doesn't exist).
   $ yarn storybook   # Open the component storybook.
   $ yarn lint        # Lint the frontend.
   $ yarn codegen     # Regenerate the GraphQL code from the backend schema.
   $ yarn tsc         # Run the TypeScript type checker.

Demo Music
----------

A small music library from https://freemusicarchive.org has been compiled
together to provide developers with a convenient library to use in their
development environments.

The library is available at https://u.sunsetglow.net/f/EzUAq5TsupQ.tgz.
Unarchive this tarball into the ``repertoire/_testlib`` directory and run the
``$ repertoire index`` command on the backend (or, if you are on Docker, in the
backend container).

For a simple set of shell commands to set up the test library, see:

.. code-block:: sh

   $ cd repertoire/
   $ wget -O - https://u.sunsetglow.net/f/5moSen8BU_c.tgz | tar -xzvf -
   $ cd backend/
   $ poetry run repertoire index
