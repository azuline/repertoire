-- initial creation of the database
-- depends:

CREATE TABLE music__releases (
    id INTEGER NOT NULL,
    title VARCHAR NOT NULL,
    release_type INTEGER NOT NULL DEFAULT 1,
    release_year INTEGER NOT NULL DEFAULT 0,
    release_date DATE,
    image_path VARCHAR,
    added_on TIMESTAMP DEFAULT (CURRENT_TIMESTAMP) NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (release_type) REFERENCES music__release_types(id)
);

CREATE TABLE music__release_types (
    id INTEGER NOT NULL,
    type VARCHAR NOT NULL,
    PRIMARY KEY (id),
    UNIQUE (type)
);

--- Insert our release types.
INSERT INTO music__release_types (id, type) VALUES
    (1, "ALBUM"),
    (2, "SINGLE"),
    (3, "EP"),
    (4, "COMPILATION"),
    (5, "SOUNDTRACK"),
    (6, "SPOKENWORD"),
    (7, "LIVE"),
    (8, "REMIX"),
    (9, "DJMIX"),
    (10, "MIXTAPE"),
    (11, "OTHER"),
    (12, "UNKNOWN");

-- Create an Unknown release.
INSERT INTO music__releases (id, title, release_type, added_on) VALUES
    (1, "Unknown Release", 12, "1970-01-01 00:00:00");


CREATE TABLE music__artists (
    id INTEGER NOT NULL,
    name VARCHAR COLLATE "NOCASE" NOT NULL,
    favorite BOOLEAN NOT NULL DEFAULT 0 CHECK (favorite IN (0, 1)),
    PRIMARY KEY (id),
    UNIQUE (name) -- We will have this constraint for now...
);

-- Create an Unknown artist.
INSERT INTO music__artists (id, name) VALUES (1, "Unknown Artist");

CREATE TABLE music__artist_roles (
    id INTEGER NOT NULL,
    role VARCHAR NOT NULL,
    PRIMARY KEY (id),
    UNIQUE (role)
);

-- Insert our role types.
INSERT INTO music__artist_roles (id, role) VALUES
    (1, "MAIN"),
    (2, "FEATURE"),
    (3, "REMIXER"),
    (4, "PRODUCER"),
    (5, "COMPOSER"),
    (6, "CONDUCTOR"),
    (7, "DJMIXER");

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
    title VARCHAR NOT NULL DEFAULT "Untitled",
    release_id INTEGER NOT NULL DEFAULT 1,
    track_number VARCHAR NOT NULL DEFAULT 1,
    disc_number VARCHAR NOT NULL DEFAULT 1,
    duration INTEGER NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (release_id) REFERENCES music__releases (id),
    UNIQUE (filepath)
);

CREATE TABLE music__tracks_artists (
    track_id INTEGER NOT NULL,
    artist_id INTEGER NOT NULL,
    role INTEGER NOT NULL,
    PRIMARY KEY (track_id, artist_id, role),
    FOREIGN KEY (track_id) REFERENCES music__tracks (id),
    FOREIGN KEY (artist_id) REFERENCES music__artists (id),
    FOREIGN KEY (role) REFERENCES music__artist_roles (id)
);

CREATE TABLE music__collections (
    id INTEGER NOT NULL,
    name VARCHAR COLLATE "NOCASE" NOT NULL,
    -- Ghetto SQLite boolean!
    favorite BOOLEAN NOT NULL DEFAULT 0 CHECK (favorite IN (0, 1)),
    type INTEGER NOT NULL,
    PRIMARY KEY (id),
    UNIQUE (name, type),
    FOREIGN KEY (type) REFERENCES music__collection_types(id)
);

CREATE TABLE music__collection_types (
    id INTEGER NOT NULL,
    type VARCHAR NOT NULL,
    PRIMARY KEY (id),
    UNIQUE (type)
);

-- Insert our collection types.
INSERT INTO music__collection_types (id, type) VALUES
    (1, "System"),
    (2, "Collage"),
    (3, "Label"),
    (4, "Genre"),
    (5, "Rating");

-- Insert a system inbox collection.
INSERT INTO music__collections (id, name, type) VALUES
    (1, "Inbox", 1),
    (2, "Favorite", 1),
	(3, "1", 5),
	(4, "2", 5),
	(5, "3", 5),
	(6, "4", 5),
	(7, "5", 5),
	(8, "6", 5),
	(9, "7", 5),
	(10, "8", 5),
	(11, "9", 5);

CREATE TABLE music__collections_releases (
    collection_id INTEGER NOT NULL,
    release_id INTEGER NOT NULL,
    added_on TIMESTAMP DEFAULT (CURRENT_TIMESTAMP) NOT NULL,
    PRIMARY KEY (release_id, collection_id),
    FOREIGN KEY (release_id) REFERENCES music__releases(id) ON DELETE CASCADE,
    FOREIGN KEY (collection_id) REFERENCES music__collections(id) ON DELETE CASCADE
);

CREATE TABLE music__releases_search_index (
	id INTEGER NOT NULL,
	release_id INTEGER NOT NULL,
	word VARCHAR COLLATE "NOCASE" NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY (release_id) REFERENCES music__releases(id) ON DELETE CASCADE
);

CREATE TABLE music__releases_to_fetch_images (
	release_id INTEGER NOT NULL,
	PRIMARY KEY (release_id),
	FOREIGN KEY (release_id) REFERENCES music__releases(id) ON DELETE CASCADE
);

CREATE TABLE music__play_history (
	id INTEGER NOT NULL,
	time TIMESTAMP DEFAULT (CURRENT_TIMESTAMP) NOT NULL,
	track_id INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY (track_id) REFERENCES music__tracks(id) ON DELETE SET NULL
);

CREATE TABLE system__users (
    id INTEGER NOT NULL,
    username VARCHAR NOT NULL,
    token_prefix BLOB NOT NULL,
    token_hash VARCHAR NOT NULL,
    PRIMARY KEY (id),
    UNIQUE (username),
    UNIQUE (token_prefix)
);
