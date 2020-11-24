.. _backend_graphql:

GraphQL
=======

The GraphQL API is implemented with Ariadne.  See the `Ariadne docs
<https://ariadnegraphql.org/docs/intro>`_ for documentation on developing the
GraphQL API.

The ``backend.graphql`` package is laid out as follows:

.. code-block::

   graphql/
   ├── __init__.py          # Exports the final `schema`.
   ├── enums.py             # Contains the GraphQL enum resolvers.
   ├── mutation.py          # Contains the base `mutation` type.
   ├── query.py             # Contains the base `query` type.
   ├── scalars.py           # Contains the GraphQL scalar resolvers.
   ├── schema.graphql       # The complete and raw GraphQL schema.
   ├── util.py              # Utility functions for GraphQL resolvers.
   └── types/               # The resolvers for each GraphQL type.

.. _graphql_schema:

Schema
------

For quick reference, the raw GraphQL schema is included below:

.. literalinclude:: ../../../backend/src/graphql/schema.graphql
   :linenos:

Utility Functions
-----------------

.. automodule:: src.graphql.util
   :members:
