Environment
===========

This page covers the development environment.

Backend
-------

The Python backend uses Poetry to manage its dependencies and environment.
See https://python-poetry.org/docs/#installation for installation instructions.

Run ``poetry install`` to install the dependencies into a Python environment
and ``poetry shell`` to spawn the environment.

The debug backend webserver can be ran with

.. code-block:: sh

   $ QUART_DEBUG=1 QUART_APP="backend.webserver.app:create_app()" quart run

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
