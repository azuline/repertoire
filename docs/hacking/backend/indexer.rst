.. _backend_indexer:

Indexer
=======

The indexer is responsible for indexing the music library on the filesystem and
populating the database with the available metadata and information.

The indexer runs in three stages:

#. **Index music directories** - Scan the filesystem for new music files, store
   them in the database.
#. **Build search index** - After indexing all new music files, build a search
   index with the new metadata.
#. **Extract album art** - Extract and store the album art from the music
   library. Generate thumbnails for the frontend.
