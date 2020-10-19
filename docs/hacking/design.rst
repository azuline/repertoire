.. _hacking_design:

Design
======

This page covers some design decisions.

Data Model
----------

Although the data model is fairly standard, there is one interesting thing to
note about the data model: all collections of releases (e.g. inbox, favorites,
collages, labels, genres, ratings) have been grouped together in the
``collections`` table.
