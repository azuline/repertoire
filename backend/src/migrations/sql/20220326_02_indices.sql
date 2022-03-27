-- initial database schema (application version 0.2.0)
-- depends: 20200828_01_fmt5z

-----------------------------
--- ADD INDICES TO TABLES ---
-----------------------------

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
