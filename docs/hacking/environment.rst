.. _environment:

Development Environment
=======================

This page covers the development environment.

Backend
-------

The Python backend uses Poetry to manage its dependencies and environment.
See https://python-poetry.org/docs/#installation for instructions on installing
with Poetry.

In ``backend/``:

- Run ``poetry install`` to install the dependencies into a virtual environment.
- Run ``poetry shell`` to activate the virtual environment.

The debug backend webserver can be ran with

.. code-block:: sh

   $ cd backend/
   $ poetry shell
   $ QUART_DEBUG=1 QUART_APP="src.webserver.app:create_app()" quart run

The ``Makefile`` also contains some phony rules for commonly-used sets of
commands.

.. code-block:: sh

   $ make tests      # Run tests & lint check. Generate HTML coverage report.
   $ make typecheck  # Run mypy type checker.
   $ make lint       # Lint the backend.
   $ make docs       # (Re)generate the documentation into `docs/_build`.
   $ make schema     # (Re)generate `schema.sql`.
   $ make setupfiles # (Re)generate `setup.py` & `requirements.txt`.

.. note::

   The backend requires SQLite version 3.34.0 or newer, which many systems do
   not have. Due to this, we use ``pysqlite3`` over ``sqlite3``, which takes us
   off the system ``libsqlite3``.

   Unfortunately, developer tooling, namely the ``yoyo`` migrations CLI tool,
   uses the system version of libsqlite3. For developing the database, it is
   strongly recommended that you have SQLite3 version 3.34.0 or above installed
   on your system.

   See https://charlesleifer.com/blog/compiling-sqlite-for-use-with-python-applications/
   for upgrade / installation instructions for SQLite.

   It is for this reason that we build SQLite in our CI jobs.

Frontend
--------

The Typescript frontend uses Yarn to manage its dependencies and
environment. See https://yarnpkg.com/getting-started/install for installation
instructions.

A development server can be ran with

.. code-block:: sh

   $ cd frontend/
   $ yarn start
