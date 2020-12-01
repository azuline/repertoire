-- This file should undo anything in `up.sql`

DROP TABLE music__releases;
DROP TABLE music__release_types;
DROP TABLE music__artists;
DROP TABLE music__artist_roles;
DROP TABLE music__releases_artists;
DROP TABLE music__tracks;
DROP TABLE music__tracks_artists;
DROP TABLE music__collections;
DROP TABLE music__collection_types;
DROP TABLE music__collections_releases;
DROP TABLE music__releases_search_index;
DROP TABLE images;
DROP TABLE images__music_releases_to_fetch;
DROP TABLE system__users;
DROP TABLE system__secret_key;
DROP INDEX idx__music__releases__title;
DROP INDEX idx__music__releases__release_type;
DROP INDEX idx__music__releases__added_on;
DROP INDEX idx__music__releases__release_year;
DROP INDEX idx__music__releases__rating;
DROP INDEX idx__music__artists__sorting;
DROP INDEX idx__music__collections__sorting;
DROP INDEX idx__music__releases_search_index__word;
