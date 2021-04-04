.. _installation:

Installation
============

This document covers installing repertoire for a production environment. To
install repertoire for development, see :ref:`development`.

This document assumes at least basic familiarity with the shell. At the moment,
all installation options require the shell.

There are three installation options:

- :ref:`installation_docker`
- :ref:`installation_poetry`
- :ref:`installation_virtualenv`

Choose whichever is right for you! If you do not know which option to choose, I
recommend :ref:`installation_docker`. The other options are primarily intended
for power users.

Regardless of which installation option is chosen, repertoire will run on port
45731. You should be able to access it via ``http://127.0.0.1:45731``.

.. note::

   Commands that should be run in the shell are prefixed with ``$``. The ``$``
   should not be included when running the command.

   Lines beginning with a `#` are comments and should not be executed.

.. warning::

   repertoire comes built in with a debugging server. This server **should
   never be run in production or exposed to the internet**.

   The debug server enables functionality to arbitrarily create accounts for
   testing purposes. This compromises the security of the application.

.. _installation_docker:

Docker
------

You will need Docker and Docker Compose installed. See
https://docs.docker.com/engine/install/ and
https://docs.docker.com/compose/install/.

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

Example ``docker-compose.yml``:

.. code-block:: yaml

   version: '3'
   services:
     server:
       # This uses the latest repertoire image off the master branch.
       image: blissful/repertoire:latest
       # This binds repertoire to port 45731, listening only on 127.0.0.1.
       ports:
         - "127.0.0.1:45731:45731"
       volumes:
         - data:/data
         # You should replace the following elements with your music
         # directories. For each directory with music on your computer,
         # map it to a subdirectory of `/music` in the container. The format of
         # each line is `{directory_on_computer}:{directory_in_docker_container}`.
         - /my/music1:/music/lib1
         - /my/music2:/music/lib2
   volumes:
     data:

.. _installation_poetry:

Poetry
------

.. note::

   repertoire is only tested on specific versions of Python and JavaScript. See
   :ref:`installation_py_js` for instructions on installing the required
   versions of Python and JavaScript.

.. warning::

   The backend requires SQLite version 3.34.0 or newer. See
   :ref:`installation_sqlite` for installation instructions.

This option uses Poetry to handle the virtual environment and install the
backend. See https://python-poetry.org/docs/#installation for instructions on
installing Poetry.

Yarn is used to build the frontend. See https://classic.yarnpkg.com/en/docs/install/ 
for instructions on installing Yarn.

Installation with Poetry has the following steps:

#. Clone the repository with ``$ git clone https://github.com/azuline/repertoire``.
#. Change directory to ``repertoire/backend``.
#. Install backend with ``$ poetry install --no-dev``.
#. Activate the Poetry virtual environment with ``$ poetry shell``.
#. Configure the backend by first copying ``.env.sample`` to ``.env``
   (``$ cp .env.sample .env``) and then editing it (``$ nano .env``). See
   :ref:`configuration` for information regarding the configuration options.
#. Configure the backend with ``$ repertoire config``.
#. Compile the frontend in ``frontend/`` with ``$ yarn build``.
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
   $ yarn install            # Install frontend dependencies.
   $ yarn build              # Build the frontend.
   $ cd ..
   $ repertoire index        # Index your music library.
   $ repertoire start        # Start the server!

.. _installation_virtualenv:

Pip & Virtualenv
----------------

.. note::

   repertoire is only tested on specific versions of Python and JavaScript. See
   :ref:`installation_py_js` for instructions on installing the required
   versions of Python and JavaScript.

.. warning::

   The backend requires SQLite version 3.34.0 or newer. See
   :ref:`installation_sqlite` for installation instructions.

This option directly works with the Python virtual environment and uses ``pip``
to install the backend. You must have ``pip`` installed on your computer.

Yarn is used to build the frontend. See
https://classic.yarnpkg.com/en/docs/install/ for instructions on installing
Yarn.

Installation with Pip & Virtualenv has the following steps:

#. Clone the repository with ``$ git clone https://github.com/azuline/repertoire``.
#. Change directory to ``repertoire/backend/``.
#. Create virtualenv with ``$ python3 -m venv .venv``.
#. Activate virtualenv with ``$ source .venv/bin/activate``.
#. Configure the backend by first copying ``.env.sample`` to ``.env``
   (``$ cp .env.sample .env``) and then editing it (``$ nano .env``). See
   :ref:`configuration` for information regarding the configuration options.
#. Install backend with ``$ pip install -e .``.
#. Configure the backend with ``$ repertoire config``.
#. Compile the frontend in ``frontend/`` with ``$ yarn build``.
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
   $ yarn install              # Install frontend dependencies.
   $ yarn build                # Build the frontend.
   $ cd ..
   $ repertoire index          # Index your music library.
   $ repertoire start          # Start the server!

.. _installation_py_js:

Installing Python & JavaScript
------------------------------

repertoire pins to specific versions of Python and JavaScript to ensure
consistency between development and production environments.

To install the required versions of Python and JavaScript, we recommend using
pyenv and nvm.

Python
^^^^^^

#. Follow the instructions at https://github.com/pyenv/pyenv#installation to
   install pyenv.
#. Run ``$ pyenv install 3.9.1`` to install the required Python version.

JavaScript
^^^^^^^^^^

#. Follow the instructions at https://github.com/nvm-sh/nvm#installing-and-updating
   to install nvm.
#. Run ``$ nvm install 15.8.0`` to install the required JavaScript version.
#. **In the frontend directory** (``repertoire/frontend/``) run ``$ nvm use``.

.. _installation_sqlite:

Installing a Newer SQLite
--------------------------

The backend requires SQLite version 3.34.0 or newer for its trigram tokenizer
extension, which many systems do not have. If your system does not have SQLite
3.34.0 or newer, you will need to upgrade or switch to Docker. The Docker
container comes with a working version of SQLite.

See https://charlesleifer.com/blog/compiling-sqlite-for-use-with-python-applications/
for upgrade / installation instructions. In addition to these instructions, if
your system already has a version of SQLite installed, you may need to run
``export LD_LIBRARY_PATH=/usr/local/lib`` to get Python to use the newly
installed version of SQLite.
