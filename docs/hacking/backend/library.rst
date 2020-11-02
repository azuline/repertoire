.. _backend_library:

Library
=======

The ``library`` package contains functions and dataclasses that expose a clean
and functional interface for working with the data from the database.

This package is designed functionally--each module corresponds to one data
model. A dataclass for each data model exists at ``module.T``, and each module
contains functions that fetch or operate on dataclasses.

Artist
------

.. automodule:: src.library.artist
   :members:
   :autosummary:

Collection
----------

.. automodule:: src.library.collection
   :members:
   :autosummary:

Release
-------

.. automodule:: src.library.release
   :members:
   :autosummary:

Track
-----

.. automodule:: src.library.track
   :members:
   :autosummary:

User
----

.. automodule:: src.library.user
   :members:
   :autosummary:
