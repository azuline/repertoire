#!/usr/bin/env python

import glob
import itertools
import logging
import re
import sqlite3
from hashlib import sha256
from typing import Iterable, List

import click
from tagfiles import TagFile

from backend.config import Config
from backend.enums import CollectionType, ReleaseType
from backend.util import database

logger = logging.getLogger()

EXTS = [
    ".m4a",
    ".mp3",
    ".ogg",
    ".flac",
]

GENRE_DELIMITER_REGEX = re.compile(r"\\\\|\/|,|;")


def index_directories() -> None:
    """Catalog all the music in the configured library directories."""
    config = Config()
    for dir_ in config.music_directories:
        catalog_directory(dir_)


def catalog_directory(audio_path: str) -> None:
    """Catalog the music in a directory."""
    logger.info(f"Beginning catalog of `{audio_path}`.")
    click.echo(f"Beginning catalog of `{audio_path}`.")
    with database() as conn:
        files = []
        for ext in EXTS:
            logger.info(f"Searching for files of extension {ext}...")
            files.extend(glob.glob(f"{audio_path}/**/*{ext}", recursive=True))

        logger.info(f"Found {len(files)} tracks to catalog.")
        click.echo(f"Found {len(files)} tracks to catalog.")

        for i, filepath in enumerate(files):
            if i % 25 == 0:
                click.echo(f"Cataloguing track {i}...\r", nl=False)
            catalog_file(conn, TagFile(filepath))

        click.echo("Finished cataloguing tracks.")

        fix_release_types(conn)


def catalog_file(conn: sqlite3.Connection, tf: TagFile) -> None:
    """Catalog a file and write it to the database connection."""
    logger.debug(f"Cataloguing file `{tf.path}`.")

    cursor = conn.cursor()

    # Check to see if file is already in database.
    cursor.execute(
        """
        SELECT 1 FROM music__tracks WHERE filepath = ?
        """,
        (tf.path,),
    )
    if cursor.fetchone():
        logger.debug(f"File `{tf.path}` already in database, skipping...")
        return

    title = f"{tf.title} ({tf.version})" if tf.version else tf.title
    filepath = tf.path
    sha256 = calculate_sha_256(tf.path)
    track_number = tf.track_number or 1
    disc_number = tf.disc_number or 1
    duration = int(tf.mut.info.length)

    logger.info(
        f"Found new track `{tf.path}` with title `{title}` and hash "
        f"`{sha256.hex()}`, inserting into database..."
    )

    release_id = fetch_or_create_release(tf, cursor)

    cursor.execute(
        """
        INSERT INTO music__tracks
        (title, filepath, sha256, release_id, track_number, disc_number, duration)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """,
        (title, filepath, sha256, release_id, track_number, disc_number, duration),
    )
    conn.commit()
    track_id = cursor.lastrowid

    logger.info(f"Track `{tf.path}` inserted with ID {track_id}.")

    # Handle track-specific artists.
    logger.info(f"Inserting artists for track `{tf.path}`...")
    for role, artists in tf.artist.items():
        for artist in artists:
            artist_id = fetch_or_create_artist(artist, cursor)
            cursor.execute(
                """
                INSERT INTO music__tracks_artists
                (track_id, artist_id, role)
                VALUES (?, ?, ?)
                """,
                (track_id, artist_id, role.value),
            )
            conn.commit()
            logger.info(
                f"Added artist {artist_id} to track {track_id} with role {role.name}."
            )

    cursor.close()


def fetch_or_create_release(tf: TagFile, cursor: sqlite3.Cursor) -> int:
    """Fetch or create an release in the database. Return its ID."""
    if not tf.album:
        logger.debug(f"Fetched `Unknown Release` for track `{tf.path}`.")
        return 1  # Unknown release.

    logger.debug(f"Attempting to fetch release for track `{tf.path}`...")

    # Check to see if the release already exists.
    # First compare the title; if we have a match, then proceed to
    # compare the album artists.
    cursor.execute(
        """
        SELECT id FROM music__releases WHERE title = ?
        """,
        (tf.album,),
    )
    rows = cursor.fetchall()
    logger.debug(
        f"Found {len(rows)} existing release(s) matching the album "
        f"name of track `{tf.path}`, comparing artists for a full match..."
    )
    for row in rows:
        release_id = row["id"]
        cursor.execute(
            """
            SELECT name
            FROM music__artists AS arts
            INNER JOIN music__releases_artists AS relarts
                ON relarts.artist_id = arts.id
            WHERE relarts.release_id = ?
            """,
            (release_id,),
        )
        stored_album_artists = {row["name"] for row in cursor.fetchall()}

        logger.debug(
            f"Comparing `{stored_album_artists}` from stored release "
            f"{release_id} with `{tf.artist_album}` from the track."
        )
        if contains_same_artists(stored_album_artists, tf.artist_album):
            logger.debug(f"Fetched release {release_id} for track `{tf.path}`.")
            return release_id

        logger.debug(
            f"Release {release_id} did not match album artists with "
            f"`{tf.path}`, not a match..."
        )

    title = tf.album
    release_type = get_release_type(tf)
    release_year = tf.date.year or 0
    release_date = tf.date.date or None
    album_artists = tf.artist_album

    logger.info(
        f"Failed to fetch release for track `{tf.path}`, creating with title "
        f"`{title}` from year {release_year}."
    )

    cursor.execute(
        """
        INSERT INTO music__releases
        (title, release_type, release_year, release_date)
        VALUES (?, ?, ?, ?)
        """,
        (title, release_type.value, release_year, release_date),
    )
    cursor.connection.commit()
    release_id = cursor.lastrowid

    logger.info(f"Release `{title}` inserted with ID {release_id}.")

    # Mark release as pending for album art checking.
    cursor.execute(
        """
        INSERT INTO music__releases_to_fetch_images (release_id) VALUES (?)
        """,
        (release_id,),
    )
    cursor.connection.commit()

    logger.info(f"Inserting {len(album_artists)} artist(s) for release {release_id}.")
    for artist in album_artists:
        artist_id = fetch_or_create_artist(artist, cursor)
        cursor.execute(
            """
            INSERT INTO music__releases_artists
            (release_id, artist_id)
            VALUES (?, ?)
            """,
            (release_id, artist_id),
        )
        cursor.connection.commit()
        logger.info(f"Added artist {artist_id} to release {release_id}.")

    insert_into_inbox_collection(release_id, cursor)
    insert_into_label_collection(release_id, tf.label, cursor)

    genres = list(itertools.chain.from_iterable([split_genres(g) for g in tf.genre]))
    insert_into_genre_collections(release_id, genres, cursor)

    return release_id


def contains_same_artists(one: Iterable, two: Iterable) -> bool:
    """See if the two iterables contain the same case-insensitive strings."""
    return {s.lower() for s in one} == {s.lower() for s in two}


def fetch_or_create_artist(artist: str, cursor: sqlite3.Cursor) -> int:
    """Fetch or create an artist in the database. Return its ID."""
    if not artist:
        logger.debug("Fetched unknown artist!")
        return 1  # Unknown artist!

    cursor.execute(
        """
        SELECT id FROM music__artists WHERE name = ?
        """,
        (artist,),
    )
    row = cursor.fetchone()

    # Return artist id if it was fetched.
    if row:
        logger.debug(f"Fetched artist {row['id']} for artist `{artist}`.")
        return row["id"]

    logger.info(f"Failed to fetch artist `{artist}`, creating artist...")

    # Otherwise, create artist.
    cursor.execute(
        """
        INSERT INTO music__artists (name) VALUES (?)
        """,
        (artist,),
    )
    cursor.connection.commit()
    artist_id = cursor.lastrowid
    logger.info(f"Artist `{artist}` inserted with ID {artist_id}.")
    return artist_id


def get_release_type(tf: TagFile) -> ReleaseType:
    """Get the release type. If it doesn't exist, return UNKNOWN."""
    for type_ in ReleaseType:
        if tf.release_type and tf.release_type.lower() == type_.name.lower():
            return type_
    return ReleaseType.UNKNOWN


def insert_into_inbox_collection(release_id: int, cursor: sqlite3.Cursor) -> None:
    """
    Insert a release into the inbox collection.
    """
    cursor.execute(
        """
        INSERT INTO music__collections_releases (release_id, collection_id)
        VALUES (?, ?)
        """,
        (release_id, 1),
    )
    cursor.connection.commit()


def insert_into_label_collection(
    release_id: int, label: str, cursor: sqlite3.Cursor
) -> None:
    """
    Insert an release into a label collection. Create the collection if
    it doesn't already exist.
    """
    if not label:
        logger.debug(f"No label provided for release {release_id}, skipping...")
        return

    cursor.execute(
        """
        SELECT id FROM music__collections
        WHERE name = ? AND type = ?
        """,
        (label, CollectionType.LABEL.value),
    )
    row = cursor.fetchone()

    if row:  # Use collection ID if it was fetched.
        logger.debug(f"Fetched label collection {row['id']} for label `{label}`.")
        collection_id = row["id"]
    else:  # Otherwise, create collection and insert release into it.
        logger.info(f"Failed to fetch label collection for `{label}`, creating...")
        cursor.execute(
            """
            INSERT INTO music__collections (name, type) VALUES (?, ?)
            """,
            (label, CollectionType.LABEL.value),
        )
        cursor.connection.commit()
        collection_id = cursor.lastrowid
        logger.info(f"Label collection `{label}` inserted with ID {collection_id}.")

    cursor.execute(
        """
        INSERT INTO music__collections_releases
        (release_id, collection_id)
        VALUES (?, ?)
        """,
        (release_id, collection_id),
    )
    cursor.connection.commit()
    logger.info(
        f"Release {release_id} inserted into label collection `{collection_id}`."
    )


def split_genres(genres: str) -> List[str]:
    """Split a string of multiple delimited genres into a list of genres."""
    return [g.strip() for g in GENRE_DELIMITER_REGEX.split(genres)]


def insert_into_genre_collections(
    release_id: int, genres: List[str], cursor: sqlite3.Cursor
) -> None:
    """
    Insert a release into its genre collections. Create the collections if
    they don't already exist.
    """
    for genre in genres:
        cursor.execute(
            """
            SELECT id FROM music__collections
            WHERE name = ? AND type = ?
            """,
            (genre, CollectionType.GENRE.value),
        )
        row = cursor.fetchone()

        if row:  # Use collection ID if it was fetched.
            logger.debug(f"Fetched genre collection {row['id']} for genre `{genre}`.")
            collection_id = row["id"]
        else:  # Otherwise, create collection.
            logger.info(f"Failed to fetch genre collection for `{genre}`, creating...")
            cursor.execute(
                """
                INSERT INTO music__collections (name, type) VALUES (?, ?)
                """,
                (genre, CollectionType.GENRE.value),
            )
            cursor.connection.commit()
            collection_id = cursor.lastrowid
            logger.info(f"Genre collection `{genre}` inserted with ID {collection_id}.")

        cursor.execute(
            """
            INSERT INTO music__collections_releases
            (release_id, collection_id)
            VALUES (?, ?)
            """,
            (release_id, collection_id),
        )
        cursor.connection.commit()
        logger.info(
            f"Release {release_id} inserted into genre collection `{collection_id}`."
        )


def calculate_sha_256(filepath: str) -> bytes:
    """Calculate the SHA256 of a file."""
    hash_ = sha256()
    with open(filepath, "rb") as fp:
        for block in iter(lambda: fp.read(65536), b""):
            hash_.update(block)

    return hash_.digest()


def fix_release_types(conn: sqlite3.Connection) -> None:
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
    cursor = conn.cursor()

    # Normally, we would use a left join for this type of query, but We can use
    # the more efficient inner join here because we don't have releases w/out
    # tracks.
    cursor.execute(
        """
        SELECT
            rels.id AS release_id,
            COUNT(trks.id) AS track_count
        FROM music__releases AS rels
            INNER JOIN music__tracks as trks ON trks.release_id = rels.id
        WHERE rels.release_type = ?
        GROUP BY rels.id
        """,
        (ReleaseType.UNKNOWN.value,),
    )

    rows = cursor.fetchall()
    for row in rows:
        release_id = row["release_id"]
        track_count = row["track_count"]

        if track_count < 3:
            type_ = ReleaseType.SINGLE
        elif track_count < 6:
            type_ = ReleaseType.EP
        else:
            type_ = ReleaseType.ALBUM

        logger.info(f"Setting release type of release {release_id} to {type_.name}.")
        cursor.execute(
            """
            UPDATE music__releases SET release_type = ? WHERE id = ?
            """,
            (type_.value, release_id),
        )
        conn.commit()

    cursor.close()
