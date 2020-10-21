Environment
===========

This page covers the development environment.

Backend
-------

The Python backend uses Poetry to manage its dependencies and environment.

Run ``poetry install`` to install the dependencies into a Python environment
and ``poetry shell`` to spawn the environment.

The debug backend server can be ran with

.. code-block:: sh

   $ QUART_APP=backend.webserver.app:create_app() quart run

If you are working with the database, a ``yoyo.ini`` file can be created in the
project root to simplify working with the ``yoyo`` database migration tool.

.. code-block::

   [DEFAULT]
   sources = backend/migrations
   migration_table = _yoyo_migration
   batch_mode = off
   verbosity = 0
   database = sqlite:///data/db.sqlite3

The ``Makefile`` contains some phony rules for commonly-used sets of commands.

.. code-block:: sh

   $ make tests    # Run tests & lint check. Generate HTML coverage report.
   $ make lint     # Lint the backend.
   $ make docs     # Regenerate the documentation in `docs/_build`.
   $ make setup.py # Regenerate the `setup.py` file from the `pyproject.toml`.
   $ make build    # Build the frontend.

Frontend
--------

TODO.
