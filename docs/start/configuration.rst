.. _configuration:

Configuration
=============

All backend configuration and data is stored in a data directory. This
directory is set by the ``DATA_PATH`` environment variable, which is sourced
from the ``.env`` file.

A good default value for ``DATA_PATH`` is ``/path/to/repertoire/data``.

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

*Note: Comments in the real config will be stripped.*

Example crontabs can be found/sourced at https://crontab.guru/examples.html.
