.. _backend_library:

Library
=======

The ``backend.library`` package contains functions and dataclasses that expose a
clean and functional interface for working with the data from the database.

This package is designed functionally--each module corresponds to one data
model. A dataclass for each data model exists at ``module.T``, and each module
contains functions that fetch or operate on dataclasses.

Artist
------

.. automodule:: backend.library.artist
   :members:
   :autosummary:

Collection
----------

.. automodule:: backend.library.collection
   :members:
   :autosummary:

Play History
------------

.. automodule:: backend.library.play_history
   :members:
   :autosummary:

Release
-------

.. automodule:: backend.library.release
   :members:
   :autosummary:

Track
-----

.. automodule:: backend.library.track
   :members:
   :autosummary:

User
----

.. automodule:: backend.library.user
   :members:
   :autosummary:
