.. _backend_library:

Library
=======

The ``library`` package contains functions and dataclasses that expose a clean
and functional interface for working with the data from the database.

This package is designed functionally--each module corresponds to one data
model. A dataclass for each data model exists at ``module.T``, and each module
contains functions that fetch or operate on dataclasses.

These dataclasses are frozen (immutable). To update them, see the available
utility functions at :ref:`backend_util`.

.. note::

   The mutation functions in this library do not commit their mutations to the
   database. The caller function is responsible for committing after invoking
   these functions.

   We leave committing to the caller as it is expensive, and in cases where
   many mutations need to be made consecutively and can be considered one
   single transaction, letting the caller commit once at the end is far more
   efficient.

   In the past, mutation functions did commit their changes, but indexing one
   test track then required 14 commits, taking almost a tenth of a second.

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

Image
-----

.. automodule:: src.library.image
   :members:
   :autosummary:
