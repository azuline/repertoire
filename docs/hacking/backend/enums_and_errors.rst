.. _backend_enums_and_errors:

Enums & Errors
==============

This page documents the enums and errors of the backend. These values are
consistent across all program instances.

Enums
-----

.. This is a manual documentation of the ``ArtistRole`` enum we re-export from
   ``tagfiles``. Sphinx does not automatically document it.

.. py:class:: src.enums.ArtistRole(value)

   The possible artist roles.

   .. py:attribute:: MAIN
      :value: 1

   .. py:attribute:: FEATURE
      :value: 2

   .. py:attribute:: REMIXER
      :value: 3

   .. py:attribute:: PRODUCER
      :value: 4

   .. py:attribute:: COMPOSER
      :value: 5

   .. py:attribute:: CONDUCTOR
      :value: 6

   .. py:attribute:: DJMIXER
      :value: 7

.. automodule:: src.enums
   :members:
   :member-order: bysource

Errors
------

.. automodule:: src.errors
   :members:
   :show-inheritance:
   :member-order: bysource
