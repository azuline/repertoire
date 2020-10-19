.. _backend:

Backend
=======

This section contains the documentation for the backend source code. This page
goes over the organization of the backend and provides a general overview. The
next several pages contain the source code documentation:

- :ref:`backend_backend` documents the top-level backend boilerplate code.
- :ref:`backend_command_line` documents the command line interface
  implementation.
- :ref:`backend_indexer` documents the indexer implementation.
- :ref:`backend_library` documents the internal library API.
- :ref:`backend_webserver` documents the webserver implementation.

The backend is laid out as follows:

.. code-block::

   backend/
   ├── __init__.py          # Package initialization code is run here.
   ├── __main__.py          # Command line entry point.
   ├── config.py            # Where the configuration is read and exposed.
   ├── constants.py         # Backend constants (namely filepaths and directories).
   ├── enums.py             # Where custom enums are defined.
   ├── errors.py            # Custom exception classes.
   ├── tasks.py             # Periodic tasks are scheduled here
   ├── util.py              # General utility functions.
   ├── cli/                 # The command line commands are defined here.
   ├── indexer/             # Library indexer; populates the database.
   ├── lib/                 # Library with data abstractions.
   ├── migrations/          # Database migrations.
   ├── tests/               # The tests for the backend.
   └── web/                 # The Flask webserver directory.
       ├── app.py           # Contains the Flask app factory.
       ├── routes/          # Where the REST API routes are stored.
       ├── util.py          # Web server utility functions.
       └── validators.py    # Custom validators for request data validation.

The backend can be split into several layers, from lowest to highest:

- The Filesystem (Music Files)
- The Library Indexer (:ref:`backend_indexer`)
- The Database (SQLite)
- The Library Interface (:ref:`backend_library`)
- Library Interface Consumers:

  - The Command Line (:ref:`backend_command_line`)
  - The Webserver (:ref:`backend_webserver`)

.. toctree::
   :maxdepth: 1
   :hidden:
   :caption: Backend

   backend
   command_line
   indexer
   library
   webserver