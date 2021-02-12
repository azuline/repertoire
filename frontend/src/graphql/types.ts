export type Maybe<T> = T | null;
export type Exact<T extends { [key: string]: unknown }> = { [K in keyof T]: T[K] };
export type MakeOptional<T, K extends keyof T> = Omit<T, K> & { [SubKey in K]?: Maybe<T[SubKey]> };
export type MakeMaybe<T, K extends keyof T> = Omit<T, K> & { [SubKey in K]: Maybe<T[SubKey]> };
/** All built-in and custom scalars, mapped to their actual values */
export type Scalars = {
  ID: string;
  String: string;
  Boolean: boolean;
  Int: number;
  Float: number;
  PosixTime: any;
};


export type Query = {
  __typename?: 'Query';
  artist?: Maybe<Artist>;
  artistFromName?: Maybe<Artist>;
  collection?: Maybe<Collection>;
  collectionFromNameAndType?: Maybe<Collection>;
  playlist?: Maybe<Playlist>;
  playlistFromNameAndType?: Maybe<Playlist>;
  release?: Maybe<Release>;
  track?: Maybe<Track>;
  /** Fetch the currently authenticated user. */
  user?: Maybe<User>;
  /** Fetch all artists. */
  artists?: Maybe<Artists>;
  /** Fetch all collections (of one or more types). */
  collections?: Maybe<Collections>;
  /** Fetch all playlists (of one or more types). */
  playlists?: Maybe<Playlists>;
  /** Search for releases matching a certain criteria. */
  releases?: Maybe<Releases>;
  /** Fetch all existing release years sorted in descending order. */
  releaseYears?: Maybe<Array<Maybe<Scalars['Int']>>>;
};


export type QueryArtistArgs = {
  id: Scalars['Int'];
};


export type QueryArtistFromNameArgs = {
  name: Scalars['String'];
};


export type QueryCollectionArgs = {
  id: Scalars['Int'];
};


export type QueryCollectionFromNameAndTypeArgs = {
  name: Scalars['String'];
  type: CollectionType;
};


export type QueryPlaylistArgs = {
  id: Scalars['Int'];
};


export type QueryPlaylistFromNameAndTypeArgs = {
  name: Scalars['String'];
  type: PlaylistType;
};


export type QueryReleaseArgs = {
  id: Scalars['Int'];
};


export type QueryTrackArgs = {
  id: Scalars['Int'];
};


export type QueryCollectionsArgs = {
  types?: Maybe<Array<Maybe<CollectionType>>>;
};


export type QueryPlaylistsArgs = {
  types?: Maybe<Array<Maybe<PlaylistType>>>;
};


export type QueryReleasesArgs = {
  search?: Maybe<Scalars['String']>;
  collectionIds?: Maybe<Array<Maybe<Scalars['Int']>>>;
  artistIds?: Maybe<Array<Maybe<Scalars['Int']>>>;
  releaseTypes?: Maybe<Array<Maybe<ReleaseType>>>;
  years?: Maybe<Array<Maybe<Scalars['Int']>>>;
  ratings?: Maybe<Array<Maybe<Scalars['Int']>>>;
  page?: Maybe<Scalars['Int']>;
  perPage?: Maybe<Scalars['Int']>;
  sort?: Maybe<ReleaseSort>;
  asc?: Maybe<Scalars['Boolean']>;
};

export type Mutation = {
  __typename?: 'Mutation';
  createArtist?: Maybe<Artist>;
  updateArtist?: Maybe<Artist>;
  createCollection?: Maybe<Collection>;
  updateCollection?: Maybe<Collection>;
  addReleaseToCollection?: Maybe<CollectionAndRelease>;
  delReleaseFromCollection?: Maybe<CollectionAndRelease>;
  createPlaylist?: Maybe<Playlist>;
  updatePlaylist?: Maybe<Playlist>;
  addTrackToPlaylist?: Maybe<PlaylistAndTrack>;
  delTrackFromPlaylist?: Maybe<PlaylistAndTrack>;
  createRelease?: Maybe<Release>;
  updateRelease?: Maybe<Release>;
  addArtistToRelease?: Maybe<ReleaseAndArtist>;
  delArtistFromRelease?: Maybe<ReleaseAndArtist>;
  updateTrack?: Maybe<Track>;
  addArtistToTrack?: Maybe<TrackAndArtist>;
  delArtistFromTrack?: Maybe<TrackAndArtist>;
  /** Update the authenticated user. */
  updateUser?: Maybe<User>;
  /**
   * Generate a new authentication token for the current user. Invalidate the
   * old one.
   */
  newToken?: Maybe<Token>;
};


export type MutationCreateArtistArgs = {
  name: Scalars['String'];
  starred?: Maybe<Scalars['Boolean']>;
};


export type MutationUpdateArtistArgs = {
  id: Scalars['Int'];
  name?: Maybe<Scalars['String']>;
  starred?: Maybe<Scalars['Boolean']>;
};


export type MutationCreateCollectionArgs = {
  name: Scalars['String'];
  type: CollectionType;
  starred?: Maybe<Scalars['Boolean']>;
};


export type MutationUpdateCollectionArgs = {
  id: Scalars['Int'];
  name?: Maybe<Scalars['String']>;
  starred?: Maybe<Scalars['Boolean']>;
};


export type MutationAddReleaseToCollectionArgs = {
  collectionId: Scalars['Int'];
  releaseId: Scalars['Int'];
};


export type MutationDelReleaseFromCollectionArgs = {
  collectionId: Scalars['Int'];
  releaseId: Scalars['Int'];
};


export type MutationCreatePlaylistArgs = {
  name: Scalars['String'];
  type: PlaylistType;
  starred?: Maybe<Scalars['Boolean']>;
};


export type MutationUpdatePlaylistArgs = {
  id: Scalars['Int'];
  name?: Maybe<Scalars['String']>;
  starred?: Maybe<Scalars['Boolean']>;
};


export type MutationAddTrackToPlaylistArgs = {
  playlistId: Scalars['Int'];
  trackId: Scalars['Int'];
};


export type MutationDelTrackFromPlaylistArgs = {
  playlistId: Scalars['Int'];
  trackId: Scalars['Int'];
};


export type MutationCreateReleaseArgs = {
  title: Scalars['String'];
  artistIds: Array<Maybe<Scalars['Int']>>;
  releaseType: ReleaseType;
  releaseYear: Scalars['Int'];
  releaseDate?: Maybe<Scalars['String']>;
  rating?: Maybe<Scalars['Int']>;
};


export type MutationUpdateReleaseArgs = {
  id: Scalars['Int'];
  title?: Maybe<Scalars['String']>;
  releaseType?: Maybe<ReleaseType>;
  releaseYear?: Maybe<Scalars['Int']>;
  releaseDate?: Maybe<Scalars['String']>;
  rating?: Maybe<Scalars['Int']>;
};


export type MutationAddArtistToReleaseArgs = {
  releaseId: Scalars['Int'];
  artistId: Scalars['Int'];
};


export type MutationDelArtistFromReleaseArgs = {
  releaseId: Scalars['Int'];
  artistId: Scalars['Int'];
};


export type MutationUpdateTrackArgs = {
  id: Scalars['Int'];
  title?: Maybe<Scalars['String']>;
  releaseId?: Maybe<Scalars['Int']>;
  trackNumber?: Maybe<Scalars['String']>;
  discNumber?: Maybe<Scalars['String']>;
};


export type MutationAddArtistToTrackArgs = {
  trackId: Scalars['Int'];
  artistId: Scalars['Int'];
  role: ArtistRole;
};


export type MutationDelArtistFromTrackArgs = {
  trackId: Scalars['Int'];
  artistId: Scalars['Int'];
  role: ArtistRole;
};


export type MutationUpdateUserArgs = {
  nickname?: Maybe<Scalars['String']>;
};

export type Artist = {
  __typename?: 'Artist';
  id: Scalars['Int'];
  name: Scalars['String'];
  starred: Scalars['Boolean'];
  numReleases: Scalars['Int'];
  /** The image ID of one of the artist's releases. Potentially null. */
  imageId?: Maybe<Scalars['Int']>;
  releases: Array<Maybe<Release>>;
  /** The top genres of the artist, compiled from their releases. */
  topGenres: Array<Maybe<TopGenre>>;
};

export type Artists = {
  __typename?: 'Artists';
  results: Array<Maybe<Artist>>;
};

export type Collection = {
  __typename?: 'Collection';
  id: Scalars['Int'];
  name: Scalars['String'];
  starred: Scalars['Boolean'];
  type: CollectionType;
  numReleases: Scalars['Int'];
  /** The last datetime a release was added to the collection. */
  lastUpdatedOn?: Maybe<Scalars['PosixTime']>;
  /** The image ID of a release in the collection. Potentially null. */
  imageId?: Maybe<Scalars['Int']>;
  releases: Array<Maybe<Release>>;
  /** The top genres of the collection, compiled from its releases. */
  topGenres: Array<Maybe<TopGenre>>;
};

export type Collections = {
  __typename?: 'Collections';
  results: Array<Maybe<Collection>>;
};

export type Playlist = {
  __typename?: 'Playlist';
  id: Scalars['Int'];
  name: Scalars['String'];
  starred: Scalars['Boolean'];
  type: PlaylistType;
  numTracks: Scalars['Int'];
  /** The last datetime a release was added to the playlist. */
  lastUpdatedOn?: Maybe<Scalars['PosixTime']>;
  /** The image ID of a track in the playlst. Potentially null. */
  imageId?: Maybe<Scalars['Int']>;
  tracks: Array<Maybe<Track>>;
  /** The top genres of the playlist, compiled from its tracks. */
  topGenres: Array<Maybe<TopGenre>>;
};

export type Playlists = {
  __typename?: 'Playlists';
  results: Array<Maybe<Playlist>>;
};

export type Release = {
  __typename?: 'Release';
  id: Scalars['Int'];
  title: Scalars['String'];
  releaseType: ReleaseType;
  addedOn: Scalars['PosixTime'];
  inInbox: Scalars['Boolean'];
  inFavorites: Scalars['Boolean'];
  releaseYear?: Maybe<Scalars['Int']>;
  /** The date that the release was released in YYYY-MM-DD format (Optional). */
  releaseDate?: Maybe<Scalars['String']>;
  /** The release rating, either null or an int on the interval [1, 10]. */
  rating?: Maybe<Scalars['Int']>;
  numTracks: Scalars['Int'];
  /** The total runtime (sum of track durations). */
  runtime: Scalars['Int'];
  /** The image ID of the release's cover image. Potentially null. */
  imageId?: Maybe<Scalars['Int']>;
  artists: Array<Maybe<Artist>>;
  tracks: Array<Maybe<Track>>;
  genres: Array<Maybe<Collection>>;
  labels: Array<Maybe<Collection>>;
  collages: Array<Maybe<Collection>>;
};

export type Releases = {
  __typename?: 'Releases';
  /** The total number of releases matching the query across all pages. */
  total: Scalars['Int'];
  /** The releases on the current page. */
  results: Array<Maybe<Release>>;
};

export type Track = {
  __typename?: 'Track';
  id: Scalars['Int'];
  title: Scalars['String'];
  duration: Scalars['Int'];
  trackNumber: Scalars['String'];
  discNumber: Scalars['String'];
  release: Release;
  artists: Array<Maybe<TrackArtist>>;
};

export type TrackArtist = {
  __typename?: 'TrackArtist';
  artist: Artist;
  /** The role that the artist has on the track. */
  role: ArtistRole;
};

/** A type that represents the top genres of an artist/collection. */
export type TopGenre = {
  __typename?: 'TopGenre';
  genre: Collection;
  /** The number of releases in the artist/collection that match this genre. */
  numMatches: Scalars['Int'];
};

export type User = {
  __typename?: 'User';
  id: Scalars['Int'];
  nickname: Scalars['String'];
};

export type Token = {
  __typename?: 'Token';
  hex: Scalars['String'];
};

export type CollectionAndRelease = {
  __typename?: 'CollectionAndRelease';
  collection: Collection;
  release: Release;
};

export type PlaylistAndTrack = {
  __typename?: 'PlaylistAndTrack';
  playlist: Playlist;
  track: Track;
};

export type ReleaseAndArtist = {
  __typename?: 'ReleaseAndArtist';
  release: Release;
  artist: Artist;
};

export type TrackAndArtist = {
  __typename?: 'TrackAndArtist';
  track: Track;
  trackArtist: TrackArtist;
};

export enum ArtistRole {
  Main = 'MAIN',
  Feature = 'FEATURE',
  Remixer = 'REMIXER',
  Producer = 'PRODUCER',
  Composer = 'COMPOSER',
  Conductor = 'CONDUCTOR',
  Djmixer = 'DJMIXER'
}

export enum ReleaseType {
  Album = 'ALBUM',
  Single = 'SINGLE',
  Ep = 'EP',
  Compilation = 'COMPILATION',
  Soundtrack = 'SOUNDTRACK',
  Spokenword = 'SPOKENWORD',
  Live = 'LIVE',
  Remix = 'REMIX',
  Djmix = 'DJMIX',
  Mixtape = 'MIXTAPE',
  Other = 'OTHER',
  Unknown = 'UNKNOWN'
}

export enum CollectionType {
  System = 'SYSTEM',
  Collage = 'COLLAGE',
  Label = 'LABEL',
  Genre = 'GENRE'
}

export enum ReleaseSort {
  RecentlyAdded = 'RECENTLY_ADDED',
  Title = 'TITLE',
  Year = 'YEAR',
  Rating = 'RATING',
  Random = 'RANDOM'
}

export enum PlaylistType {
  System = 'SYSTEM',
  Playlist = 'PLAYLIST'
}
