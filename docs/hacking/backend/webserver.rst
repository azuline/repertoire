.. _backend_webserver:

Webserver
=========

Our webserver is implemented with ``Quart``, an ASGI Flask-like web framework.
We use ``voluptuous`` for data validation.

See:

- https://pgjones.gitlab.io/quart/index.html
- https://github.com/alecthomas/voluptuous

The package is laid out as follows:

.. code-block::

    webserver/
    ├── app.py          # Contains the app factory.
    ├── util.py         # Utility functions for Quart routes.
    ├── validators.py   # Custom voluptuous validators.
    └── routes/         # The routes registered on the server.

The endpoints are documented at :ref:`server_api`.

Utility Functions
-----------------

.. automodule:: src.webserver.util
   :members:
   :autosummary:

Custom Validators
-----------------

.. automodule:: src.webserver.validators
   :members:
   :autosummary:
