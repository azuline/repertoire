.. _backend_database:

Database
========

We use SQLite for our database.

.. note::

   Developer tooling expects that the data directory is in ``repertoire/data``.
   The yoyo database migration tool (for developers) is configured to also look
   in that directory for the database.

Search Index
------------

We use SQLite's FTS5 virtual tables for our search index. To keep the search
index in sync with the database content, we have a set of triggers defined in
the database. These are written in and applied via the database migrations.

See https://www.sqlite.org/fts5.html for an overview of FTS5.

.. note::

   SQLite does not support stored procedures, yet the triggers that maintain
   the search index state share logic. Thus, our trigger SQL is heavily
   duplicated. Please bear with it~

Migrations
----------

Database migrations are handled with the ``yoyo-migrations`` package. We invoke
this package in the module-level scope of ``backend/src/__init__.py`` to
automatically perform any pending migrations when repertoire is run.

Migrations are stored in ``backend/src/migrations``.

.. warning::

   Commands such as ``yoyo reapply`` can cause data loss. Be very careful if
   developing on a production instance.

Schema
------

The DB schema is included below.

.. literalinclude:: ../../../backend/schema.sql
   :language: sql
   :lines: 4-
   :linenos:
