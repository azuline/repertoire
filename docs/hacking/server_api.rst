.. _server_api:

Server API
==========

The backend webserver API consists of several REST API endpoints and a GraphQL
API.

The GraphQL API is available via ``POST`` requests to the ``/graphql``
endpoint. The raw schema is documented at :ref:`graphql_schema`.

For reference, the GraphQL queries executed by the frontend are available `on
Github <https://github.com/azuline/repertoire/tree/master/frontend/src/lib>`_.

Authentication
--------------

Each user is provisioned one authorization token. To authenticate with the
backend, this token should be included with every request as the
``Authorization`` header, in the format ``Token {token_hex}``.

A token can be generated for the ``admin`` user with the shell command ``$
repertoire token``.

Sessions
^^^^^^^^

In some situations, using an authorization token to authenticate every request.
An alternative method of authentication--HTTP sessions--is available.

This method of authentication requires a CSRF token to be sent alongside all
non-GET requests. The CSRF token is returned upon session creation.

See :ref:`server_api_session` for the related API endpoints.

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

GraphQL resources are restricted to authenticated users. To be able to
query/mutate them, the ``Authorization`` HTTP header must be configured.

The playground should look something like:

.. image:: /_static/playground_auth.png

REST Endpoints
--------------

The REST endpoints of the API are as follows:

.. _server_api_session:

Sessions
^^^^^^^^

These endpoints allow clients to generate sessions as an alternative
method of authentication.

.. autoflask:: src.webserver.app:create_app()
   :modules: src.webserver.routes.session
   :groupby: view
   :order: path

File Serving
^^^^^^^^^^^^

These endpoints serve the music and image files stored on the backend.

.. autoflask:: src.webserver.app:create_app()
   :modules: src.webserver.routes.files
   :groupby: view
   :order: path
