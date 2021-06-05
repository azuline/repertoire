.. _configuration:

Configuration
=============

.. note::

   If you installed repertoire with Docker, most configuration is taken care
   of, provided that your music libraries are mounted (volumes) as
   subdirectories of ``/music``.

The Environment
---------------

The first variable that must be configured is the ``DATA_PATH`` environment
variable. This defines where the configuration and application data data should
be stored.

We define environment variables in ``repertoire/backend/.env``. A sample
``.env`` file is located at ``repertoire/backend/.env.sample``.

Configuration Options
---------------------

TODO: GUI editing for the configuration variables. Replace these outdated docs.

Once the ``DATA_PATH`` environment variable is configured, the backend can be
configured with the command ``$ repertoire config``. This will open the
configuration file to be edited in your ``$EDITOR``.

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
