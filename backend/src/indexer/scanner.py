#!/usr/bin/env python
import glob
import logging
import re
from itertools import chain
from sqlite3 import Cursor
from typing import List, Optional

from tagfiles import TagFile

from src.config import Config
from src.enums import CollectionType, ReleaseType
from src.errors import Duplicate
from src.library import artist, collection, release, track
from src.util import calculate_sha_256, database

logger = logging.getLogger()

EXTS = [
    ".m4a",
    ".mp3",
    ".ogg",
    ".flac",
]

GENRE_DELIMITER_REGEX = re.compile(r"\\\\|\/|,|;")


def scan_directories() -> None:
    """
    Read the music directories to be indexed from the configuration and scan them for new
    files.
    """
    music_directories = Config().music_directories
    logger.info(f"Found {len(music_directories)} directories to scan.")

    for dir_ in music_directories:
        scan_directory(dir_)


def scan_directory(directory: str) -> None:
    """
    Scan a given directory for music files and catalog the discovered files.

    :param directory: The directory to scan.
    """
    logger.info(f"Scanning `{directory}`.")

    with database() as conn:
        cursor = conn.cursor()

        for ext in EXTS:
            for filepath in glob.iglob(f"{directory}/**/*{ext}", recursive=True):
                if not _in_database(filepath, cursor):
                    logger.info(f"Discovered new file `{filepath}`.")
                    catalog_file(filepath, cursor)
                else:
                    logger.debug(f"File `{filepath}` already in database, skipping...")

        fix_release_types(cursor)


def _in_database(filepath: str, cursor: Cursor) -> bool:
    """
    Return whether a given filepath is associated with a track in the database.

    :param filepath: The filepath to check.
    :param cursor: A cursor to the database.
    :return: Whether a track already is associated with this filepath.
    """
    # Rather than use `track.from_filepath`, we directly query the database for
    # efficiency, as this function is called for every track.
    cursor.execute("SELECT 1 FROM music__tracks WHERE filepath = ?", (filepath,))
    return bool(cursor.fetchone())


def catalog_file(filepath: str, cursor: Cursor) -> None:
    """
    Given a file, enter its information into the database. If associated database
    objects, e.g. artists and albums, don't exist, they are created with information from
    the track.

    If a track with this file's sha256 already exists in the database, the filepath of
    the existing database row will be updated to the new filepath. No metadata updating
    will happen.

    :param filepath: The filepath of the music file.
    :param cursor: A cursor to the database.
    """
    tf = TagFile(filepath)

    rls = fetch_or_create_release(tf, cursor)
    artists = [
        {"artist_id": fetch_or_create_artist(art, cursor).id, "role": role}
        for role, artists in tf.artist.items()
        for art in artists
    ]

    track.create(
        title=f"{tf.title} ({tf.version})" if tf.version else tf.title,
        filepath=tf.path,
        sha256=calculate_sha_256(tf.path),
        release_id=rls.id,
        artists=artists,
        duration=int(tf.mut.info.length),
        track_number=tf.track_number or "1",
        disc_number=tf.disc_number or "1",
        cursor=cursor,
    )


def fetch_or_create_release(tf: TagFile, cursor: Cursor) -> release.T:
    """
    Try to match the album and album artist fields of the tagfile against the database.
    If a matching release is found, return it. Otherwise, create and return a new
    release. If the track has no album, return the Unknown Release (ID: 1).

    If a new release is created, add it to the inbox collection and relevant label/genre
    collections. We also flag the release for cover art extraction in the future (not as
    scary as it sounds!).

    :param tf: The track whose release we want to fetch.
    :param cursor: A cursor to the database.
    :return: The release the track belongs to.
    """
    if not tf.album:
        logger.debug(f"Fetched `Unknown Release` for track `{tf.path}`.")
        return release.from_id(1, cursor)

    # Try to create a release with the given title and album artists. If it raises a
    # duplicate error, return the duplicate entity.
    try:
        rls = release.create(
            title=tf.album,
            artist_ids=[
                fetch_or_create_artist(art, cursor).id for art in tf.artist_album
            ],
            release_type=_get_release_type(tf),
            release_year=tf.date.year or 0,
            release_date=tf.date.date or None,
            cursor=cursor,
            allow_duplicate=False,
        )
    except Duplicate as e:
        logger.debug(f"Return existing release {e.entity.id} for track `{tf.path}`.")
        return e.entity

    logger.debug(f"Created new release {rls.id} for track `{tf.path}`.")

    # Add release to the inbox and its label/genres.
    insert_into_inbox_collection(rls, cursor)
    insert_into_label_collection(rls, tf.label, cursor)
    insert_into_genre_collections(rls, tf.genre, cursor)

    # Flag the release to have its cover art extracted and stored.
    cursor.execute(
        "INSERT INTO music__releases_to_fetch_images (release_id) VALUES (?)",
        (rls.id,),
    )
    cursor.connection.commit()

    return rls


def _get_release_type(tf: TagFile) -> ReleaseType:
    """
    Get the release type of a tagfile. If it doesn't exist, return the UNKNOWN release
    type.

    :param tf: The tagfile whose release type we want to fetch.
    :return: The determined release type.
    """
    if not tf.release_type:
        return ReleaseType.UNKNOWN

    for rtype in ReleaseType:
        if tf.release_type.lower() == rtype.name.lower():
            return rtype

    return ReleaseType.UNKNOWN


def fetch_or_create_artist(name: str, cursor: Cursor) -> artist.T:
    """
    Try to fetch an artist from the database with the given name. If one doesn't exist,
    create it. If ``name`` is empty or ``None``, return the Unknown Artist (ID: 1).

    :param name: The name of the artist.
    :param cursor: A cursor to the database.
    :return: The fetched/created artist.
    """
    if not name:
        return artist.from_id(1, cursor)

    try:
        return artist.create(name, cursor)
    except Duplicate as e:
        return e.entity


def insert_into_inbox_collection(rls: release.T, cursor: Cursor) -> None:
    """
    Insert a release into the inbox collection.

    :param rls: The release to add to the inbox collection.
    :param cursor: A cursor to the database.
    """
    logger.debug(f"Adding release {rls.id} to the inbox collection.")
    # Inbox has ID 1--this is specified in the database schema.
    inbox = collection.from_id(1, cursor)
    collection.add_release(inbox, rls.id, cursor)


def insert_into_label_collection(
    rls: release.T, label: Optional[str], cursor: Cursor
) -> None:
    """
    Insert an release into a label collection. Create the collection if
    it doesn't already exist.

    :param rls: The release to add to the label collection.
    :param label: The label to add the release to.
    :param cursor: A cursor to the database.
    """
    if not label:
        logger.debug(f"No label provided for release {rls.id}, skipping...")
        return

    try:
        col = collection.create(label, CollectionType.LABEL, cursor)
    except Duplicate as e:
        col = e.entity

    collection.add_release(col, rls.id, cursor)


def insert_into_genre_collections(
    rls: release.T, genres: List[str], cursor: Cursor
) -> None:
    """
    Split each genre in the ``genres`` parameter on the defined genre delimiters. Insert
    the provided release into the corresponding collection for each split genre. Create
    any genre collections that don't exist.

    :param rls: The release to add to the genre collections.
    :param genres: The genre tags from the track.
    :param cursor: A cursor to the database.
    """
    for genre in chain(*[_split_genres(g) for g in genres]):
        if not genre:
            continue

        try:
            col = collection.create(genre, CollectionType.GENRE, cursor)
        except Duplicate as e:
            col = e.entity

        collection.add_release(col, rls.id, cursor)


def _split_genres(genres: str) -> List[str]:
    """
    Split a string of multiple delimited genres into a list of genres.

    :param genres: An unsplit genre tag.
    :return: A list of split genre strings.
    """
    return [g.strip() for g in GENRE_DELIMITER_REGEX.split(genres)]


def fix_release_types(cursor: Cursor) -> None:
    """
    Because release type is a fairly non-existent tag, for the UNKNOWN release types in
    the database, fix them.

    Guess-timate the release type by the number of tracks in the release, a-la Tidal
    (iirc, < 3 --> Single, < 6 --> EP, >= 6 --> Album). We are not worrying about getting
    the release type exactly right. It's not very important.

    We run function this after scanning a full directory, since we don't have information
    on the number of tracks in a release when creating the release (track total tag is
    sometimes inaccurate or missing).
    """
    logger.info("Fixing release types...")

    _, releases = release.search(cursor, release_types=[ReleaseType.UNKNOWN])

    for rls in releases:
        if rls.num_tracks < 3:
            type_ = ReleaseType.SINGLE
        elif rls.num_tracks < 6:
            type_ = ReleaseType.EP
        else:
            type_ = ReleaseType.ALBUM

        logger.info(f"Setting release type of release {rls.id} to {type_.name}.")
        release.update(rls, cursor, release_type=type_)
