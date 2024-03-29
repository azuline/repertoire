-- This file is for documentation purposes only.
-- It is autogenerated from the migrations, please do NOT edit!

CREATE TABLE music__releases (
    id INTEGER PRIMARY KEY,
    title VARCHAR COLLATE 'NOCASE' NOT NULL,
    release_type INTEGER NOT NULL REFERENCES music__release_types__enum(id) DEFAULT 1,
    release_year INTEGER,
    release_date DATE,
    image_id INTEGER REFERENCES images(id),
    added_on TIMESTAMP DEFAULT (CURRENT_TIMESTAMP) NOT NULL,
    rating INTEGER CHECK (rating >= 1 AND rating <=10)
);

CREATE INDEX music__releases__title__idx ON music__releases (title);

CREATE INDEX music__releases__release_type__idx ON music__releases (release_type);

CREATE INDEX music__releases__added_on__idx ON music__releases (added_on);

CREATE INDEX music__releases__release_year__idx ON music__releases (release_year);

CREATE INDEX music__releases__rating__idx ON music__releases (rating);

CREATE TABLE music__release_types__enum (
    id INTEGER PRIMARY KEY,
    type VARCHAR UNIQUE NOT NULL
);

CREATE TABLE music__artists (
    id INTEGER PRIMARY KEY,
    name VARCHAR COLLATE 'NOCASE' NOT NULL
);

CREATE TABLE music__artists_starred (
    user_id INTEGER REFERENCES system__users(id) ON DELETE CASCADE,
    artist_id INTEGER REFERENCES music__artists(id) ON DELETE CASCADE,
    PRIMARY KEY (user_id, artist_id)
);

CREATE TABLE music__artist_roles__enum (
    id INTEGER PRIMARY KEY,
    role VARCHAR UNIQUE NOT NULL
);

CREATE TABLE music__releases_artists (
    release_id INTEGER REFERENCES music__releases(id) ON DELETE CASCADE,
    artist_id INTEGER REFERENCES music__artists(id) ON DELETE CASCADE,
    role INTEGER REFERENCES music__artist_roles__enum (id),
    PRIMARY KEY (release_id, artist_id, role)
);

CREATE TABLE music__tracks (
    id INTEGER PRIMARY KEY,
    filepath VARCHAR UNIQUE NOT NULL,
    -- The SHA256 of the full track. This is initially NULL for efficiency, but
    -- eventually becomes NOT NULL.
    sha256 BLOB UNIQUE,
    -- The SHA256 of the first 1KB of the track.
    sha256_initial BLOB NOT NULL,
    title VARCHAR COLLATE 'NOCASE' NOT NULL DEFAULT 'Untitled',
    release_id INTEGER NOT NULL REFERENCES music__releases(id) DEFAULT 1,
    track_number VARCHAR NOT NULL DEFAULT '1',
    disc_number VARCHAR NOT NULL DEFAULT '1',
    duration INTEGER NOT NULL
);

CREATE INDEX music__tracks__disc_track_numbers__idx
    ON music__tracks (disc_number, track_number);

CREATE TABLE music__tracks_artists (
    track_id INTEGER REFERENCES music__tracks (id) ON DELETE CASCADE,
    artist_id INTEGER REFERENCES music__artists (id) ON DELETE CASCADE,
    role INTEGER REFERENCES music__artist_roles__enum (id),
    PRIMARY KEY (track_id, artist_id, role)
);

CREATE TABLE music__collections (
    id INTEGER PRIMARY KEY,
    name VARCHAR COLLATE 'NOCASE' NOT NULL,
    type INTEGER NOT NULL REFERENCES music__collection_types__enum(id),
    user_id INTEGER REFERENCES system__users(id) ON DELETE CASCADE,
    last_updated_on TIMESTAMP DEFAULT (CURRENT_TIMESTAMP) NOT NULL,
    UNIQUE (name, type, user_id),
    -- Assert that all System & Personal collections have a user ID attached.
    CHECK (type NOT IN (1, 2) OR user_id IS NOT NULL)
);

CREATE INDEX music__collections__sorting__idx
    ON music__collections (type, name);

CREATE TABLE music__collections_starred (
    user_id INTEGER REFERENCES system__users(id) ON DELETE CASCADE,
    collection_id INTEGER REFERENCES music__collections(id) ON DELETE CASCADE,
    PRIMARY KEY (user_id, collection_id)
);

CREATE TABLE music__collection_types__enum (
    id INTEGER PRIMARY KEY,
    type VARCHAR UNIQUE NOT NULL
);

CREATE TABLE music__collections_releases (
    collection_id INTEGER REFERENCES music__collections(id) ON DELETE CASCADE,
    release_id INTEGER REFERENCES music__releases(id) ON DELETE CASCADE,
    added_on TIMESTAMP NOT NULL DEFAULT (CURRENT_TIMESTAMP),
    PRIMARY KEY (release_id, collection_id)
);

CREATE TABLE music__playlists (
    id INTEGER PRIMARY KEY,
    name VARCHAR COLLATE 'NOCASE' NOT NULL,
    type INTEGER NOT NULL REFERENCES music__playlist_types__enum(id),
    user_id INTEGER REFERENCES system__users(id) ON DELETE CASCADE,
    last_updated_on TIMESTAMP DEFAULT (CURRENT_TIMESTAMP) NOT NULL,
    UNIQUE (name, type, user_id),
    -- Assert that all System & Personal playlists have a user ID attached.
    CHECK (type NOT IN (1, 2) OR user_id IS NOT NULL)
);

CREATE INDEX music__playlists__sorting__idx
    ON music__playlists (type, name);

CREATE TABLE music__playlists_starred (
    user_id INTEGER REFERENCES system__users(id) ON DELETE CASCADE,
    playlist_id INTEGER REFERENCES music__playlists(id) ON DELETE CASCADE,
    PRIMARY KEY (user_id, playlist_id)
);

CREATE TABLE music__playlist_types__enum (
    id INTEGER PRIMARY KEY,
    type VARCHAR UNIQUE NOT NULL
);

CREATE TABLE music__playlists_tracks (
    id INTEGER PRIMARY KEY,
    playlist_id INTEGER NOT NULL REFERENCES music__playlists(id) ON DELETE CASCADE,
    track_id INTEGER NOT NULL REFERENCES music__tracks(id) ON DELETE CASCADE,
    added_on TIMESTAMP DEFAULT (CURRENT_TIMESTAMP) NOT NULL,
    position INTEGER NOT NULL
);

CREATE INDEX music__playlists_tracks__playlist_position__idx
    ON music__playlists_tracks (playlist_id, position);

CREATE TABLE images (
    id INTEGER PRIMARY KEY,
    path VARCHAR UNIQUE NOT NULL
);

CREATE TABLE music__releases_images_to_fetch (
    release_id INTEGER PRIMARY KEY REFERENCES music__releases(id) ON DELETE CASCADE
);

CREATE TABLE system__users (
    id INTEGER PRIMARY KEY,
    nickname VARCHAR NOT NULL,
    token_prefix BLOB UNIQUE NOT NULL,
    token_hash VARCHAR NOT NULL,
    csrf_token BLOB NOT NULL
);

CREATE TABLE system__invites (
    id INTEGER PRIMARY KEY,
    code BLOB UNIQUE NOT NULL,
    created_by INTEGER NOT NULL,
    created_at TIMESTAMP DEFAULT (CURRENT_TIMESTAMP) NOT NULL,
    used_by INTEGER REFERENCES system__users(id)
);

CREATE TABLE system__secret_key (
    key BLOB PRIMARY KEY
);

CREATE TABLE system__config (
    key VARCHAR PRIMARY KEY,
    value VARCHAR
);

CREATE VIEW music__releases__fts_content AS
    SELECT
        rls.id AS id,
        rls.title AS title,
        GROUP_CONCAT(arts.name, " ") AS artists
    FROM music__releases AS rls
    LEFT JOIN music__releases_artists AS rlsarts ON rlsarts.release_id = rls.id
    LEFT JOIN music__artists AS arts ON arts.id = rlsarts.artist_id
    GROUP BY rls.id
/* music__releases__fts_content(id,title,artists) */;

CREATE VIRTUAL TABLE music__releases__fts USING fts5(
    title,
    artists,
    content='music__releases__fts_content',
    content_rowid='id',
    tokenize='trigram'
)
/* music__releases__fts(title,artists) */;

CREATE TABLE IF NOT EXISTS 'music__releases__fts_data'(id INTEGER PRIMARY KEY, block BLOB);

CREATE TABLE IF NOT EXISTS 'music__releases__fts_idx'(segid, term, pgno, PRIMARY KEY(segid, term)) WITHOUT ROWID;

CREATE TABLE IF NOT EXISTS 'music__releases__fts_docsize'(id INTEGER PRIMARY KEY, sz BLOB);

CREATE TABLE IF NOT EXISTS 'music__releases__fts_config'(k PRIMARY KEY, v) WITHOUT ROWID;

CREATE TRIGGER music__releases__fts__release_insert
    AFTER INSERT ON music__releases
    FOR EACH ROW
    BEGIN
        INSERT INTO music__releases__fts (rowid, title, artists)
        SELECT id, title, artists FROM music__releases__fts_content WHERE id = new.id;
    END;

CREATE TRIGGER music__releases__fts__release_delete
    BEFORE DELETE ON music__releases
    FOR EACH ROW
    BEGIN
        INSERT INTO music__releases__fts (music__releases__fts, rowid, title, artists)
        SELECT 'delete', rowid, title, artists FROM music__releases__fts WHERE rowid = old.id;
    END;

CREATE TRIGGER music__releases__fts__release_update_pre
    BEFORE UPDATE ON music__releases
    FOR EACH ROW
    BEGIN
        INSERT INTO music__releases__fts (music__releases__fts, rowid, title, artists)
        SELECT 'delete', rowid, title, artists FROM music__releases__fts WHERE rowid = old.id;
    END;

CREATE TRIGGER music__releases__fts__release_update_post
    AFTER UPDATE ON music__releases
    FOR EACH ROW
    BEGIN
        INSERT INTO music__releases__fts (rowid, title, artists)
        SELECT id, title, artists FROM music__releases__fts_content WHERE id = new.id;
    END;

CREATE TRIGGER music__releases__fts__artist_insert_pre
    BEFORE INSERT ON music__releases_artists
    FOR EACH ROW
    BEGIN
        INSERT INTO music__releases__fts (music__releases__fts, rowid, title, artists)
        SELECT 'delete', rowid, title, artists FROM music__releases__fts WHERE rowid = new.release_id;
    END;

CREATE TRIGGER music__releases__fts__artist_insert_post
    AFTER INSERT ON music__releases_artists
    FOR EACH ROW
    BEGIN
        INSERT INTO music__releases__fts (rowid, title, artists)
        SELECT id, title, artists FROM music__releases__fts_content WHERE id = new.release_id;
    END;

CREATE TRIGGER music__releases__fts__artist_delete_pre
    BEFORE DELETE ON music__releases_artists
    FOR EACH ROW
    BEGIN
        INSERT INTO music__releases__fts (music__releases__fts, rowid, title, artists)
        SELECT 'delete', rowid, title, artists FROM music__releases__fts WHERE rowid = old.release_id;
    END;

CREATE TRIGGER music__releases__fts__artist_delete_post
    AFTER DELETE ON music__releases_artists
    FOR EACH ROW
    BEGIN
        INSERT INTO music__releases__fts (rowid, title, artists)
        SELECT id, title, artists FROM music__releases__fts_content WHERE id = old.release_id;
    END;

CREATE TRIGGER music__releases__fts__artist_update_pre
    BEFORE UPDATE ON music__releases_artists
    FOR EACH ROW
    BEGIN
        INSERT INTO music__releases__fts (music__releases__fts, rowid, title, artists)
        SELECT 'delete', rowid, title, artists FROM music__releases__fts WHERE rowid = old.release_id;
    END;

CREATE TRIGGER music__releases__fts__artist_update_post
    AFTER UPDATE ON music__releases_artists
    FOR EACH ROW
    BEGIN
        INSERT INTO music__releases__fts (rowid, title, artists)
        SELECT id, title, artists FROM music__releases__fts_content WHERE id = new.release_id;
    END;

CREATE VIRTUAL TABLE music__artists__fts USING fts5(
    name,
    content='music__artists',
    content_rowid='id',
    tokenize='trigram'
)
/* music__artists__fts(name) */;

CREATE TABLE IF NOT EXISTS 'music__artists__fts_data'(id INTEGER PRIMARY KEY, block BLOB);

CREATE TABLE IF NOT EXISTS 'music__artists__fts_idx'(segid, term, pgno, PRIMARY KEY(segid, term)) WITHOUT ROWID;

CREATE TABLE IF NOT EXISTS 'music__artists__fts_docsize'(id INTEGER PRIMARY KEY, sz BLOB);

CREATE TABLE IF NOT EXISTS 'music__artists__fts_config'(k PRIMARY KEY, v) WITHOUT ROWID;

CREATE TRIGGER music__artists__fts__insert
    AFTER INSERT ON music__artists
    FOR EACH ROW
    BEGIN
        INSERT INTO music__artists__fts (rowid, name) VALUES (new.id, new.name);
    END;

CREATE TRIGGER music__artists__fts__delete
    AFTER DELETE ON music__artists
    FOR EACH ROW
    BEGIN
        INSERT INTO music__artists__fts (music__artists__fts, rowid, name)
        VALUES ('delete', old.id, old.name);
    END;

CREATE TRIGGER music__artists__fts__update
    AFTER UPDATE ON music__artists
    FOR EACH ROW
    BEGIN
        INSERT INTO music__artists__fts (music__artists__fts, rowid, name)
        VALUES ('delete', old.id, old.name);

        INSERT INTO music__artists__fts (rowid, name) VALUES (new.id, new.name);
    END;

CREATE VIEW music__tracks__fts_content AS
    SELECT
        trks.id AS id,
        trks.title AS title,
        GROUP_CONCAT(arts.name, " ") AS artists
    FROM music__tracks AS trks
    LEFT JOIN music__tracks_artists AS trksarts ON trksarts.track_id = trks.id
    LEFT JOIN music__artists AS arts ON arts.id = trksarts.artist_id
    GROUP BY trks.id
/* music__tracks__fts_content(id,title,artists) */;

CREATE VIRTUAL TABLE music__tracks__fts USING fts5(
    title,
    artists,
    content='music__tracks__fts_content',
    content_rowid='id',
    tokenize='trigram'
)
/* music__tracks__fts(title,artists) */;

CREATE TABLE IF NOT EXISTS 'music__tracks__fts_data'(id INTEGER PRIMARY KEY, block BLOB);

CREATE TABLE IF NOT EXISTS 'music__tracks__fts_idx'(segid, term, pgno, PRIMARY KEY(segid, term)) WITHOUT ROWID;

CREATE TABLE IF NOT EXISTS 'music__tracks__fts_docsize'(id INTEGER PRIMARY KEY, sz BLOB);

CREATE TABLE IF NOT EXISTS 'music__tracks__fts_config'(k PRIMARY KEY, v) WITHOUT ROWID;

CREATE TRIGGER music__tracks__fts__track_insert
    AFTER INSERT ON music__tracks
    FOR EACH ROW
    BEGIN
        INSERT INTO music__tracks__fts (rowid, title, artists)
        SELECT id, title, artists FROM music__tracks__fts_content WHERE id = new.id;
    END;

CREATE TRIGGER music__tracks__fts__track_delete
    BEFORE DELETE ON music__tracks
    FOR EACH ROW
    BEGIN
        INSERT INTO music__tracks__fts (music__tracks__fts, rowid, title, artists)
        SELECT 'delete', rowid, title, artists FROM music__tracks__fts WHERE rowid = old.id;
    END;

CREATE TRIGGER music__tracks__fts__track_update_pre
    BEFORE UPDATE ON music__tracks
    FOR EACH ROW
    BEGIN
        INSERT INTO music__tracks__fts (music__tracks__fts, rowid, title, artists)
        SELECT 'delete', rowid, title, artists FROM music__tracks__fts WHERE rowid = old.id;
    END;

CREATE TRIGGER music__tracks__fts__track_update_post
    AFTER UPDATE ON music__tracks
    FOR EACH ROW
    BEGIN
        INSERT INTO music__tracks__fts (rowid, title, artists)
        SELECT id, title, artists FROM music__tracks__fts_content WHERE id = new.id;
    END;

CREATE TRIGGER music__tracks__fts__artist_insert_pre
    BEFORE INSERT ON music__tracks_artists
    FOR EACH ROW
    BEGIN
        INSERT INTO music__tracks__fts (music__tracks__fts, rowid, title, artists)
        SELECT 'delete', rowid, title, artists FROM music__tracks__fts WHERE rowid = new.track_id;
    END;

CREATE TRIGGER music__tracks__fts__artist_insert_post
    AFTER INSERT ON music__tracks_artists
    FOR EACH ROW
    BEGIN
        INSERT INTO music__tracks__fts (rowid, title, artists)
        SELECT id, title, artists FROM music__tracks__fts_content WHERE id = new.track_id;
    END;

CREATE TRIGGER music__tracks__fts__artist_delete_pre
    BEFORE DELETE ON music__tracks_artists
    FOR EACH ROW
    BEGIN
        INSERT INTO music__tracks__fts (music__tracks__fts, rowid, title, artists)
        SELECT 'delete', rowid, title, artists FROM music__tracks__fts WHERE rowid = old.track_id;
    END;

CREATE TRIGGER music__tracks__fts__artist_delete_post
    AFTER DELETE ON music__tracks_artists
    FOR EACH ROW
    BEGIN
        INSERT INTO music__tracks__fts (rowid, title, artists)
        SELECT id, title, artists FROM music__tracks__fts_content WHERE id = old.track_id;
    END;

CREATE TRIGGER music__tracks__fts__artist_update_pre
    BEFORE UPDATE ON music__tracks_artists
    FOR EACH ROW
    BEGIN
        INSERT INTO music__tracks__fts (music__tracks__fts, rowid, title, artists)
        SELECT 'delete', rowid, title, artists FROM music__tracks__fts WHERE rowid = old.track_id;
    END;

CREATE TRIGGER music__tracks__fts__artist_update_post
    AFTER UPDATE ON music__tracks_artists
    FOR EACH ROW
    BEGIN
        INSERT INTO music__tracks__fts (rowid, title, artists)
        SELECT id, title, artists FROM music__tracks__fts_content WHERE id = new.track_id;
    END;

CREATE VIRTUAL TABLE music__collections__fts USING fts5(
    name,
    content='music__collections',
    content_rowid='id',
    tokenize='trigram'
)
/* music__collections__fts(name) */;

CREATE TABLE IF NOT EXISTS 'music__collections__fts_data'(id INTEGER PRIMARY KEY, block BLOB);

CREATE TABLE IF NOT EXISTS 'music__collections__fts_idx'(segid, term, pgno, PRIMARY KEY(segid, term)) WITHOUT ROWID;

CREATE TABLE IF NOT EXISTS 'music__collections__fts_docsize'(id INTEGER PRIMARY KEY, sz BLOB);

CREATE TABLE IF NOT EXISTS 'music__collections__fts_config'(k PRIMARY KEY, v) WITHOUT ROWID;

CREATE TRIGGER music__collections__fts__insert
    AFTER INSERT ON music__collections
    FOR EACH ROW
    BEGIN
        INSERT INTO music__collections__fts (rowid, name) VALUES (new.id, new.name);
    END;

CREATE TRIGGER music__collections__fts__delete
    AFTER DELETE ON music__collections
    FOR EACH ROW
    BEGIN
        INSERT INTO music__collections__fts (music__collections__fts, rowid, name)
        VALUES ('delete', old.id, old.name);
    END;

CREATE TRIGGER music__collections__fts__update
    AFTER UPDATE ON music__collections
    FOR EACH ROW
    BEGIN
        INSERT INTO music__collections__fts (music__collections__fts, rowid, name)
        VALUES ('delete', old.id, old.name);

        INSERT INTO music__collections__fts (rowid, name) VALUES (new.id, new.name);
    END;

CREATE VIRTUAL TABLE music__playlists__fts USING fts5(
    name,
    content='music__playlists',
    content_rowid='id',
    tokenize='trigram'
)
/* music__playlists__fts(name) */;

CREATE TABLE IF NOT EXISTS 'music__playlists__fts_data'(id INTEGER PRIMARY KEY, block BLOB);

CREATE TABLE IF NOT EXISTS 'music__playlists__fts_idx'(segid, term, pgno, PRIMARY KEY(segid, term)) WITHOUT ROWID;

CREATE TABLE IF NOT EXISTS 'music__playlists__fts_docsize'(id INTEGER PRIMARY KEY, sz BLOB);

CREATE TABLE IF NOT EXISTS 'music__playlists__fts_config'(k PRIMARY KEY, v) WITHOUT ROWID;

CREATE TRIGGER music__playlists__fts__insert
    AFTER INSERT ON music__playlists
    FOR EACH ROW
    BEGIN
        INSERT INTO music__playlists__fts (rowid, name) VALUES (new.id, new.name);
    END;

CREATE TRIGGER music__playlists__fts__delete
    AFTER DELETE ON music__playlists
    FOR EACH ROW
    BEGIN
        INSERT INTO music__playlists__fts (music__playlists__fts, rowid, name)
        VALUES ('delete', old.id, old.name);
    END;

CREATE TRIGGER music__playlists__fts__update
    AFTER UPDATE ON music__playlists
    FOR EACH ROW
    BEGIN
        INSERT INTO music__playlists__fts (music__playlists__fts, rowid, name)
        VALUES ('delete', old.id, old.name);

        INSERT INTO music__playlists__fts (rowid, name) VALUES (new.id, new.name);
    END;

CREATE INDEX music__artists_starred__user_id__idx ON music__artists_starred (user_id);

CREATE INDEX music__artists_starred__artist_id__idx ON music__artists_starred (artist_id);

CREATE INDEX music__releases_artists__release_id__idx ON music__releases_artists (release_id);

CREATE INDEX music__releases_artists__artist_id__idx ON music__releases_artists (artist_id);

CREATE INDEX music__tracks__sha256__idx ON music__tracks (sha256);

CREATE INDEX music__tracks__sha256_initial__idx ON music__tracks (sha256_initial);

CREATE INDEX music__tracks__filepath__idx ON music__tracks (filepath);

CREATE INDEX music__tracks__release_id__idx ON music__tracks (release_id);

CREATE INDEX music__tracks_artists__track_id__idx ON music__tracks_artists (track_id);

CREATE INDEX music__tracks_artists__artist_id__idx ON music__tracks_artists (artist_id);

CREATE INDEX music__collections__type__idx ON music__collections (type);

CREATE INDEX music__collections__last_updated_on__idx ON music__collections (last_updated_on);

CREATE INDEX music__collections__user_id__idx ON music__collections (user_id);

CREATE INDEX music__collections__user_id__type__idx ON music__collections (user_id, type);

CREATE INDEX music__collections__user_id__last_updated_on__idx ON music__collections (user_id, last_updated_on);

CREATE INDEX music__collections_starred__user_id__idx ON music__collections_starred (user_id);

CREATE INDEX music__collections_starred__collection_id__idx ON music__collections_starred (collection_id);

CREATE INDEX music__collections_releases__collection_id__idx ON music__collections_releases (collection_id);

CREATE INDEX music__collections_releases__release_id__idx ON music__collections_releases (release_id);

CREATE INDEX music__collections_releases__collection_id__added_on__idx ON music__collections_releases (collection_id, added_on);

CREATE INDEX music__playlists__type__idx ON music__playlists (type);

CREATE INDEX music__playlists__last_updated_on__idx ON music__playlists (last_updated_on);

CREATE INDEX music__playlists__user_id__idx ON music__playlists (user_id);

CREATE INDEX music__playlists__user_id__type__idx ON music__playlists (user_id, type);

CREATE INDEX music__playlists__user_id__last_updated_on__idx ON music__playlists (user_id, last_updated_on);

CREATE INDEX music__playlists_starred__user_id__idx ON music__playlists_starred (user_id);

CREATE INDEX music__playlists_starred__playlist_id__idx ON music__playlists_starred (playlist_id);

CREATE INDEX music__playlists_tracks__playlist_id__idx ON music__playlists_tracks (playlist_id);

CREATE INDEX music__playlists_tracks__track_id__idx ON music__playlists_tracks (track_id);

CREATE INDEX music__playlists_tracks__playlist_id__added_on__idx ON music__playlists_tracks (playlist_id, added_on);
