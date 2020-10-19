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

.. automodsumm:: backend.lib.artist
   :functions-only:
   :nosignatures:

.. automodule:: backend.lib.artist
   :members:

Collection
----------

.. automodsumm:: backend.lib.collection
   :functions-only:
   :nosignatures:

.. automodule:: backend.lib.collection
   :members:

Play History
------------

.. automodsumm:: backend.lib.play_history
   :functions-only:
   :nosignatures:

.. automodule:: backend.lib.play_history
   :members:

Release
-------

.. automodsumm:: backend.lib.release
   :functions-only:
   :nosignatures:

.. automodule:: backend.lib.release
   :members:

Track
-----

.. automodsumm:: backend.lib.track
   :functions-only:
   :nosignatures:

.. automodule:: backend.lib.track
   :members:

User
----

.. automodsumm:: backend.lib.user
   :functions-only:
   :nosignatures:

.. automodule:: backend.lib.user
   :members:
