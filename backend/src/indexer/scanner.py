#!/usr/bin/env python
import glob
import logging
import re
from datetime import date
from itertools import chain
from sqlite3 import Connection
from typing import Optional

from tagfiles import TagFile

from src.config import config
from src.enums import ArtistRole, CollectionType, ReleaseType
from src.errors import Duplicate
from src.library import artist, collection, release, track
from src.tasks import huey
from src.util import calculate_initial_sha_256, database, uniq_list

# TODO: TagFile type is incorrect--fix the entire library...

logger = logging.getLogger()

EXTS = [
    ".m4a",
    ".mp3",
    ".ogg",
    ".flac",
]

GENRE_DELIMITER_REGEX = re.compile(r"\\\\|\/|,|;")

MAIN_ROLES = [
    ArtistRole.MAIN,
    ArtistRole.PRODUCER,
    ArtistRole.COMPOSER,
    ArtistRole.CONDUCTOR,
    ArtistRole.DJMIXER,
]


def scan_directories() -> None:
    """
    Read the music directories to be indexed from the configuration and scan them for
    new files.
    """
    music_directories = config.music_directories
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
        track_batch: list[track.T] = []

        for ext in EXTS:
            for filepath in glob.iglob(f"{directory}/**/*{ext}", recursive=True):
                # Every 50 tracks, run some specialized logic.
                if len(track_batch) == 50:
                    handle_track_batch(track_batch, conn)
                    track_batch = []

                if not _in_database(filepath, conn):
                    logger.debug(f"Discovered new file `{filepath}`.")
                    trk = catalog_file(filepath, conn)
                    track_batch.append(trk)
                else:
                    logger.debug(f"File `{filepath}` already in database, skipping...")

        # Handle the last batch of tracks.
        handle_track_batch(track_batch, conn)

        conn.commit()


def handle_track_batch(track_batch: list[track.T], conn: Connection) -> None:
    """
    Every time we have a batch of tracks, run some logic. This is logic that has a
    cost--we don't want to run it once every track, but not to the point where we want
    to only run it once.
    """
    logger.debug("Running the 50 track batch handler.")

    # Autofix potential deficiencies in the track tags.
    _fix_album_artists(conn)
    _fix_release_types(conn)

    # Commit our new tracks and changes to the DB.
    conn.commit()

    # Schedule a task to calculate the full sha256s.
    track_ids = [t.id for t in track_batch]
    calculate_track_sha256s.schedule(args=(track_ids,), delay=0)


@huey.task()
def calculate_track_sha256s(track_ids: list[int]) -> None:
    """
    Calculate a list of track's full SHA256s.
    """
    with database() as conn:
        for id_ in track_ids:
            trk = track.from_id(id_, conn)
            if not trk or trk.sha256_full:
                continue

            track.calculate_track_full_sha256(trk, conn)

        conn.commit()


def _in_database(filepath: str, conn: Connection) -> bool:
    """
    Return whether a given filepath is associated with a track in the database.

    :param filepath: The filepath to check.
    :param conn: A connection to the database.
    :return: Whether a track already is associated with this filepath.
    """
    # Rather than use `track.from_filepath`, we directly query the database for
    # efficiency, as this function is called for every track.
    cursor = conn.execute("SELECT 1 FROM music__tracks WHERE filepath = ?", (filepath,))
    return bool(cursor.fetchone())


def catalog_file(filepath: str, conn: Connection) -> track.T:
    """
    Given a file, enter its information into the database. If associated database
    objects, e.g. artists and albums, don't exist, they are created with information
    from the track.

    If a track with this file's sha256 already exists in the database, the filepath of
    the existing database row will be updated to the new filepath. No metadata updating
    will happen.

    :param filepath: The filepath of the music file.
    :param conn: A connection to the database.
    """
    tf = TagFile(filepath)

    title = f"{tf.title} ({tf.version})" if tf.version else tf.title or "Untitled"

    rls = _fetch_or_create_release(tf, conn)

    artists = [
        {"artist_id": _fetch_or_create_artist(art, conn).id, "role": role}
        for role, artists in tf.artist.items()
        # The track tags might contain duplicate artists...
        for art in uniq_list(artists)
    ]

    trk = track.create(
        title=title,
        filepath=tf.path,
        sha256_initial=calculate_initial_sha_256(tf.path),
        release_id=rls.id,
        artists=artists,
        duration=int(tf.mut.info.length),
        track_number=tf.track_number or "1",
        disc_number=tf.disc_number or "1",
        conn=conn,
    )

    return trk


def _fetch_or_create_release(tf: TagFile, conn: Connection) -> release.T:
    """
    Try to match the album and album artist fields of the tagfile against the database.
    If a matching release is found, return it. Otherwise, create and return a new
    release. If the track has no album, return the Unknown Release (ID: 1).

    If a new release is created, add it to the inbox collection and relevant label/genre
    collections. We also flag the release for cover art extraction in the future (not as
    scary as it sounds!).

    :param tf: The track whose release we want to fetch.
    :param conn: A connection to the database.
    :return: The release the track belongs to.
    """
    if not tf.album:
        logger.debug(f"Fetched `Unknown Release` for track `{tf.path}`.")
        rls = release.from_id(1, conn)
        assert rls is not None
        return rls

    release_date: Optional[date] = None

    try:
        release_date = date.fromisoformat(tf.date.date)
    except (TypeError, ValueError):
        pass

    # Try to create a release with the given title and album artists. If it raises a
    # duplicate error, return the duplicate entity.
    try:
        rls = release.create(
            title=tf.album,
            # The tags might contain duplicate artists..
            artist_ids=uniq_list(
                _fetch_or_create_artist(art, conn).id for art in tf.artist_album
            ),
            release_type=_get_release_type(tf),
            release_year=tf.date.year,
            release_date=release_date,
            conn=conn,
            allow_duplicate=False,
        )
    except Duplicate as e:
        logger.debug(f"Return existing release {e.entity.id} for track `{tf.path}`.")
        return e.entity

    logger.debug(f"Created new release {rls.id} for track `{tf.path}`.")

    # Add release to the inbox and its label/genres.
    _insert_into_inbox_collections(rls, conn)
    _insert_into_label_collection(rls, tf.label, conn)
    _insert_into_genre_collections(rls, tf.genre, conn)

    # Flag the release to have its cover art extracted and stored.
    conn.execute(
        "INSERT INTO music__releases_images_to_fetch (release_id) VALUES (?)",
        (rls.id,),
    )

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


def _fetch_or_create_artist(name: str, conn: Connection) -> artist.T:
    """
    Try to fetch an artist from the database with the given name. If one doesn't exist,
    create it. If ``name`` is empty or ``None``, return the Unknown Artist (ID: 1).

    :param name: The name of the artist.
    :param conn: A connection to the database.
    :return: The fetched/created artist.
    """
    if not name:
        art = artist.from_id(1, conn)
        assert art is not None
        return art

    try:
        return artist.create(name, conn)
    except Duplicate as e:
        return e.entity


def _insert_into_inbox_collections(rls: release.T, conn: Connection) -> None:
    """
    Insert a release into all inbox collections.

    :param rls: The release to add to the inbox collection.
    :param conn: A connection to the database.
    """
    logger.debug(f"Adding release {rls.id} to inbox collections.")
    inboxes = collection.from_name_and_type(
        name="Inbox",
        type=CollectionType.SYSTEM,
        conn=conn,
    )
    for inbox in inboxes:
        collection.add_release(inbox, rls.id, conn)


def _insert_into_label_collection(
    rls: release.T, label: Optional[str], conn: Connection
) -> None:
    """
    Insert an release into a label collection. Create the collection if
    it doesn't already exist.

    :param rls: The release to add to the label collection.
    :param label: The label to add the release to.
    :param conn: A connection to the database.
    """
    if not label:
        logger.debug(f"No label provided for release {rls.id}, skipping...")
        return

    try:
        col = collection.create(label, CollectionType.LABEL, conn)
    except Duplicate as e:
        col = e.entity

    collection.add_release(col, rls.id, conn)


def _insert_into_genre_collections(
    rls: release.T, genres: list[str], conn: Connection
) -> None:
    """
    Split each genre in the ``genres`` parameter on the defined genre delimiters. Insert
    the provided release into the corresponding collection for each split genre. Create
    any genre collections that don't exist.

    :param rls: The release to add to the genre collections.
    :param genres: The genre tags from the track.
    :param conn: A connection to the database.
    """
    for genre in uniq_list(chain(*[_split_genres(g) for g in genres])):
        if not genre:
            continue

        try:
            col = collection.create(genre, CollectionType.GENRE, conn)
        except Duplicate as e:
            col = e.entity

        col = collection.add_release(col, rls.id, conn)


def _split_genres(genres: str) -> list[str]:
    """
    Split a string of multiple delimited genres into a list of genres.

    :param genres: An unsplit genre tag.
    :return: A list of split genre strings.
    """
    return [g.strip() for g in GENRE_DELIMITER_REGEX.split(genres)]


def _fix_album_artists(conn: Connection) -> None:
    """
    Because not all albums contain the album artist tag, we look at all releases with no
    album artists and either assign them their track artists or assign them to the
    Unknown Artist.

    If the album's tracks have artists, then we conditionally assign the album artist
    based off the track's artists. See the code for the specific logic.

    :param conn: A connection to the database.
    """
    logger.info("Fixing album artists...")

    cursor = conn.execute(
        """
        SELECT rls.id
        FROM music__releases AS rls
        WHERE NOT EXISTS(
            SELECT 1 FROM music__releases_artists WHERE release_id = rls.id
        )
        """
    )
    release_ids = [row[0] for row in cursor]

    for rid in release_ids:
        rls = release.from_id(rid, conn)
        assert rls is not None

        tracks = release.tracks(rls, conn)
        amaps = chain.from_iterable(track.artists(trk, conn) for trk in tracks)
        artists = {amap["artist"] for amap in amaps if amap["role"] in MAIN_ROLES}

        for art in artists:
            release.add_artist(rls, art.id, conn)


def _fix_release_types(conn: Connection) -> None:
    """
    Because release type is a fairly non-existent tag, for the UNKNOWN release types in
    the database, fix them.

    Guess-timate the release type by the number of tracks in the release, a-la Tidal
    (iirc, < 3 --> Single, < 6 --> EP, >= 6 --> Album). We are not worrying about
    getting the release type exactly right. It's not very important.

    We run function this after scanning a full directory, since we don't have
    information on the number of tracks in a release when creating the release (track
    total tag is sometimes inaccurate or missing).

    :param conn: A connection to the database.
    """
    logger.info("Fixing release types...")

    releases = release.search(conn, release_types=[ReleaseType.UNKNOWN])

    for rls in releases:
        if rls.num_tracks < 3:
            type_ = ReleaseType.SINGLE
        elif rls.num_tracks < 6:
            type_ = ReleaseType.EP
        else:
            type_ = ReleaseType.ALBUM

        release.update(rls, conn, release_type=type_)
