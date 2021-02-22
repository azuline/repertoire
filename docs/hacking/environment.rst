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

Frontend
--------

The Typescript frontend uses Yarn to manage its dependencies and
environment. See https://yarnpkg.com/getting-started/install for installation
instructions.

A development server can be ran with

.. code-block:: sh

   $ cd frontend/
   $ yarn start
