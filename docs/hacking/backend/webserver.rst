.. _backend_webserver:

Webserver
=========

Our webserver is implemented with ``Quart``, an ASGI Flask-like web framework.

The package is laid out as follows:

.. code-block::

    webserver/
    ├── app.py          # Contains the app factory.
    ├── util.py         # Utility functions for Quart routes.
    ├── validators.py   # Custom voluptuous validators.
    └── routes/         # The routes registered on the server.
        ├── files.py    # Contains the endpoints that return music/image files.
        └── graphql.py  # Contains the GraphQL endpoints.

Utility Functions
-----------------

.. automodule:: backend.webserver.util
   :members:
   :autosummary:

Custom Validators
-----------------

.. automodule:: backend.webserver.validators
   :members:
   :autosummary:

GraphQL
-------

The GraphQL API is implemented with ``ariadne``.

The ``backend.graphql`` package is laid out as follows:

.. code-block::

   graphql/
   ├── __init__.py          # Exports the final `schema`.
   ├── enums.py             # Contains the GraphQL enum resolvers.
   ├── query.py             # Contains the base `query` type.
   ├── scalars.py           # Contains the GraphQL scalar resolvers.
   ├── schema.graphql       # The complete and raw GraphQL schema.
   └── types/               # The resolvers for each GraphQL type.
