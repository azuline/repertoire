.. _backend:

Backend
=======

This section contains the documentation for the backend source code. This page
goes over the organization of the backend and provides a general overview.

.. TODO: Add testing page.
   TODO: Make a note of logging practices. Debug logging should provide an
   informative idea of what the backend is doing. Info logging should log all
   important events (e.g. writes & mutations).

The backend is laid out as follows:

.. code-block::

   src/
   ├── __init__.py   # Package initialization code is run here.
   ├── __main__.py   # Command line entry point.
   ├── config.py     # Where the configuration is read and exposed.
   ├── constants.py  # Backend constants (namely filepaths and directories).
   ├── enums.py      # Where custom enums are defined.
   ├── errors.py     # Custom exception classes.
   ├── services.py   # Contains functions to start each backend service.
   ├── tasks.py      # Periodic tasks are scheduled here
   ├── util.py       # General utility functions.
   ├── cli/          # The command line commands are defined here.
   ├── indexer/      # Library indexer; populates the database.
   ├── graphql/      # GraphQL API; contains the schema definition.
   ├── library/      # Library with data abstractions.
   ├── migrations/   # Database migrations.
   └── webserver/    # The webserver (duh!).
   tests/            # The tests for the backend.

The architecture of the backend is as follows:

.. image:: /_static/backend-architecture.png

The next several pages document the major ideas of the backend.

.. note::

   We do not use namespace packages (packages without an ``__init__.py``)
   because Mypy does not autodetect them.

.. toctree::
   :maxdepth: 1
   :hidden:
   :caption: Backend

   top_level
   command_line
   database
   graphql
   indexer
   library
   webserver
   testing
