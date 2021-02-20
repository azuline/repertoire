.. _backend:

Backend
=======

This section contains the documentation for the backend source code. This page
goes over the organization of the backend and provides a general overview.

TODO: Add testing page.

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
   ├── tests/        # The tests for the backend.
   └── webserver/    # The webserver (duh!).

The backend can be split into several layers, from lowest to highest:

- The Music Files (Music Files, Bring Your Own!)
- The Database (:ref:`backend_database`)
- The Library Indexer (:ref:`backend_indexer`)
- The Library Interface (:ref:`backend_library`)
- Consumer Interfaces:

  - The Task Queue
  - The Command Line (:ref:`backend_command_line`)
  - The Webserver (:ref:`backend_webserver`)

    - GraphQL API (:ref:`backend_graphql`)

The next several pages document each major section of the backend codebase.

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
