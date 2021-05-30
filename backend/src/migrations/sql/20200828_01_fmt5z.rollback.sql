-- This file should undo anything in `up.sql`

DROP TABLE music__releases;
DROP TABLE music__release_types__enum;
DROP TABLE music__releases_images_to_fetch;
DROP TABLE music__artists;
DROP TABLE music__artist_roles__enum;
DROP TABLE music__artists_starred;
DROP TABLE music__releases_artists;
DROP TABLE music__tracks;
DROP TABLE music__tracks_artists;
DROP TABLE music__collections;
DROP TABLE music__collection_types__enum;
DROP TABLE music__collections_starred;
DROP TABLE music__collections_releases;
DROP TABLE music__playlists;
DROP TABLE music__playlist_types__enum;
DROP TABLE music__playlists_starred;
DROP TABLE music__playlists_tracks;
DROP TABLE images;
DROP TABLE system__users;
DROP TABLE system__invites;
DROP TABLE system__secret_key;

DROP VIEW music__releases__fts_content;
DROP TABLE music__releases__fts;
DROP TABLE music__artists__fts;
DROP VIEW music__tracks__fts_content;
DROP TABLE music__tracks__fts;
DROP TABLE music__collections__fts;
DROP TABLE music__playlists__fts;
