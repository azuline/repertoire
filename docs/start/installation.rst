.. _installation:

Installation
============

There are two installation options: :ref:`installation_native` and
:ref:`installation_docker`.

.. _installation_native:

Native
------

#. Install backend with ``pip install -e .`` (or to a virtualenv if you'd like).
#. Configure the backend (see :ref:`configuration`)
#. Compile the frontend in ``frontend/`` with ``yarn build``.
#. Generate an authentication token with ``repertoire token``.
#. Index your music library with ``repertoire index``.
#. Run with ``repertoire start``!

Or, as a set of shell commands:

.. code-block:: sh

   $ pip install -e .
   $ cp .env.sample .env
   $ nano .env           # Set `DATA_PATH`.
   $ repertoire config   # Configure the backend.
   $ cd frontend/
   $ yarn build          # Build the frontend.
   $ cd ..
   $ repertoire index    # Index your music library.
   $ repertoire token    # Remember this token! It is used for authentication.
   $ repertoire start    # Start the server!

.. _installation_docker:

Docker
------

TODO.
