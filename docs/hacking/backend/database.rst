.. _backend_database:

Database
========

We use SQLite for our database.

Migrations
----------

Database migrations are handled with the ``yoyo-migrations`` package. We invoke
this package in the module-level scope of ``backend/src/__init__.py`` to
automatically perform any pending migrations when repertoire is run.

Migrations are stored in ``backend/src/migrations``.

See https://ollycope.com/software/yoyo/latest/ for documentation on the
using ``yoyo`` for development. The following ``yoyo.ini`` file can be created
in the ``backend/`` directory to configure the ``yoyo`` command.

.. code-block:: ini

   [DEFAULT]
   sources = src/migrations
   migration_table = _yoyo_migration
   batch_mode = off
   verbosity = 0
   database = sqlite:///../data/db.sqlite3

.. warning::

   Commands such as ``yoyo reapply`` can cause data loss. Be very careful if
   developing on a production instance.

Schema
------

.. literalinclude:: ../../../backend/schema.sql
   :language: sql
   :lines: 4-
   :linenos:
