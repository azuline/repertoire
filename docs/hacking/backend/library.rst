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

   The library delegates transaction handling to the consumers. The calling
   function is responsible for committing any mutations.

   We do this to give more fine-grained control over transaction management to
   the handler for consistency and efficiency.

   - **Consistency:** If two mutations are coupled, they ought to be committed
     together.
   - **Efficiency:** Database commits are expensive, so allowing calling code
     to batch commit related groups of mutations is a big efficiency win. In
     the past, mutation functions did commit their changes, but indexing one
     test track then required 14 commits, taking almost a tenth of a second.
     After leaving it to the caller, which made one commit per track, the time
     per track dropped to a hundredth of a second.

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

Playlist
--------

.. automodule:: src.library.playlist
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
