.. _backend_library:

Library
=======

The ``backend.lib`` package contains functions and dataclasses that expose a
clean and functional interface for working with the data from the database.

This package is designed functionally--each module corresponds to one data
model. A dataclass for each data model exists at ``module.T``, and each module
contains functions that fetch or operate on dataclasses.

User
----

.. automodule:: backend.lib.user
   :members:

Release
-------

.. automodule:: backend.lib.release
   :members:

Track
-----

.. automodule:: backend.lib.track
   :members:

Artist
------

.. automodule:: backend.lib.artist
   :members:

Collection
----------

.. automodule:: backend.lib.collection
   :members:

Play History
------------

.. automodule:: backend.lib.play_history
   :members:
