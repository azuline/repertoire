.. _installation:

Installation
============

This document assumes at least basic familiarity with the shell. At the moment,
all installation options require the shell.

There are three installation options:

- :ref:`installation_docker`
- :ref:`installation_poetry`
- :ref:`installation_virtualenv`

Choose whichever is right for you! If you do not know which option to choose, I
recommend :ref:`installation_docker`.

.. note::
   Commands that should be run in the shell are prefixed with ``$``. The ``$``
   should not be included when running the command.

   Lines beginning with a `#` are comments and should not be executed.

.. note::
   Regardless of which installation option is chosen, repertoire will run on
   port 45731. You should be able to access it via ``http://127.0.0.1:45731``.

.. _installation_docker:

Docker
------

You will need Docker and Docker Compose installed.

To install and run repertoire, reference the following commands:

.. code-block:: sh

   # Create a directory for the compose file.
   $ mkdir repertoire
   $ cd repertoire
   # Use whatever editor you want. Refer to the docker-compose.yml file
   # below; yours should look similar if not equal.
   $ nano docker-compose.yml
   # Start the webserver.
   $ docker-compose up -d
   # Generate an authentication token for the admin user. Remember it!
   # `repertoire_server_1` should be replaced with your container name.
   $ docker exec -it repertoire_server_1 repertoire token

Example ``docker-compose.yml``:

.. code-block::

   version: '3'
   services:
     server:
       image: blissful/repertoire:latest
       command: start
       ports:
         - "127.0.0.1:45731:45731"
       volumes:
         - data:/data
         - /my/music1:/music/lib1
         - /my/music2:/music/lib2
   volumes:
     data:

.. _installation_poetry:

Poetry
------

This option uses Poetry to handle the virtual environment and install the
backend. See https://python-poetry.org/docs/#installation for instructions on
installing Poetry.

Yarn is used to build the frontend. See https://classic.yarnpkg.com/en/docs/install/ for instructions on installing
Yarn.

Installation with Poetry has the following steps:

#. Clone the repository with ``$ git clone https://github.com/azuline/repertoire``.
#. Change directory to ``repertoire/backend``.
#. Install backend with ``$ poetry install --no-dev``.
#. Activate the Poetry virtual environment with ``$ poetry shell``.
#. Configure the backend with ``$ repertoire config``.
#. Compile the frontend in ``frontend/`` with ``$ yarn build``.
#. Generate an authentication token with ``$ repertoire token``.
#. Index your music library with ``$ repertoire index``.
#. Run with ``$ repertoire start``!

Or, as a set of shell commands:

.. code-block:: sh

   $ git clone https://github.com/azuline/repertoire

   $ cd repertoire/backend/
   $ poetry install --no-dev # Install the backend.
   $ poetry shell            # Activate the Poetry virtual environment.
                             # This command needs to be run in each new shell
                             # to access the `repertoire` command.
   $ cp .env.sample .env
   $ nano .env               # Set `DATA_PATH`.
   $ repertoire config       # Configure the backend.
   $ cd ../frontend/
   $ yarn build              # Build the frontend.
   $ cd ..
   $ repertoire index        # Index your music library.
   $ repertoire token        # Remember this token! It is used for authentication.
   $ repertoire start        # Start the server!

.. _installation_virtualenv:

Pip & Virtualenv
----------------

This option directly works with the Python virtual environment and uses ``pip``
to install the backend. You must have ``pip`` installed on your computer.

Yarn is used to build the frontend. See
https://classic.yarnpkg.com/en/docs/install/ for instructions on installing
Yarn.

Installation with Poetry has the following steps:

#. Clone the repository with ``$ git clone https://github.com/azuline/repertoire``.
#. Change directory to ``repertoire/backend/``.
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

   $ git clone https://github.com/azuline/repertoire

   $ cd repertoire/backend/
   $ python3 -m venv .venv     # Create the virtual environment
   $ source .venv/bin/activate # Activate the virtual environment.
                               # This command needs to be run in each new shell
                               # to access the `repertoire` command.
   $ pip install -e .          # Install the backend.
   $ cp .env.sample .env
   $ nano .env                 # Set `DATA_PATH`.
   $ repertoire config         # Configure the backend.
   $ cd ../frontend/
   $ yarn build                # Build the frontend.
   $ cd ..
   $ repertoire index          # Index your music library.
   $ repertoire token          # Remember this token! It is used for authentication.
   $ repertoire start          # Start the server!
