.. _backend_library:

Library
=======

The ``backend.lib`` package contains functions and dataclasses that expose a
clean and functional interface for working with the data from the database.

This package is designed functionally--each module corresponds to one data
model. A dataclass for each data model exists at ``module.T``, and each module
contains functions that fetch or operate on dataclasses.

Artist
------

.. automodule:: backend.lib.artist
   :members:
   :autosummary:

Collection
----------

.. automodule:: backend.lib.collection
   :members:
   :autosummary:

Play History
------------

.. automodule:: backend.lib.play_history
   :members:
   :autosummary:

Release
-------

.. automodule:: backend.lib.release
   :members:
   :autosummary:

Track
-----

.. automodule:: backend.lib.track
   :members:
   :autosummary:

User
----

.. automodule:: backend.lib.user
   :members:
   :autosummary:
