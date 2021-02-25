.. _environment:

Development Environment
=======================

This page covers the development environment.

A Docker setup is provided for development, although developing with Docker is
also supported.

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

Some other Makefile rules for the backend are:

.. code-block:: sh

   $ make tests      # Run tests & lint check. Generate HTML coverage report.
   $ make typecheck  # Run mypy type checker.
   $ make lint       # Lint the backend.
   $ make docs       # (Re)generate the documentation into `docs/_build`.
   $ make schema     # (Re)generate `schema.sql`.
   $ make setupfiles # (Re)generate `setup.py` & `requirements.txt`.

Commands on the frontend can be run analogously, for example, ``$ docker exec
-it repertoire_frontend_1 yarn tsc`` to typecheck the code.

No Docker
---------

Setup without Docker assumes you have a Linux system and a shell. It directly
uses the package managers and installs everything directly onto your computer.

Backend
^^^^^^^

The Python backend uses Poetry to manage its dependencies and environment.
See https://python-poetry.org/docs/#installation for instructions on installing
with Poetry.

In ``backend/``:

- Run ``poetry install`` to install (developer) dependencies into a virtual
  environment.
- Run ``poetry shell`` to activate the virtual environment.

The debug backend webserver can be ran with

.. code-block:: sh

   $ cd backend/
   $ poetry shell
   $ QUART_DEBUG=1 QUART_APP="src.webserver.app:create_app()" quart run

The backend contains some Makefile rules:

.. code-block:: sh

   $ make tests      # Run tests & lint check. Generate HTML coverage report.
   $ make typecheck  # Run mypy type checker.
   $ make lint       # Lint the backend.
   $ make docs       # (Re)generate the documentation into `docs/_build`.
   $ make schema     # (Re)generate `schema.sql`.
   $ make setupfiles # (Re)generate `setup.py` & `requirements.txt`.

Frontend
^^^^^^^^

The Typescript frontend uses Yarn to manage its dependencies and
environment. See https://yarnpkg.com/getting-started/install for installation
instructions.

In ``frontend/``:

- Run ``$ yarn install`` to install the (developer) dependencies.

A development server can be ran with

.. code-block:: sh

   $ cd frontend/
   $ yarn start
