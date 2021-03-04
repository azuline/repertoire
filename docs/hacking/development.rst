.. _development:

Development
===========

This page covers getting set up to develop repertoire.

The development setup process is different from the production installation
process. You do not need to go through the production installation process
before starting the development setup process. Many parts of the installation
process are actually not relevant to development.

Similar to the production installation process, we provide a docker setup and a
non-docker setup. The docker option is a bit less ergonomic, but has the
benefit of a consistent environment and being easier to initially get running.
The non-docker option is more ergonomic, but has a lengthier initial setup
process, and the environment differences may cause problems.

Pick whichever is option more suitable for you.

Initial Steps
-------------

This step is common to both the docker and non-docker setups.

First, clone the repository from GitHub. If you intend to develop, it is more
convenient to set up SSH authentication and clone via SSH, with ``$ git clone
git@github.com:azuline/repertoire.git``. Cloning via HTTP with ``$ git clone
https://github.com/azuline/repertoire.git`` is still an option though.

Docker
------

The Docker setup uses Docker Compose to manage the containers. See
https://docs.docker.com/compose/install/ for installation instructions.

In the project root directory (``repertoire/``), run ``$ docker-compose up``.
This will build and start the backend and frontend in containers. The
containers are set up such that code changes in the source code directories are
reflected in the containers.

The developer frontend is accessible at ``127.0.0.1:3000``.

Running Commands
^^^^^^^^^^^^^^^^

Developer commands, such as linting code or running tests, can be executed
inside the containers.

To execute a command, we first need to figure out the container name. Run ``$
docker ps`` to list the active containers. You should see an output like so:

.. code-block::

   CONTAINER ID        IMAGE                 COMMAND                  CREATED             STATUS              PORTS                      NAMES
   40430397e5f1        repertoire_backend    "quart run --host 0.…"   16 minutes ago      Up 16 minutes       127.0.0.1:5000->5000/tcp   repertoire_backend_1
   9c7655b98dc4        repertoire_frontend   "yarn start"             36 minutes ago      Up 23 minutes       127.0.0.1:3000->3000/tcp   repertoire_frontend_1

This tells us that our container names are ``repertoire_backend_1`` and
``repertoire_frontend_1``. For the rest of this document, we will assume that
our containers have these names, but your container names may differ.

A shell command can be ran in a container using ``$ docker exec``. For example,
to run the backend tests, execute ``$ docker exec -it repertoire_backend_1 make
tests``.

A list of developer commands can be found at :ref:`development_commands`.

Non-Docker
----------

The non-docker installation method assumes you have a Linux system and a shell.
It directly uses the Poetry and Yarn package managers to install everything
directly onto your computer.

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
   ``.env`` such that ``DATA_PATH=../data``.
#. Configure the backend with ``$ repertoire config``. Set the value of the
   ``music_directories`` key to ``["../testlib"]``.
#. Generate an authentication token with ``$ repertoire token``. Remember this
   token; you will use it to log in while developing.
#. Index the test library with ``$ repertoire index``.
#. Run the debug backend webserver with
   ``$ QUART_DEBUG=1 QUART_APP="src.webserver.app:create_app()" quart run``

Or, as a set of shell commands:

.. code-block:: sh

   $ cd repertoire/backend
   $ poetry install
   $ poetry shell
   $ cp .env.sample .env
   $ nano .env             # Set `DATA_PATH=../data` on the first line.
   $ repertoire config     # Set `music_directories = ["../testlib"]`.
   $ repertoire token      # Remember this token!
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

   $ make test       # Run tests & lint check. Generate HTML coverage report.
   $ make typecheck  # Run mypy type checker.
   $ make lint       # Lint the backend.
   $ make docs       # (Re)generate the documentation into `docs/_build`.
   $ make schema     # (Re)generate `schema.sql`.
   $ make setupfiles # (Re)generate `setup.py` & `requirements.txt`.

On the frontend, developer commands are defined under the ``package.json``
``scripts`` key.

.. code-block:: sh

  $ yarn test        # Run the test suite (currently doesn't exist).
  $ yarn storybook   # Open the component storybook (currently doesn't exist).
  $ yarn lint        # Lint the frontend.
  $ yarn codegen     # Regenerate the GraphQL code from the backend schema.
  $ yarn tsc         # Run the TypeScript type checker.

Demo Music
----------

A small music library from https://freemusicarchive.org has been compiled
together to provide developers with a convenient library to use in their
development environments.

The library is available at https://u.sunsetglow.net/f/EzUAq5TsupQ.tgz.
Unarchive this tarball into the ``repertoire/testlib`` directory and run the
``$ repertoire index`` command on the backend (or, if you are on Docker, in the
backend container).

For a simple set of shell commands to set up the test library, see:

.. code-block:: sh

   $ cd repertoire/
   $ wget -O - https://u.sunsetglow.net/f/EzUAq5TsupQ.tgz | tar -xzvf -
   $ cd backend/
   $ poetry run repertoire index
