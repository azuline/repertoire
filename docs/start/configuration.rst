.. _configuration:

Configuration
=============

.. note::

   If you installed repertoire with Docker, most of this is taken care of
   provided that your music libraries are mounted (volumes) as subdirectories
   of ``/music``.

   The configuration can then be edited by invoking ``repertoire config`` in the
   container.

All backend configuration and data is stored in a data directory. This
directory is configured by the ``DATA_PATH`` environment variable.

Environment variables can be specified in an ``.env`` file. The ``.env`` file
should be placed at ``repertoire/backend/.env``. An example ``.env`` file is
located at ``repertoire/backend/.env.sample``.

Once ``DATA_PATH`` is set, the backend can be configured with the command
``repertoire config``. This will open the configuration file in your
``$EDITOR``.

A sample configuration file is as follows:

.. code-block:: ini

   [repertoire]
   ; A JSON-encoded list of directories to index music files from.
   music_directories = ["/path/one", "/path/two"]
   ; A crontab to schedule the indexing of the `music_directories`.
   index_crontab = 0 0 * * *

.. note::

   Comments in the real config will be stripped.

Example crontabs can be found/sourced at https://crontab.guru/examples.html.

Other Environment Variables
---------------------------

These environment variables are only necessary if you want to do something
*weird*.

- ``BUILT_FRONTEND_DIR``: The directory of the compiled frontend. This has a
  reasonable default of following the repository directory structure.
