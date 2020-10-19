#!/usr/bin/env python
import glob
import logging
import re
from itertools import chain
from sqlite3 import Cursor
from typing import List

import click
from tagfiles import TagFile

from backend.config import Config
from backend.enums import CollectionType, ReleaseType
from backend.errors import Duplicate
from backend.lib import artist, collection, release, track
from backend.util import calculate_sha_256, database

logger = logging.getLogger()

EXTS = [
    ".m4a",
    ".mp3",
    ".ogg",
    ".flac",
]

GENRE_DELIMITER_REGEX = re.compile(r"\\\\|\/|,|;")


def index_directories() -> None:
    """Index the music files in the configured music directories."""
    config = Config()
    tracks_indexed = 0

    for dir_ in config.music_directories:
        for _ in catalog_directory(dir_):
            tracks_indexed += 1
            yield tracks_indexed


def catalog_directory(directory: str) -> None:
    """
    Recurisvely catalog the music in a given directory.
    """
    logger.info(f"Beginning catalog of `{directory}`.")

    with database() as conn:
        cursor = conn.cursor()

        logger.info("Searching for music files...")
        files = chain(
            *[glob.glob(f"{directory}/**/*{ext}", recursive=True) for ext in EXTS]
        )

        logger.info(f"Found {len(files)} tracks to catalog.")
        click.echo(f"Found {len(files)} tracks to catalog.")

        for i, filepath in enumerate(files):
            catalog_file(TagFile(filepath), cursor)
            yield i

        click.echo("Finished cataloguing tracks.")

        fix_release_types(cursor)


def catalog_file(tf: TagFile, cursor: Cursor) -> None:
    """Catalog a file and write it to the database connection."""
    logger.debug(f"Cataloguing file `{tf.path}`.")

    # Check to see if the filepath is already indexed. If so, then skip.
    #
    # We directly query the database here as a slight optimization over the more
    # expensive `track.from_filepath`, as this is run for every file we find.
    cursor.execute("SELECT 1 FROM music__tracks WHERE filepath = ?", (str(tf.path),))
    if cursor.fetchone():
        logger.debug(f"File `{tf.path}` already in database, skipping...")
        return

    artists = [
        {"artist": fetch_or_create_artist(art, cursor), "role": role}
        for role, artists in tf.artist.items()
        for art in artists
    ]

    track.create(
        title=f"{tf.title} ({tf.version})" if tf.version else tf.title,
        filepath=tf.path,
        sha256=calculate_sha_256(tf.path),
        release=fetch_or_create_release(tf, cursor),
        artists=artists,
        duration=int(tf.mut.info.length),
        track_number=tf.track_number or "1",
        disc_number=tf.disc_number or "1",
    )


def fetch_or_create_release(tf: TagFile, cursor: Cursor) -> int:
    """Fetch or create an release in the database. Return its ID."""
    logger.debug(f"Attempting to fetch release for track `{tf.path}`...")

    if not tf.album:
        logger.debug(f"Fetched `Unknown Release` for track `{tf.path}`.")
        return 1  # Unknown release.

    # Try to create a releas with the given title and album artists. If it raises a
    # duplicate error, return the duplicate entity.
    try:
        rls = release.create(
            title=tf.album,
            artists=[fetch_or_create_artist(art, cursor) for art in tf.artist_album],
            release_type=_get_release_type(tf),
            release_year=tf.date.year or 0,
            release_date=tf.date.date or None,
        )
    except Duplicate as e:
        return e.entity

    # Flag the release to have its cover art extracted and stored.
    cursor.execute(
        "INSERT INTO music__releases_to_fetch_images (release_id) VALUES (?)",
        (rls.id,),
    )
    cursor.connection.commit()

    # Add release to the inbox and its label/genres.
    insert_into_inbox_collection(rls, cursor)
    insert_into_label_collection(rls, tf.label, cursor)
    insert_into_genre_collections(rls, tf.genre, cursor)

    return rls


def _get_release_type(tf: TagFile) -> ReleaseType:
    """Get the release type. If it doesn't exist, return UNKNOWN."""
    for type_ in ReleaseType:
        if tf.release_type and tf.release_type.lower() == type_.name.lower():
            return type_

    return ReleaseType.UNKNOWN


def fetch_or_create_artist(name: str, cursor: Cursor) -> artist.T:
    if not name:
        return artist.from_id(1, cursor)

    try:
        return artist.create(name, cursor)
    except Duplicate as e:
        return e.entity


def insert_into_inbox_collection(rls: release.T, cursor: Cursor) -> None:
    """
    Insert a release into the inbox collection.
    """
    # Inbox has ID 1--this is specified in the database schema.
    inbox = collection.from_id(1)
    inbox.add_release(rls)


def insert_into_label_collection(rls: release.T, label: str, cursor: Cursor) -> None:
    """
    Insert an release into a label collection. Create the collection if
    it doesn't already exist.
    """
    if not label:
        logger.debug(f"No label provided for release {rls.id}, skipping...")
        return

    try:
        col = collection.create(label, CollectionType.LABEL, cursor)
    except Duplicate as e:
        col = e.entity

    collection.add_release(col, rls, cursor)


def insert_into_genre_collections(rls: release.T, genre: str, cursor: Cursor) -> None:
    """
    Insert a release into its genre collections. Create the collections if
    they don't already exist.
    """
    for genre in chain(*[_split_genres(g) for g in genre]):
        try:
            col = collection.create(genre, CollectionType.GENRE, cursor)
        except Duplicate as e:
            col = e.entity

        collection.add_release(col, rls, cursor)


def _split_genres(genres: str) -> List[str]:
    """Split a string of multiple delimited genres into a list of genres."""
    return [g.strip() for g in GENRE_DELIMITER_REGEX.split(genres)]


def fix_release_types(cursor: Cursor) -> None:
    """
    Because release type is a fairly non-existent tag, for the UNKNOWN
    release types in the database, fix them.

    Guess-timate the release type by the number of tracks in the release, a-la
    Tidal (iirc, < 3 --> Single, < 6 --> EP, >= 6 --> Album). We are not
    worrying about getting the release type exactly right. It's not very
    important.

    We are running this afterwards since our other alternative is to use
    the track_total tag, which is probably not going to be accurate more than
    60% of the time for things that didn't run through beets.
    """
    logger.info("Fixing release types...")

    _, releases = release.search(release_types=[ReleaseType.UNKNOWN])

    for rls in releases:
        if rls.num_tracks < 3:
            type_ = ReleaseType.SINGLE
        elif rls.num_tracks < 6:
            type_ = ReleaseType.EP
        else:
            type_ = ReleaseType.ALBUM

        logger.info(f"Setting release type of release {rls.id} to {type_.name}.")
        release.update(rls, release_type=type_)
