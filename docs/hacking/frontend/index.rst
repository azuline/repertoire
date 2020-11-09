.. _frontend:

Frontend
========

This section contains the documentation for the frontend source code. This page
goes over the frontend stack and the organization of the frontend.

The frontend is written in Typescript and uses the React framework. For styles,
it uses the Tailwind utility CSS framework.

The frontend is laid out as follows:

.. code-block::

   src/
   ├── App.tsx             // The top-level App component.
   ├── assets              // Static assets (e.g. images) used in the application.
   ├── common              // Common utility functions shared amongst the codebase.
   ├── components          // Components in the application.
   │   ├── common          // "Dumb" components meant for use in other components.
   ├── constants.ts        // Application constants.
   ├── contexts            // Custom contexts and the global state context.
   ├── hooks               // Custom hooks.
   ├── index.tailwind.css  // Custom application-specific CSS to augment Tailwind.
   ├── index.tsx           // The top-level React index file.
   ├── lib                 // Contains functions for fetching data from the backend.
   ├── pages               // The "Page" components that the router routes to.
   ├── Routes.tsx          // The application router.
   └── types.ts            // Common types used throughout the application.


.. note::

   I still need to figure out the appropriate amount/type of documentation for
   a frontend. More will come when that happens. Sorry!
