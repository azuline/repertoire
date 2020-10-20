.. _backend_backend:

Backend
=======

This page contains documentation for the top-level backend boilerplate and
utility functions.

Config
------

.. automodule:: backend.config
   :members:

Enums
-----

.. This is a manual documentation of the ``ArtistRole`` enum we re-export from
   ``tagfiles``. Sphinx does not automatically document it.

.. py:class:: backend.enums.ArtistRole(value)

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

.. automodule:: backend.enums
   :members:

Errors
------

.. automodule:: backend.errors
   :members:
   :show-inheritance:
   :member-order: bysource

Tasks
-----

.. automodule:: backend.tasks
   :members:

Util
----

.. automodule:: backend.util
   :members:
   :autosummary:
