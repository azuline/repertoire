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

   $ FLASK_DEBUG=1 FLASK_APP=backend/web/app.py python -m flask run

If you are working with the database, a ``yoyo.ini`` file can be created in the
project root to simplify working with the ``yoyo`` database migration tool.

.. code-block::

   [DEFAULT]
   sources = backend/migrations
   migration_table = _yoyo_migration
   batch_mode = off
   verbosity = 0
   database = sqlite:///data/db.sqlite3

Frontend
--------

TODO.
