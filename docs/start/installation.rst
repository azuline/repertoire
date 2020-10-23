.. _installation:

Installation
============

There are three installation options:

- :ref:`installation_poetry`
- :ref:`installation_virtualenv`
- :ref:`installation_docker`

Choose whichever is right for you! If you do not know which option to choose, I
recommend :ref:`installation_poetry`.

To compile the frontend, the ``yarn`` Javascript package manager is needed.

.. _installation_poetry:

Poetry
------

This option uses Poetry to handle the virtual environment and install the
backend.

See https://python-poetry.org/docs/#installation for instructions on installing
poetry.

Installation with Poetry has the following steps:

#. Change directory to ``repertoire/``.
#. Install backend with ``$ poetry install --no-dev``.
#. Activate the Poetry virtual environment with ``$ poetry shell``.
#. Configure the backend with ``$ repertoire config``.
#. Compile the frontend in ``frontend/`` with ``$ yarn build``.
#. Generate an authentication token with ``$ repertoire token``.
#. Index your music library with ``$ repertoire index``.
#. Run with ``$ repertoire start``!

Or, as a set of shell commands:

.. code-block:: sh

   $ cd repertoire/
   $ poetry install --no-dev # Install the backend.
   $ poetry shell            # Activate the Poetry virtual environment.
   $ cp .env.sample .env
   $ nano .env               # Set `DATA_PATH`.
   $ repertoire config       # Configure the backend.
   $ cd frontend/
   $ yarn build              # Build the frontend.
   $ cd ..
   $ repertoire index        # Index your music library.
   $ repertoire token        # Remember this token! It is used for authentication.
   $ repertoire start        # Start the server!

.. _installation_virtualenv:

Pip & Virtualenv
----------------

This option directly works with the Python virtual environment and uses ``pip``
to install the backend.

Installation with Poetry has the following steps:

#. Change directory to ``repertoire/``.
#. Create virtualenv with ``$ python3 -m venv .venv``.
#. Activate virtualenv with ``$ source .venv/bin/activate``.
#. Install backend with ``$ pip install -e .``.
#. Configure the backend with ``$ repertoire config``.
#. Compile the frontend in ``frontend/`` with ``$ yarn build``.
#. Generate an authentication token with ``$ repertoire token``.
#. Index your music library with ``$ repertoire index``.
#. Run with ``$ repertoire start``!

Or, as a set of shell commands:

.. code-block:: sh

   $ cd repertoire/
   $ python3 -m venv .venv     # Create the virtual environment
   $ source .venv/bin/activate # Activate the virtual environment.
   $ pip install -e .          # Install the backend.
   $ cp .env.sample .env
   $ nano .env                 # Set `DATA_PATH`.
   $ repertoire config         # Configure the backend.
   $ cd frontend/
   $ yarn build                # Build the frontend.
   $ cd ..
   $ repertoire index          # Index your music library.
   $ repertoire token          # Remember this token! It is used for authentication.
   $ repertoire start          # Start the server!

.. _installation_docker:

Docker
------

This option uses Docker to install the server inside a container. TODO.
