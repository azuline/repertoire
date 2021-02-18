-- initial creation of the database
-- depends:

CREATE TABLE music__releases (
    id INTEGER NOT NULL,
    title VARCHAR COLLATE 'NOCASE' NOT NULL,
    release_type INTEGER NOT NULL DEFAULT 1,
    release_year INTEGER,
    release_date DATE,
    image_id INTEGER,
    added_on TIMESTAMP DEFAULT (CURRENT_TIMESTAMP) NOT NULL,
    rating INTEGER CHECK (rating >= 1 AND rating <=10),
    PRIMARY KEY (id),
    FOREIGN KEY (release_type) REFERENCES music__release_types__enum(id),
    FOREIGN KEY (image_id) REFERENCES images(id)
);

CREATE INDEX idx__music__releases__title ON music__releases (title);

CREATE INDEX idx__music__releases__release_type ON music__releases (release_type);

CREATE INDEX idx__music__releases__added_on ON music__releases (added_on);

CREATE INDEX idx__music__releases__release_year ON music__releases (release_year);

CREATE INDEX idx__music__releases__rating ON music__releases (rating);


CREATE TABLE music__release_types__enum (
    id INTEGER NOT NULL,
    type VARCHAR NOT NULL,
    PRIMARY KEY (id),
    UNIQUE (type)
);

--- Insert our release types.
INSERT INTO music__release_types__enum (id, type)
    VALUES (1,  'ALBUM'),
           (2,  'SINGLE'),
           (3,  'EP'),
           (4,  'COMPILATION'),
           (5,  'SOUNDTRACK'),
           (6,  'SPOKENWORD'),
           (7,  'LIVE'),
           (8,  'REMIX'),
           (9,  'DJMIX'),
           (10, 'MIXTAPE'),
           (11, 'OTHER'),
           (12, 'UNKNOWN');

-- Create an Unknown release.
INSERT INTO music__releases (id, title, release_type, added_on)
    VALUES (1, 'Unknown Release', 12, '1970-01-01 00:00:00');


CREATE TABLE music__artists (
    id INTEGER NOT NULL,
    name VARCHAR COLLATE 'NOCASE' NOT NULL,
    starred BOOLEAN NOT NULL DEFAULT 0 CHECK (starred IN (0, 1)),
    PRIMARY KEY (id)
);

CREATE INDEX idx__music__artists__sorting ON music__artists (starred DESC, name);

-- Create an Unknown artist.
INSERT INTO music__artists (id, name) VALUES (1, 'Unknown Artist');

CREATE TABLE music__artist_roles__enum (
    id INTEGER NOT NULL,
    role VARCHAR NOT NULL,
    PRIMARY KEY (id),
    UNIQUE (role)
);

-- Insert our role types.
INSERT INTO music__artist_roles__enum (id, role)
    VALUES (1, 'MAIN'),
           (2, 'FEATURE'),
           (3, 'REMIXER'),
           (4, 'PRODUCER'),
           (5, 'COMPOSER'),
           (6, 'CONDUCTOR'),
           (7, 'DJMIXER');

CREATE TABLE music__releases_artists (
    release_id INTEGER NOT NULL,
    artist_id INTEGER NOT NULL,
    PRIMARY KEY (release_id, artist_id),
    FOREIGN KEY (release_id) REFERENCES music__releases (id),
    FOREIGN KEY (artist_id) REFERENCES music__artists (id)
);

CREATE TABLE music__tracks (
    id INTEGER NOT NULL,
    filepath VARCHAR NOT NULL,
    sha256 BLOB NOT NULL,
    title VARCHAR NOT NULL DEFAULT 'Untitled',
    release_id INTEGER NOT NULL DEFAULT 1,
    track_number VARCHAR NOT NULL DEFAULT '1',
    disc_number VARCHAR NOT NULL DEFAULT '1',
    duration INTEGER NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (release_id) REFERENCES music__releases (id),
    UNIQUE (filepath),
    UNIQUE (sha256)
);

CREATE TABLE music__tracks_artists (
    track_id INTEGER NOT NULL,
    artist_id INTEGER NOT NULL,
    role INTEGER NOT NULL,
    PRIMARY KEY (track_id, artist_id, role),
    FOREIGN KEY (track_id) REFERENCES music__tracks (id),
    FOREIGN KEY (artist_id) REFERENCES music__artists (id),
    FOREIGN KEY (role) REFERENCES music__artist_roles__enum (id)
);

CREATE TABLE music__collections (
    id INTEGER NOT NULL,
    name VARCHAR COLLATE 'NOCASE' NOT NULL,
    starred BOOLEAN NOT NULL DEFAULT 0 CHECK (starred IN (0, 1)),
    type INTEGER NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (type) REFERENCES music__collection_types__enum(id),
    UNIQUE (name, type)
);

CREATE INDEX idx__music__collections__sorting ON
    music__collections (type, starred DESC, name);

CREATE TABLE music__collection_types__enum (
    id INTEGER NOT NULL,
    type VARCHAR NOT NULL,
    PRIMARY KEY (id),
    UNIQUE (type)
);

-- Insert our collection types.
INSERT INTO music__collection_types__enum (id, type)
    VALUES (1, 'System'),
           (2, 'Collage'),
           (3, 'Label'),
           (4, 'Genre');

-- Insert a system inbox collection.
INSERT INTO music__collections (id, name, type, starred)
    VALUES (1, 'Inbox', 1, 1),
           (2, 'Favorites', 1, 1);

CREATE TABLE music__collections_releases (
    collection_id INTEGER NOT NULL,
    release_id INTEGER NOT NULL,
    added_on TIMESTAMP DEFAULT (CURRENT_TIMESTAMP) NOT NULL,
    PRIMARY KEY (release_id, collection_id),
    FOREIGN KEY (release_id) REFERENCES music__releases(id) ON DELETE CASCADE,
    FOREIGN KEY (collection_id) REFERENCES music__collections(id) ON DELETE CASCADE
);

CREATE TABLE music__playlists (
    id INTEGER NOT NULL,
    name VARCHAR COLLATE 'NOCASE' NOT NULL,
    starred BOOLEAN NOT NULL DEFAULT 0 CHECK (starred IN (0, 1)),
    type INTEGER NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (type) REFERENCES music__playlist_types__enum(id),
    UNIQUE (name, type)
);

CREATE INDEX idx__music__playlists__sorting
    ON music__playlists (type, starred DESC, name);

CREATE TABLE music__playlist_types__enum (
    id INTEGER NOT NULL,
    type VARCHAR NOT NULL,
    PRIMARY KEY (id),
    UNIQUE (type)
);

-- Insert our playlist types.
INSERT INTO music__playlist_types__enum (id, type)
    VALUES (1, 'System'),
           (2, 'Playlist');

-- Insert a system inbox playlist.
INSERT INTO music__playlists (id, name, type, starred)
    VALUES (1, 'Favorites', 1, 1);

CREATE TABLE music__playlists_tracks (
    id INTEGER NOT NULL,
    playlist_id INTEGER NOT NULL,
    track_id INTEGER NOT NULL,
    added_on TIMESTAMP DEFAULT (CURRENT_TIMESTAMP) NOT NULL,
    position INTEGER NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (track_id) REFERENCES music__tracks(id) ON DELETE CASCADE,
    FOREIGN KEY (playlist_id) REFERENCES music__playlists(id) ON DELETE CASCADE,
    UNIQUE (playlist_id, position)
);

CREATE INDEX idx__music__playlists_tracks__playlist_position
    ON music__playlists_tracks (playlist_id, position);

CREATE TABLE music__releases_search_index (
    id INTEGER NOT NULL,
    release_id INTEGER NOT NULL,
    word VARCHAR COLLATE 'NOCASE' NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (release_id) REFERENCES music__releases(id) ON DELETE CASCADE
);

CREATE INDEX idx__music__releases_search_index__word
    ON music__releases_search_index (word);

CREATE TABLE images (
    id INTEGER NOT NULL,
    path VARCHAR NOT NULL,
    PRIMARY KEY (id),
    UNIQUE (path)
);

CREATE TABLE images__music_releases_to_fetch (
    release_id INTEGER NOT NULL,
    PRIMARY KEY (release_id),
    FOREIGN KEY (release_id) REFERENCES music__releases(id) ON DELETE CASCADE
);

CREATE TABLE system__users (
    id INTEGER NOT NULL,
    nickname VARCHAR NOT NULL,
    token_prefix BLOB NOT NULL,
    token_hash VARCHAR NOT NULL,
    csrf_token BLOB NOT NULL,
    PRIMARY KEY (id),
    UNIQUE (token_prefix)
);

CREATE TABLE system__secret_key (
    key BLOB NOT NULL,
    PRIMARY KEY (key)
);
