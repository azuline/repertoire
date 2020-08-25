table! {
    music__artist_roles (id) {
        id -> Integer,
        role -> Text,
    }
}

table! {
    music__artists (id) {
        id -> Integer,
        name -> Text,
        image_path -> Nullable<Text>,
        favorite -> Bool,
    }
}

table! {
    music__artists_links (artist_id, link) {
        artist_id -> Integer,
        link -> Text,
    }
}

table! {
    music__collection_types (id) {
        id -> Integer,
        #[sql_name = "type"]
        type_ -> Text,
    }
}

table! {
    music__collections (id) {
        id -> Integer,
        name -> Text,
        favorite -> Bool,
        #[sql_name = "type"]
        type_ -> Integer,
    }
}

table! {
    music__collections_releases (release_id, collection_id) {
        release_id -> Integer,
        collection_id -> Integer,
        added_on -> Timestamp,
    }
}

table! {
    music__release_types (id) {
        id -> Integer,
        #[sql_name = "type"]
        type_ -> Text,
    }
}

table! {
    music__releases (id) {
        id -> Integer,
        title -> Text,
        release_type -> Integer,
        release_year -> Integer,
        release_date -> Nullable<Timestamp>,
        image_path -> Nullable<Text>,
        added_on -> Timestamp,
    }
}

table! {
    music__releases_artists (release_id, artist_id) {
        release_id -> Integer,
        artist_id -> Integer,
    }
}

table! {
    music__releases_links (release_id, link) {
        release_id -> Integer,
        link -> Text,
    }
}

table! {
    music__saved_queries (id) {
        id -> Integer,
        query -> Text,
        added_on -> Timestamp,
    }
}

table! {
    music__tracks (id) {
        id -> Integer,
        filepath -> Text,
        sha256 -> Binary,
        title -> Text,
        release_id -> Integer,
        track_number -> Text,
        disc_number -> Text,
        duration -> Integer,
    }
}

table! {
    music__tracks_artists (track_id, artist_id, role) {
        track_id -> Integer,
        artist_id -> Integer,
        role -> Integer,
    }
}

joinable!(music__collections -> music__collection_types (type));
joinable!(music__collections_releases -> music__collections (collection_id));
joinable!(music__collections_releases -> music__releases (release_id));
joinable!(music__releases -> music__release_types (release_type));
joinable!(music__releases_artists -> music__artists (artist_id));
joinable!(music__releases_artists -> music__releases (release_id));
joinable!(music__tracks -> music__releases (release_id));
joinable!(music__tracks_artists -> music__artist_roles (role));
joinable!(music__tracks_artists -> music__artists (artist_id));
joinable!(music__tracks_artists -> music__tracks (track_id));

allow_tables_to_appear_in_same_query!(
    music__artist_roles,
    music__artists,
    music__artists_links,
    music__collection_types,
    music__collections,
    music__collections_releases,
    music__release_types,
    music__releases,
    music__releases_artists,
    music__releases_links,
    music__saved_queries,
    music__tracks,
    music__tracks_artists,
);
