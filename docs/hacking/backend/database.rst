.. _backend_database:

Database
========

We use SQLite as our database.

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

.. code-block:: sql

   CREATE TABLE music__releases (
       id INTEGER NOT NULL,
       title VARCHAR NOT NULL,
       release_type INTEGER NOT NULL DEFAULT 1,
       release_year INTEGER NOT NULL DEFAULT 0,
       release_date DATE,
       image_path VARCHAR,
       added_on TIMESTAMP DEFAULT (CURRENT_TIMESTAMP) NOT NULL,
       PRIMARY KEY (id),
       FOREIGN KEY (release_type) REFERENCES music__release_types(id)
   );

   CREATE TABLE music__release_types (
       id INTEGER NOT NULL,
       type VARCHAR NOT NULL,
       PRIMARY KEY (id),
       UNIQUE (type)
   );

   CREATE TABLE music__artists (
       id INTEGER NOT NULL,
       name VARCHAR COLLATE "NOCASE" NOT NULL,
       favorite BOOLEAN NOT NULL DEFAULT 0 CHECK (favorite IN (0, 1)),
       PRIMARY KEY (id),
       UNIQUE (name) -- We will have this constraint for now...
   );

   CREATE TABLE music__artist_roles (
       id INTEGER NOT NULL,
       role VARCHAR NOT NULL,
       PRIMARY KEY (id),
       UNIQUE (role)
   );

   CREATE TABLE music__releases_artists (
       release_id INTEGER NOT NULL,
       artist_id INTEGER NOT NULL,
       PRIMARY KEY (release_id, artist_id),
       FOREIGN KEY (release_id) REFERENCES music__releases (id),
       FOREIGN KEY (artist_id) REFERENCES music__artists (id)
   );

   CREATE TABLE music__tracks (
       id INTEGER NOT NULL,
       filepath VARCHAR NOT NULL,
       sha256 BLOB NOT NULL,
       title VARCHAR NOT NULL DEFAULT "Untitled",
       release_id INTEGER NOT NULL DEFAULT 1,
       track_number VARCHAR NOT NULL DEFAULT 1,
       disc_number VARCHAR NOT NULL DEFAULT 1,
       duration INTEGER NOT NULL,
       PRIMARY KEY (id),
       FOREIGN KEY (release_id) REFERENCES music__releases (id),
       UNIQUE (filepath)
   );

   CREATE TABLE music__tracks_artists (
       track_id INTEGER NOT NULL,
       artist_id INTEGER NOT NULL,
       role INTEGER NOT NULL,
       PRIMARY KEY (track_id, artist_id, role),
       FOREIGN KEY (track_id) REFERENCES music__tracks (id),
       FOREIGN KEY (artist_id) REFERENCES music__artists (id),
       FOREIGN KEY (role) REFERENCES music__artist_roles (id)
   );

   CREATE TABLE music__collections (
       id INTEGER NOT NULL,
       name VARCHAR COLLATE "NOCASE" NOT NULL,
       -- Ghetto SQLite boolean!
       favorite BOOLEAN NOT NULL DEFAULT 0 CHECK (favorite IN (0, 1)),
       type INTEGER NOT NULL,
       PRIMARY KEY (id),
       UNIQUE (name, type),
       FOREIGN KEY (type) REFERENCES music__collection_types(id)
   );

   CREATE TABLE music__collection_types (
       id INTEGER NOT NULL,
       type VARCHAR NOT NULL,
       PRIMARY KEY (id),
       UNIQUE (type)
   );

   CREATE TABLE music__collections_releases (
       collection_id INTEGER NOT NULL,
       release_id INTEGER NOT NULL,
       added_on TIMESTAMP DEFAULT (CURRENT_TIMESTAMP) NOT NULL,
       PRIMARY KEY (release_id, collection_id),
       FOREIGN KEY (release_id) REFERENCES music__releases(id) ON DELETE CASCADE,
       FOREIGN KEY (collection_id) REFERENCES music__collections(id) ON DELETE CASCADE
   );

   CREATE TABLE music__releases_search_index (
       id INTEGER NOT NULL,
       release_id INTEGER NOT NULL,
       word VARCHAR COLLATE "NOCASE" NOT NULL,
       PRIMARY KEY (id),
       FOREIGN KEY (release_id) REFERENCES music__releases(id) ON DELETE CASCADE
   );

   CREATE TABLE music__releases_to_fetch_images (
       release_id INTEGER NOT NULL,
       PRIMARY KEY (release_id),
       FOREIGN KEY (release_id) REFERENCES music__releases(id) ON DELETE CASCADE
   );

   CREATE TABLE music__play_history (
       id INTEGER NOT NULL,
       time TIMESTAMP DEFAULT (CURRENT_TIMESTAMP) NOT NULL,
       track_id INTEGER NOT NULL,
       PRIMARY KEY (id),
       FOREIGN KEY (track_id) REFERENCES music__tracks(id) ON DELETE SET NULL
   );

   CREATE TABLE system__users (
       id INTEGER NOT NULL,
       username VARCHAR NOT NULL,
       token_prefix BLOB NOT NULL,
       token_hash VARCHAR NOT NULL,
       PRIMARY KEY (id),
       UNIQUE (username),
       UNIQUE (token_prefix)
   );
