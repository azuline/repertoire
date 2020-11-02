.. _advanced_server_api:

Server API
==========

The backend webserver API consists of several REST-flavored API endpoints and a
GraphQL API.

The GraphQL API is available via ``POST`` requests to the ``/graphql``
endpoint. The raw schema is documented at :ref:`graphql_schema`.

Authentication
--------------

Each user is provisioned one authorization token. To authenticate with the
backend, this token should be included with every request as the
``Authorization`` header, in the format ``Token {token_hex}``.

A token can be generated for the ``admin`` user with the shell command ``$
repertoire token``.

GraphQL Playground
------------------

The "GraphQL Playground" is packaged with repertoire. It provides an
interactive playground to explore the schema documentation and write GraphQL
queries. It can be accessed by visiting the ``/graphql`` endpoint in your
browser. By default (and in production), it is disabled.

To run the "GraphQL Playground," repertoire's backend webserver must be run in
debug mode. See :ref:`hacking_environment` to set up a development environment
and run the backend webserver in debug mode.

Authentication
^^^^^^^^^^^^^^

Most GraphQL resources are restricted to authenticated users. To be able to
query/mutate them, the ``Authorization`` HTTP header must be configured.

The playground should look something like:

.. image:: playground_auth.png

REST-Flavored Endpoints
-----------------------

The REST flavored endpoints of the API are as follows:

File Serving
^^^^^^^^^^^^

These endpoints serve the music and image files stored on the backend.

.. autoflask:: src.webserver.app:create_app()
   :modules: src.webserver.routes.files
   :groupby: view
   :order: path
