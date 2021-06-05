import { gql } from '@apollo/client';
import * as Apollo from '@apollo/client';
import { FieldPolicy, FieldReadFunction, TypePolicies, TypePolicy } from '@apollo/client/cache';
export type Maybe<T> = T | null;
export type Exact<T extends { [key: string]: unknown }> = { [K in keyof T]: T[K] };
export type MakeOptional<T, K extends keyof T> = Omit<T, K> & { [SubKey in K]?: Maybe<T[SubKey]> };
export type MakeMaybe<T, K extends keyof T> = Omit<T, K> & { [SubKey in K]: Maybe<T[SubKey]> };
const defaultOptions =  {}
/** All built-in and custom scalars, mapped to their actual values */
export type Scalars = {
  ID: string;
  String: string;
  Boolean: boolean;
  Int: number;
  Float: number;
  PosixTime: number;
};

export type IArtist = {
  __typename?: 'Artist';
  id: Scalars['Int'];
  name: Scalars['String'];
  starred: Scalars['Boolean'];
  numReleases: Scalars['Int'];
  /** The image ID of one of the artist's releases. */
  imageId: Maybe<Scalars['Int']>;
  releases: Array<IRelease>;
  /** The top genres of the artist, compiled from their releases. */
  topGenres: Array<ITopGenre>;
};

export enum IArtistRole {
  Main = 'MAIN',
  Feature = 'FEATURE',
  Remixer = 'REMIXER',
  Producer = 'PRODUCER',
  Composer = 'COMPOSER',
  Conductor = 'CONDUCTOR',
  Djmixer = 'DJMIXER'
}

export type IArtistWithRole = {
  __typename?: 'ArtistWithRole';
  artist: IArtist;
  /** The role that the artist has on the track. */
  role: IArtistRole;
};

export type IArtistWithRoleInput = {
  artist_id: Scalars['Int'];
  /** The role that the artist has on the track. */
  role: IArtistRole;
};

export type IArtists = {
  __typename?: 'Artists';
  /** The total number of artists matching the query across all pages. */
  total: Scalars['Int'];
  /** The artists on the current page. */
  results: Array<IArtist>;
};

export type ICollection = {
  __typename?: 'Collection';
  id: Scalars['Int'];
  name: Scalars['String'];
  starred: Scalars['Boolean'];
  type: ICollectionType;
  numReleases: Scalars['Int'];
  /** The last datetime a release was added to the collection. */
  lastUpdatedOn: Scalars['PosixTime'];
  /** The image ID of a release in the collection. */
  imageId: Maybe<Scalars['Int']>;
  releases: Array<IRelease>;
  /** The top genres of the collection, compiled from its releases. */
  topGenres: Array<ITopGenre>;
  /** The user the collection belongs to. */
  user: Maybe<IUser>;
};

export type ICollectionAndRelease = {
  __typename?: 'CollectionAndRelease';
  collection: ICollection;
  release: IRelease;
};

export enum ICollectionType {
  System = 'SYSTEM',
  Personal = 'PERSONAL',
  Collage = 'COLLAGE',
  Label = 'LABEL',
  Genre = 'GENRE'
}

export type ICollections = {
  __typename?: 'Collections';
  /** The total number of collections matching the query across all pages. */
  total: Scalars['Int'];
  /** The collections on the current page. */
  results: Array<ICollection>;
};

export type IInvite = {
  __typename?: 'Invite';
  id: Scalars['Int'];
  /** Hex encoded invite code. */
  code: Scalars['String'];
  createdBy: IUser;
  createdAt: Scalars['PosixTime'];
  usedBy: Maybe<IUser>;
};

export type IInvites = {
  __typename?: 'Invites';
  /** The total number of invites matching the query across all pages. */
  total: Scalars['Int'];
  /** The invites on the current page. */
  results: Array<IInvite>;
};

export type IMutation = {
  __typename?: 'Mutation';
  /** Update the authenticated user. */
  updateUser: IUser;
  /**
   * Generate a new authentication token for the current user. Invalidate the
   * old one.
   */
  newToken: IToken;
  createArtist: IArtist;
  updateArtist: IArtist;
  starArtist: IArtist;
  unstarArtist: IArtist;
  createCollection: ICollection;
  updateCollection: ICollection;
  starCollection: ICollection;
  unstarCollection: ICollection;
  addReleaseToCollection: ICollectionAndRelease;
  delReleaseFromCollection: ICollectionAndRelease;
  createInvite: IInvite;
  createPlaylist: IPlaylist;
  updatePlaylist: IPlaylist;
  starPlaylist: IPlaylist;
  unstarPlaylist: IPlaylist;
  createPlaylistEntry: IPlaylistEntry;
  delPlaylistEntry: IPlaylistAndTrack;
  delPlaylistEntries: IPlaylistAndTrack;
  updatePlaylistEntry: IPlaylistEntry;
  createRelease: IRelease;
  updateRelease: IRelease;
  addArtistToRelease: IReleaseAndArtist;
  delArtistFromRelease: IReleaseAndArtist;
  updateTrack: ITrack;
  addArtistToTrack: ITrackAndArtist;
  delArtistFromTrack: ITrackAndArtist;
};


export type IMutationUpdateUserArgs = {
  nickname: Maybe<Scalars['String']>;
};


export type IMutationCreateArtistArgs = {
  name: Scalars['String'];
};


export type IMutationUpdateArtistArgs = {
  id: Scalars['Int'];
  name: Maybe<Scalars['String']>;
};


export type IMutationStarArtistArgs = {
  id: Scalars['Int'];
};


export type IMutationUnstarArtistArgs = {
  id: Scalars['Int'];
};


export type IMutationCreateCollectionArgs = {
  name: Scalars['String'];
  type: ICollectionType;
};


export type IMutationUpdateCollectionArgs = {
  id: Scalars['Int'];
  name: Maybe<Scalars['String']>;
};


export type IMutationStarCollectionArgs = {
  id: Scalars['Int'];
};


export type IMutationUnstarCollectionArgs = {
  id: Scalars['Int'];
};


export type IMutationAddReleaseToCollectionArgs = {
  collectionId: Scalars['Int'];
  releaseId: Scalars['Int'];
};


export type IMutationDelReleaseFromCollectionArgs = {
  collectionId: Scalars['Int'];
  releaseId: Scalars['Int'];
};


export type IMutationCreatePlaylistArgs = {
  name: Scalars['String'];
  type: IPlaylistType;
};


export type IMutationUpdatePlaylistArgs = {
  id: Scalars['Int'];
  name: Maybe<Scalars['String']>;
};


export type IMutationStarPlaylistArgs = {
  id: Scalars['Int'];
};


export type IMutationUnstarPlaylistArgs = {
  id: Scalars['Int'];
};


export type IMutationCreatePlaylistEntryArgs = {
  playlistId: Scalars['Int'];
  trackId: Scalars['Int'];
};


export type IMutationDelPlaylistEntryArgs = {
  id: Scalars['Int'];
};


export type IMutationDelPlaylistEntriesArgs = {
  playlistId: Scalars['Int'];
  trackId: Scalars['Int'];
};


export type IMutationUpdatePlaylistEntryArgs = {
  id: Scalars['Int'];
  position: Scalars['Int'];
};


export type IMutationCreateReleaseArgs = {
  title: Scalars['String'];
  artists: Array<IArtistWithRoleInput>;
  releaseType: IReleaseType;
  releaseYear: Scalars['Int'];
  releaseDate: Maybe<Scalars['String']>;
  rating: Maybe<Scalars['Int']>;
};


export type IMutationUpdateReleaseArgs = {
  id: Scalars['Int'];
  title: Maybe<Scalars['String']>;
  releaseType: Maybe<IReleaseType>;
  releaseYear: Maybe<Scalars['Int']>;
  releaseDate: Maybe<Scalars['String']>;
  rating: Maybe<Scalars['Int']>;
};


export type IMutationAddArtistToReleaseArgs = {
  releaseId: Scalars['Int'];
  artistId: Scalars['Int'];
  role: IArtistRole;
};


export type IMutationDelArtistFromReleaseArgs = {
  releaseId: Scalars['Int'];
  artistId: Scalars['Int'];
  role: IArtistRole;
};


export type IMutationUpdateTrackArgs = {
  id: Scalars['Int'];
  title: Maybe<Scalars['String']>;
  releaseId: Maybe<Scalars['Int']>;
  trackNumber: Maybe<Scalars['String']>;
  discNumber: Maybe<Scalars['String']>;
};


export type IMutationAddArtistToTrackArgs = {
  trackId: Scalars['Int'];
  artistId: Scalars['Int'];
  role: IArtistRole;
};


export type IMutationDelArtistFromTrackArgs = {
  trackId: Scalars['Int'];
  artistId: Scalars['Int'];
  role: IArtistRole;
};

export type IPlaylist = {
  __typename?: 'Playlist';
  id: Scalars['Int'];
  name: Scalars['String'];
  starred: Scalars['Boolean'];
  type: IPlaylistType;
  numTracks: Scalars['Int'];
  /** The last datetime a release was added to the playlist. */
  lastUpdatedOn: Scalars['PosixTime'];
  /** The image ID of a track in the playlst. Potentially null. */
  imageId: Maybe<Scalars['Int']>;
  entries: Array<IPlaylistEntry>;
  /** The top genres of the playlist, compiled from its tracks. */
  topGenres: Array<ITopGenre>;
  /** The user the playlist belongs to. */
  user: Maybe<IUser>;
};

export type IPlaylistAndTrack = {
  __typename?: 'PlaylistAndTrack';
  playlist: IPlaylist;
  track: ITrack;
};

export type IPlaylistEntry = {
  __typename?: 'PlaylistEntry';
  id: Scalars['Int'];
  playlistId: Scalars['Int'];
  trackId: Scalars['Int'];
  position: Scalars['Int'];
  addedOn: Scalars['PosixTime'];
  playlist: IPlaylist;
  track: ITrack;
};

export enum IPlaylistType {
  System = 'SYSTEM',
  Personal = 'PERSONAL',
  Playlist = 'PLAYLIST'
}

export type IPlaylists = {
  __typename?: 'Playlists';
  /** The total number of playlists matching the query across all pages. */
  total: Scalars['Int'];
  /** The playlists on the current page. */
  results: Array<IPlaylist>;
};


export type IQuery = {
  __typename?: 'Query';
  /** Fetch the currently authenticated user. */
  user: IUser;
  /** Search artists. */
  artists: IArtists;
  /** Fetch an artist by ID. */
  artist: IArtist;
  /** Fetch an artist by name. */
  artistFromName: IArtist;
  /** Search collections. */
  collections: ICollections;
  /** Fetch a collection by ID. */
  collection: ICollection;
  /** Fetch a collection by name, type, and user. */
  collectionFromNameTypeUser: ICollection;
  /** Fetch invites. */
  invites: IInvites;
  /** Fetch invites by ID. */
  invite: IInvite;
  /** Search playlists. */
  playlists: IPlaylists;
  /** Fetch a playlist by ID. */
  playlist: IPlaylist;
  /** Fetch a playlist by name, type, and user. */
  playlistFromNameTypeUser: IPlaylist;
  /** Search releases. */
  releases: IReleases;
  /** Fetch a release by ID. */
  release: IRelease;
  /** Search tracks. */
  tracks: Maybe<ITracks>;
  /** Fetch a track by ID. */
  track: ITrack;
  /** Fetch all existing release years sorted in descending order. */
  releaseYears: Array<Scalars['Int']>;
};


export type IQueryArtistsArgs = {
  search: Maybe<Scalars['String']>;
  page: Maybe<Scalars['Int']>;
  perPage: Maybe<Scalars['Int']>;
};


export type IQueryArtistArgs = {
  id: Scalars['Int'];
};


export type IQueryArtistFromNameArgs = {
  name: Scalars['String'];
};


export type IQueryCollectionsArgs = {
  search: Maybe<Scalars['String']>;
  types: Maybe<Array<ICollectionType>>;
  userIds: Maybe<Array<Scalars['Int']>>;
  page: Maybe<Scalars['Int']>;
  perPage: Maybe<Scalars['Int']>;
};


export type IQueryCollectionArgs = {
  id: Scalars['Int'];
};


export type IQueryCollectionFromNameTypeUserArgs = {
  name: Scalars['String'];
  type: ICollectionType;
  user: Maybe<Scalars['Int']>;
};


export type IQueryInvitesArgs = {
  includeExpired: Maybe<Scalars['Boolean']>;
  includeUsed: Maybe<Scalars['Boolean']>;
  createdBy: Maybe<Scalars['Int']>;
  page: Maybe<Scalars['Int']>;
  perPage: Maybe<Scalars['Int']>;
};


export type IQueryInviteArgs = {
  id: Scalars['Int'];
};


export type IQueryPlaylistsArgs = {
  search: Maybe<Scalars['String']>;
  types: Maybe<Array<IPlaylistType>>;
  userIds: Maybe<Array<Scalars['Int']>>;
  page: Maybe<Scalars['Int']>;
  perPage: Maybe<Scalars['Int']>;
};


export type IQueryPlaylistArgs = {
  id: Scalars['Int'];
};


export type IQueryPlaylistFromNameTypeUserArgs = {
  name: Scalars['String'];
  type: IPlaylistType;
  user: Maybe<Scalars['Int']>;
};


export type IQueryReleasesArgs = {
  search: Maybe<Scalars['String']>;
  collectionIds: Maybe<Array<Scalars['Int']>>;
  artistIds: Maybe<Array<Scalars['Int']>>;
  releaseTypes: Maybe<Array<IReleaseType>>;
  years: Maybe<Array<Scalars['Int']>>;
  ratings: Maybe<Array<Scalars['Int']>>;
  page: Maybe<Scalars['Int']>;
  perPage: Maybe<Scalars['Int']>;
  sort: Maybe<IReleaseSort>;
  asc: Maybe<Scalars['Boolean']>;
};


export type IQueryReleaseArgs = {
  id: Scalars['Int'];
};


export type IQueryTracksArgs = {
  search: Maybe<Scalars['String']>;
  playlistIds: Maybe<Array<Scalars['Int']>>;
  artistIds: Maybe<Array<Scalars['Int']>>;
  years: Maybe<Array<Scalars['Int']>>;
  page: Maybe<Scalars['Int']>;
  perPage: Maybe<Scalars['Int']>;
  sort: Maybe<ITrackSort>;
  asc: Maybe<Scalars['Boolean']>;
};


export type IQueryTrackArgs = {
  id: Scalars['Int'];
};

export type IRelease = {
  __typename?: 'Release';
  id: Scalars['Int'];
  title: Scalars['String'];
  releaseType: IReleaseType;
  addedOn: Scalars['PosixTime'];
  inInbox: Scalars['Boolean'];
  inFavorites: Scalars['Boolean'];
  releaseYear: Maybe<Scalars['Int']>;
  /** The date that the release was released in YYYY-MM-DD format. */
  releaseDate: Maybe<Scalars['String']>;
  /** The release rating, either null or an int on the interval [1, 10]. */
  rating: Maybe<Scalars['Int']>;
  numTracks: Scalars['Int'];
  /** The total runtime (sum of track durations). */
  runtime: Scalars['Int'];
  /** The image ID of the release's cover image. */
  imageId: Maybe<Scalars['Int']>;
  artists: Array<IArtistWithRole>;
  tracks: Array<ITrack>;
  genres: Array<ICollection>;
  labels: Array<ICollection>;
  collages: Array<ICollection>;
};

export type IReleaseAndArtist = {
  __typename?: 'ReleaseAndArtist';
  release: IRelease;
  artist: IArtist;
};

export enum IReleaseSort {
  RecentlyAdded = 'RECENTLY_ADDED',
  Title = 'TITLE',
  Year = 'YEAR',
  Rating = 'RATING',
  Random = 'RANDOM',
  SearchRank = 'SEARCH_RANK'
}

export enum IReleaseType {
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

export type IReleases = {
  __typename?: 'Releases';
  /** The total number of releases matching the query across all pages. */
  total: Scalars['Int'];
  /** The releases on the current page. */
  results: Array<IRelease>;
};

export type IToken = {
  __typename?: 'Token';
  hex: Scalars['String'];
};

/** A type that represents the top genres of an artist/collection. */
export type ITopGenre = {
  __typename?: 'TopGenre';
  genre: ICollection;
  /** The number of releases in the artist/collection that match this genre. */
  numMatches: Scalars['Int'];
};

export type ITrack = {
  __typename?: 'Track';
  id: Scalars['Int'];
  title: Scalars['String'];
  duration: Scalars['Int'];
  trackNumber: Scalars['String'];
  discNumber: Scalars['String'];
  /** Whether the track is in the user's favorites playlist. */
  inFavorites: Scalars['Boolean'];
  release: IRelease;
  artists: Array<IArtistWithRole>;
};

export type ITrackAndArtist = {
  __typename?: 'TrackAndArtist';
  track: ITrack;
  trackArtist: IArtistWithRole;
};

export enum ITrackSort {
  RecentlyAdded = 'RECENTLY_ADDED',
  Title = 'TITLE',
  Year = 'YEAR',
  Random = 'RANDOM',
  SearchRank = 'SEARCH_RANK'
}

export type ITracks = {
  __typename?: 'Tracks';
  /** The total number of tracks matching the query across all pages. */
  total: Scalars['Int'];
  /** The tracks on the current page. */
  results: Array<ITrack>;
};

export type IUser = {
  __typename?: 'User';
  id: Scalars['Int'];
  nickname: Scalars['String'];
  inboxCollectionId: Scalars['Int'];
  favoritesCollectionId: Scalars['Int'];
  favoritesPlaylistId: Scalars['Int'];
};

export type IHeaderFetchUserQueryVariables = Exact<{ [key: string]: never; }>;


export type IHeaderFetchUserQuery = (
  { __typename?: 'Query' }
  & { user: (
    { __typename?: 'User' }
    & IUserFieldsFragment
  ) }
);

export type IPagedReleasesFetchReleasesQueryVariables = Exact<{
  search: Maybe<Scalars['String']>;
  collectionIds: Maybe<Array<Scalars['Int']> | Scalars['Int']>;
  artistIds: Maybe<Array<Scalars['Int']> | Scalars['Int']>;
  releaseTypes: Maybe<Array<IReleaseType> | IReleaseType>;
  years: Maybe<Array<Scalars['Int']> | Scalars['Int']>;
  ratings: Maybe<Array<Scalars['Int']> | Scalars['Int']>;
  page: Maybe<Scalars['Int']>;
  perPage: Maybe<Scalars['Int']>;
  sort: Maybe<IReleaseSort>;
  asc: Maybe<Scalars['Boolean']>;
}>;


export type IPagedReleasesFetchReleasesQuery = (
  { __typename?: 'Query' }
  & { releases: (
    { __typename?: 'Releases' }
    & Pick<IReleases, 'total'>
    & { results: Array<(
      { __typename?: 'Release' }
      & IReleaseFieldsFragment
    )> }
  ) }
);

export type IFavoritePlaylistsIdQueryVariables = Exact<{ [key: string]: never; }>;


export type IFavoritePlaylistsIdQuery = (
  { __typename?: 'Query' }
  & { user: (
    { __typename?: 'User' }
    & Pick<IUser, 'id' | 'favoritesPlaylistId'>
  ) }
);

export type IPlaylistsFavoriteTrackMutationVariables = Exact<{
  playlistId: Scalars['Int'];
  trackId: Scalars['Int'];
}>;


export type IPlaylistsFavoriteTrackMutation = (
  { __typename?: 'Mutation' }
  & { createPlaylistEntry: (
    { __typename?: 'PlaylistEntry' }
    & Pick<IPlaylistEntry, 'id'>
    & { playlist: (
      { __typename?: 'Playlist' }
      & Pick<IPlaylist, 'id' | 'numTracks'>
      & { entries: Array<(
        { __typename?: 'PlaylistEntry' }
        & Pick<IPlaylistEntry, 'id'>
      )> }
    ), track: (
      { __typename?: 'Track' }
      & Pick<ITrack, 'id' | 'inFavorites'>
    ) }
  ) }
);

export type IPlaylistsUnfavoriteTrackMutationVariables = Exact<{
  trackId: Scalars['Int'];
}>;


export type IPlaylistsUnfavoriteTrackMutation = (
  { __typename?: 'Mutation' }
  & { delPlaylistEntries: (
    { __typename?: 'PlaylistAndTrack' }
    & { playlist: (
      { __typename?: 'Playlist' }
      & Pick<IPlaylist, 'id' | 'numTracks'>
      & { entries: Array<(
        { __typename?: 'PlaylistEntry' }
        & Pick<IPlaylistEntry, 'id'>
      )> }
    ), track: (
      { __typename?: 'Track' }
      & Pick<ITrack, 'id' | 'inFavorites'>
    ) }
  ) }
);

export type IFetchCollectionsChooserQueryVariables = Exact<{
  types: Maybe<Array<ICollectionType> | ICollectionType>;
}>;


export type IFetchCollectionsChooserQuery = (
  { __typename?: 'Query' }
  & { collections: (
    { __typename?: 'Collections' }
    & { results: Array<(
      { __typename?: 'Collection' }
      & ICollectionFieldsFragment
    )> }
  ) }
);

export type IStarCollectionChooserMutationVariables = Exact<{
  id: Scalars['Int'];
}>;


export type IStarCollectionChooserMutation = (
  { __typename?: 'Mutation' }
  & { starCollection: (
    { __typename?: 'Collection' }
    & Pick<ICollection, 'id' | 'starred'>
  ) }
);

export type IUnstarCollectionChooserMutationVariables = Exact<{
  id: Scalars['Int'];
}>;


export type IUnstarCollectionChooserMutation = (
  { __typename?: 'Mutation' }
  & { unstarCollection: (
    { __typename?: 'Collection' }
    & Pick<ICollection, 'id' | 'starred'>
  ) }
);

export type IUserFieldsFragment = (
  { __typename?: 'User' }
  & Pick<IUser, 'id' | 'nickname'>
);

export type IReleaseFieldsFragment = (
  { __typename?: 'Release' }
  & Pick<IRelease, 'id' | 'title' | 'releaseType' | 'addedOn' | 'inInbox' | 'inFavorites' | 'releaseYear' | 'releaseDate' | 'rating' | 'numTracks' | 'runtime' | 'imageId'>
  & { artists: Array<(
    { __typename?: 'ArtistWithRole' }
    & Pick<IArtistWithRole, 'role'>
    & { artist: (
      { __typename?: 'Artist' }
      & Pick<IArtist, 'id' | 'name'>
    ) }
  )>, genres: Array<(
    { __typename?: 'Collection' }
    & Pick<ICollection, 'id' | 'name'>
  )> }
);

export type IArtistFieldsFragment = (
  { __typename?: 'Artist' }
  & Pick<IArtist, 'id' | 'name' | 'starred' | 'numReleases' | 'imageId'>
);

export type ICollectionFieldsFragment = (
  { __typename?: 'Collection' }
  & Pick<ICollection, 'id' | 'name' | 'starred' | 'type' | 'numReleases' | 'lastUpdatedOn' | 'imageId'>
  & { user: Maybe<(
    { __typename?: 'User' }
    & IUserFieldsFragment
  )> }
);

export type IInviteFieldsFragment = (
  { __typename?: 'Invite' }
  & Pick<IInvite, 'id' | 'code' | 'createdAt'>
  & { createdBy: (
    { __typename?: 'User' }
    & IUserFieldsFragment
  ), usedBy: Maybe<(
    { __typename?: 'User' }
    & IUserFieldsFragment
  )> }
);

export type IPlaylistFieldsFragment = (
  { __typename?: 'Playlist' }
  & Pick<IPlaylist, 'id' | 'name' | 'starred' | 'type' | 'numTracks' | 'lastUpdatedOn' | 'imageId'>
  & { user: Maybe<(
    { __typename?: 'User' }
    & IUserFieldsFragment
  )> }
);

export type ITrackFieldsFragment = (
  { __typename?: 'Track' }
  & Pick<ITrack, 'id' | 'title' | 'duration' | 'trackNumber' | 'discNumber' | 'inFavorites'>
  & { release: (
    { __typename?: 'Release' }
    & Pick<IRelease, 'id' | 'imageId'>
  ), artists: Array<(
    { __typename?: 'ArtistWithRole' }
    & Pick<IArtistWithRole, 'role'>
    & { artist: (
      { __typename?: 'Artist' }
      & Pick<IArtist, 'id' | 'name'>
    ) }
  )> }
);

export type IFullReleaseFieldsFragment = (
  { __typename?: 'Release' }
  & { collages: Array<(
    { __typename?: 'Collection' }
    & Pick<ICollection, 'id' | 'name'>
  )>, labels: Array<(
    { __typename?: 'Collection' }
    & Pick<ICollection, 'id' | 'name'>
  )>, tracks: Array<(
    { __typename?: 'Track' }
    & ITrackFieldsFragment
  )> }
  & IReleaseFieldsFragment
);

export type IArtistsFetchArtistQueryVariables = Exact<{
  id: Scalars['Int'];
}>;


export type IArtistsFetchArtistQuery = (
  { __typename?: 'Query' }
  & { artist: (
    { __typename?: 'Artist' }
    & IArtistFieldsFragment
  ) }
);

export type IFetchArtistsChooserQueryVariables = Exact<{ [key: string]: never; }>;


export type IFetchArtistsChooserQuery = (
  { __typename?: 'Query' }
  & { artists: (
    { __typename?: 'Artists' }
    & { results: Array<(
      { __typename?: 'Artist' }
      & IArtistFieldsFragment
    )> }
  ) }
);

export type IStarArtistChooserMutationVariables = Exact<{
  id: Scalars['Int'];
}>;


export type IStarArtistChooserMutation = (
  { __typename?: 'Mutation' }
  & { starArtist: (
    { __typename?: 'Artist' }
    & Pick<IArtist, 'id' | 'starred'>
  ) }
);

export type IUnstarArtistChooserMutationVariables = Exact<{
  id: Scalars['Int'];
}>;


export type IUnstarArtistChooserMutation = (
  { __typename?: 'Mutation' }
  & { unstarArtist: (
    { __typename?: 'Artist' }
    & Pick<IArtist, 'id' | 'starred'>
  ) }
);

export type ICollageFetchCollageQueryVariables = Exact<{
  id: Scalars['Int'];
}>;


export type ICollageFetchCollageQuery = (
  { __typename?: 'Query' }
  & { collection: (
    { __typename?: 'Collection' }
    & ICollectionFieldsFragment
  ) }
);

export type IRecentlyAddedFetchReleasesQueryVariables = Exact<{ [key: string]: never; }>;


export type IRecentlyAddedFetchReleasesQuery = (
  { __typename?: 'Query' }
  & { releases: (
    { __typename?: 'Releases' }
    & { results: Array<(
      { __typename?: 'Release' }
      & IReleaseFieldsFragment
    )> }
  ) }
);

export type IGenresFetchGenreQueryVariables = Exact<{
  id: Scalars['Int'];
}>;


export type IGenresFetchGenreQuery = (
  { __typename?: 'Query' }
  & { collection: (
    { __typename?: 'Collection' }
    & ICollectionFieldsFragment
  ) }
);

export type IInvitesFetchInvitesQueryVariables = Exact<{ [key: string]: never; }>;


export type IInvitesFetchInvitesQuery = (
  { __typename?: 'Query' }
  & { invites: (
    { __typename?: 'Invites' }
    & Pick<IInvites, 'total'>
    & { results: Array<(
      { __typename?: 'Invite' }
      & IInviteFieldsFragment
    )> }
  ) }
);

export type IInvitesCreateInviteMutationVariables = Exact<{ [key: string]: never; }>;


export type IInvitesCreateInviteMutation = (
  { __typename?: 'Mutation' }
  & { createInvite: (
    { __typename?: 'Invite' }
    & IInviteFieldsFragment
  ) }
);

export type ILabelFetchLabelQueryVariables = Exact<{
  id: Scalars['Int'];
}>;


export type ILabelFetchLabelQuery = (
  { __typename?: 'Query' }
  & { collection: (
    { __typename?: 'Collection' }
    & ICollectionFieldsFragment
  ) }
);

export type INowPlayingInfoFetchReleaseQueryVariables = Exact<{
  id: Scalars['Int'];
}>;


export type INowPlayingInfoFetchReleaseQuery = (
  { __typename?: 'Query' }
  & { release: (
    { __typename?: 'Release' }
    & IFullReleaseFieldsFragment
  ) }
);

export type IFetchPlaylistsChooserQueryVariables = Exact<{
  types: Maybe<Array<IPlaylistType> | IPlaylistType>;
}>;


export type IFetchPlaylistsChooserQuery = (
  { __typename?: 'Query' }
  & { playlists: (
    { __typename?: 'Playlists' }
    & { results: Array<(
      { __typename?: 'Playlist' }
      & IPlaylistFieldsFragment
    )> }
  ) }
);

export type IStarPlaylistChooserMutationVariables = Exact<{
  id: Scalars['Int'];
}>;


export type IStarPlaylistChooserMutation = (
  { __typename?: 'Mutation' }
  & { starPlaylist: (
    { __typename?: 'Playlist' }
    & Pick<IPlaylist, 'id' | 'starred'>
  ) }
);

export type IUnstarPlaylistChooserMutationVariables = Exact<{
  id: Scalars['Int'];
}>;


export type IUnstarPlaylistChooserMutation = (
  { __typename?: 'Mutation' }
  & { unstarPlaylist: (
    { __typename?: 'Playlist' }
    & Pick<IPlaylist, 'id' | 'starred'>
  ) }
);

export type IPlaylistsFetchPlaylistQueryVariables = Exact<{
  id: Scalars['Int'];
}>;


export type IPlaylistsFetchPlaylistQuery = (
  { __typename?: 'Query' }
  & { playlist: (
    { __typename?: 'Playlist' }
    & IPlaylistFieldsFragment
  ) }
);

export type IPlaylistsFetchTracksQueryVariables = Exact<{
  id: Scalars['Int'];
}>;


export type IPlaylistsFetchTracksQuery = (
  { __typename?: 'Query' }
  & { playlist: (
    { __typename?: 'Playlist' }
    & Pick<IPlaylist, 'id'>
    & { entries: Array<(
      { __typename?: 'PlaylistEntry' }
      & Pick<IPlaylistEntry, 'id'>
      & { track: (
        { __typename?: 'Track' }
        & ITrackFieldsFragment
      ) }
    )> }
  ) }
);

export type IInFavoritesFetchFavoritesIdQueryVariables = Exact<{ [key: string]: never; }>;


export type IInFavoritesFetchFavoritesIdQuery = (
  { __typename?: 'Query' }
  & { user: (
    { __typename?: 'User' }
    & Pick<IUser, 'id' | 'favoritesCollectionId'>
  ) }
);

export type IInFavoritesAddReleaseToCollectionMutationVariables = Exact<{
  collectionId: Scalars['Int'];
  releaseId: Scalars['Int'];
}>;


export type IInFavoritesAddReleaseToCollectionMutation = (
  { __typename?: 'Mutation' }
  & { addReleaseToCollection: (
    { __typename?: 'CollectionAndRelease' }
    & { collection: (
      { __typename?: 'Collection' }
      & Pick<ICollection, 'id' | 'numReleases' | 'lastUpdatedOn'>
    ), release: (
      { __typename?: 'Release' }
      & Pick<IRelease, 'id' | 'inInbox' | 'inFavorites'>
      & { genres: Array<(
        { __typename?: 'Collection' }
        & Pick<ICollection, 'id' | 'name'>
      )>, labels: Array<(
        { __typename?: 'Collection' }
        & Pick<ICollection, 'id' | 'name'>
      )>, collages: Array<(
        { __typename?: 'Collection' }
        & Pick<ICollection, 'id' | 'name'>
      )> }
    ) }
  ) }
);

export type IInFavoritesDelReleaseFromCollectionMutationVariables = Exact<{
  collectionId: Scalars['Int'];
  releaseId: Scalars['Int'];
}>;


export type IInFavoritesDelReleaseFromCollectionMutation = (
  { __typename?: 'Mutation' }
  & { delReleaseFromCollection: (
    { __typename?: 'CollectionAndRelease' }
    & { collection: (
      { __typename?: 'Collection' }
      & Pick<ICollection, 'id' | 'numReleases' | 'lastUpdatedOn'>
    ), release: (
      { __typename?: 'Release' }
      & Pick<IRelease, 'id' | 'inInbox' | 'inFavorites'>
      & { genres: Array<(
        { __typename?: 'Collection' }
        & Pick<ICollection, 'id' | 'name'>
      )>, labels: Array<(
        { __typename?: 'Collection' }
        & Pick<ICollection, 'id' | 'name'>
      )>, collages: Array<(
        { __typename?: 'Collection' }
        & Pick<ICollection, 'id' | 'name'>
      )> }
    ) }
  ) }
);

export type IInInboxFetchInboxIdQueryVariables = Exact<{ [key: string]: never; }>;


export type IInInboxFetchInboxIdQuery = (
  { __typename?: 'Query' }
  & { user: (
    { __typename?: 'User' }
    & Pick<IUser, 'id' | 'inboxCollectionId'>
  ) }
);

export type IInInboxAddReleaseToCollectionMutationVariables = Exact<{
  collectionId: Scalars['Int'];
  releaseId: Scalars['Int'];
}>;


export type IInInboxAddReleaseToCollectionMutation = (
  { __typename?: 'Mutation' }
  & { addReleaseToCollection: (
    { __typename?: 'CollectionAndRelease' }
    & { collection: (
      { __typename?: 'Collection' }
      & Pick<ICollection, 'id' | 'numReleases' | 'lastUpdatedOn'>
    ), release: (
      { __typename?: 'Release' }
      & Pick<IRelease, 'id' | 'inInbox' | 'inFavorites'>
      & { genres: Array<(
        { __typename?: 'Collection' }
        & Pick<ICollection, 'id' | 'name'>
      )>, labels: Array<(
        { __typename?: 'Collection' }
        & Pick<ICollection, 'id' | 'name'>
      )>, collages: Array<(
        { __typename?: 'Collection' }
        & Pick<ICollection, 'id' | 'name'>
      )> }
    ) }
  ) }
);

export type IInInboxDelReleaseFromCollectionMutationVariables = Exact<{
  collectionId: Scalars['Int'];
  releaseId: Scalars['Int'];
}>;


export type IInInboxDelReleaseFromCollectionMutation = (
  { __typename?: 'Mutation' }
  & { delReleaseFromCollection: (
    { __typename?: 'CollectionAndRelease' }
    & { collection: (
      { __typename?: 'Collection' }
      & Pick<ICollection, 'id' | 'numReleases' | 'lastUpdatedOn'>
    ), release: (
      { __typename?: 'Release' }
      & Pick<IRelease, 'id' | 'inInbox' | 'inFavorites'>
      & { genres: Array<(
        { __typename?: 'Collection' }
        & Pick<ICollection, 'id' | 'name'>
      )>, labels: Array<(
        { __typename?: 'Collection' }
        & Pick<ICollection, 'id' | 'name'>
      )>, collages: Array<(
        { __typename?: 'Collection' }
        & Pick<ICollection, 'id' | 'name'>
      )> }
    ) }
  ) }
);

export type IReleaseUpdateReleaseRatingMutationVariables = Exact<{
  id: Scalars['Int'];
  rating: Maybe<Scalars['Int']>;
}>;


export type IReleaseUpdateReleaseRatingMutation = (
  { __typename?: 'Mutation' }
  & { updateRelease: (
    { __typename?: 'Release' }
    & Pick<IRelease, 'id' | 'rating'>
  ) }
);

export type IReleaseFetchReleaseQueryVariables = Exact<{
  id: Scalars['Int'];
}>;


export type IReleaseFetchReleaseQuery = (
  { __typename?: 'Query' }
  & { release: (
    { __typename?: 'Release' }
    & IFullReleaseFieldsFragment
  ) }
);

export type ISettingsFetchUserQueryVariables = Exact<{ [key: string]: never; }>;


export type ISettingsFetchUserQuery = (
  { __typename?: 'Query' }
  & { user: (
    { __typename?: 'User' }
    & IUserFieldsFragment
  ) }
);

export type ISettingsUpdateUserMutationVariables = Exact<{
  nickname: Maybe<Scalars['String']>;
}>;


export type ISettingsUpdateUserMutation = (
  { __typename?: 'Mutation' }
  & { updateUser: (
    { __typename?: 'User' }
    & Pick<IUser, 'id' | 'nickname'>
  ) }
);

export type IYearsFetchReleaseYearsQueryVariables = Exact<{ [key: string]: never; }>;


export type IYearsFetchReleaseYearsQuery = (
  { __typename?: 'Query' }
  & Pick<IQuery, 'releaseYears'>
);

export const ArtistFieldsFragmentDoc = gql`
    fragment ArtistFields on Artist {
  id
  name
  starred
  numReleases
  imageId
}
    `;
export const UserFieldsFragmentDoc = gql`
    fragment UserFields on User {
  id
  nickname
}
    `;
export const CollectionFieldsFragmentDoc = gql`
    fragment CollectionFields on Collection {
  id
  name
  starred
  type
  numReleases
  lastUpdatedOn
  imageId
  user {
    ...UserFields
  }
}
    ${UserFieldsFragmentDoc}`;
export const InviteFieldsFragmentDoc = gql`
    fragment InviteFields on Invite {
  id
  code
  createdBy {
    ...UserFields
  }
  createdAt
  usedBy {
    ...UserFields
  }
}
    ${UserFieldsFragmentDoc}`;
export const PlaylistFieldsFragmentDoc = gql`
    fragment PlaylistFields on Playlist {
  id
  name
  starred
  type
  numTracks
  lastUpdatedOn
  imageId
  user {
    ...UserFields
  }
}
    ${UserFieldsFragmentDoc}`;
export const ReleaseFieldsFragmentDoc = gql`
    fragment ReleaseFields on Release {
  id
  title
  releaseType
  addedOn
  inInbox
  inFavorites
  releaseYear
  releaseDate
  rating
  numTracks
  runtime
  imageId
  artists {
    artist {
      id
      name
    }
    role
  }
  genres {
    id
    name
  }
}
    `;
export const TrackFieldsFragmentDoc = gql`
    fragment TrackFields on Track {
  id
  title
  duration
  trackNumber
  discNumber
  inFavorites
  release {
    id
    imageId
  }
  artists {
    artist {
      id
      name
    }
    role
  }
}
    `;
export const FullReleaseFieldsFragmentDoc = gql`
    fragment FullReleaseFields on Release {
  ...ReleaseFields
  collages {
    id
    name
  }
  labels {
    id
    name
  }
  tracks {
    ...TrackFields
  }
}
    ${ReleaseFieldsFragmentDoc}
${TrackFieldsFragmentDoc}`;
export const HeaderFetchUserDocument = gql`
    query HeaderFetchUser {
  user {
    ...UserFields
  }
}
    ${UserFieldsFragmentDoc}`;

/**
 * __useHeaderFetchUserQuery__
 *
 * To run a query within a React component, call `useHeaderFetchUserQuery` and pass it any options that fit your needs.
 * When your component renders, `useHeaderFetchUserQuery` returns an object from Apollo Client that contains loading, error, and data properties
 * you can use to render your UI.
 *
 * @param baseOptions options that will be passed into the query, supported options are listed on: https://www.apollographql.com/docs/react/api/react-hooks/#options;
 *
 * @example
 * const { data, loading, error } = useHeaderFetchUserQuery({
 *   variables: {
 *   },
 * });
 */
export function useHeaderFetchUserQuery(baseOptions?: Apollo.QueryHookOptions<IHeaderFetchUserQuery, IHeaderFetchUserQueryVariables>) {
        const options = {...defaultOptions, ...baseOptions}
        return Apollo.useQuery<IHeaderFetchUserQuery, IHeaderFetchUserQueryVariables>(HeaderFetchUserDocument, options);
      }
export function useHeaderFetchUserLazyQuery(baseOptions?: Apollo.LazyQueryHookOptions<IHeaderFetchUserQuery, IHeaderFetchUserQueryVariables>) {
          const options = {...defaultOptions, ...baseOptions}
          return Apollo.useLazyQuery<IHeaderFetchUserQuery, IHeaderFetchUserQueryVariables>(HeaderFetchUserDocument, options);
        }
export type HeaderFetchUserQueryHookResult = ReturnType<typeof useHeaderFetchUserQuery>;
export type HeaderFetchUserLazyQueryHookResult = ReturnType<typeof useHeaderFetchUserLazyQuery>;
export type HeaderFetchUserQueryResult = Apollo.QueryResult<IHeaderFetchUserQuery, IHeaderFetchUserQueryVariables>;
export function refetchHeaderFetchUserQuery(variables?: IHeaderFetchUserQueryVariables) {
      return { query: HeaderFetchUserDocument, variables: variables }
    }
export const PagedReleasesFetchReleasesDocument = gql`
    query PagedReleasesFetchReleases($search: String, $collectionIds: [Int!], $artistIds: [Int!], $releaseTypes: [ReleaseType!], $years: [Int!], $ratings: [Int!], $page: Int, $perPage: Int, $sort: ReleaseSort, $asc: Boolean) {
  releases(
    search: $search
    collectionIds: $collectionIds
    artistIds: $artistIds
    releaseTypes: $releaseTypes
    years: $years
    ratings: $ratings
    page: $page
    perPage: $perPage
    sort: $sort
    asc: $asc
  ) {
    total
    results {
      ...ReleaseFields
    }
  }
}
    ${ReleaseFieldsFragmentDoc}`;

/**
 * __usePagedReleasesFetchReleasesQuery__
 *
 * To run a query within a React component, call `usePagedReleasesFetchReleasesQuery` and pass it any options that fit your needs.
 * When your component renders, `usePagedReleasesFetchReleasesQuery` returns an object from Apollo Client that contains loading, error, and data properties
 * you can use to render your UI.
 *
 * @param baseOptions options that will be passed into the query, supported options are listed on: https://www.apollographql.com/docs/react/api/react-hooks/#options;
 *
 * @example
 * const { data, loading, error } = usePagedReleasesFetchReleasesQuery({
 *   variables: {
 *      search: // value for 'search'
 *      collectionIds: // value for 'collectionIds'
 *      artistIds: // value for 'artistIds'
 *      releaseTypes: // value for 'releaseTypes'
 *      years: // value for 'years'
 *      ratings: // value for 'ratings'
 *      page: // value for 'page'
 *      perPage: // value for 'perPage'
 *      sort: // value for 'sort'
 *      asc: // value for 'asc'
 *   },
 * });
 */
export function usePagedReleasesFetchReleasesQuery(baseOptions?: Apollo.QueryHookOptions<IPagedReleasesFetchReleasesQuery, IPagedReleasesFetchReleasesQueryVariables>) {
        const options = {...defaultOptions, ...baseOptions}
        return Apollo.useQuery<IPagedReleasesFetchReleasesQuery, IPagedReleasesFetchReleasesQueryVariables>(PagedReleasesFetchReleasesDocument, options);
      }
export function usePagedReleasesFetchReleasesLazyQuery(baseOptions?: Apollo.LazyQueryHookOptions<IPagedReleasesFetchReleasesQuery, IPagedReleasesFetchReleasesQueryVariables>) {
          const options = {...defaultOptions, ...baseOptions}
          return Apollo.useLazyQuery<IPagedReleasesFetchReleasesQuery, IPagedReleasesFetchReleasesQueryVariables>(PagedReleasesFetchReleasesDocument, options);
        }
export type PagedReleasesFetchReleasesQueryHookResult = ReturnType<typeof usePagedReleasesFetchReleasesQuery>;
export type PagedReleasesFetchReleasesLazyQueryHookResult = ReturnType<typeof usePagedReleasesFetchReleasesLazyQuery>;
export type PagedReleasesFetchReleasesQueryResult = Apollo.QueryResult<IPagedReleasesFetchReleasesQuery, IPagedReleasesFetchReleasesQueryVariables>;
export function refetchPagedReleasesFetchReleasesQuery(variables?: IPagedReleasesFetchReleasesQueryVariables) {
      return { query: PagedReleasesFetchReleasesDocument, variables: variables }
    }
export const FavoritePlaylistsIdDocument = gql`
    query FavoritePlaylistsId {
  user {
    id
    favoritesPlaylistId
  }
}
    `;

/**
 * __useFavoritePlaylistsIdQuery__
 *
 * To run a query within a React component, call `useFavoritePlaylistsIdQuery` and pass it any options that fit your needs.
 * When your component renders, `useFavoritePlaylistsIdQuery` returns an object from Apollo Client that contains loading, error, and data properties
 * you can use to render your UI.
 *
 * @param baseOptions options that will be passed into the query, supported options are listed on: https://www.apollographql.com/docs/react/api/react-hooks/#options;
 *
 * @example
 * const { data, loading, error } = useFavoritePlaylistsIdQuery({
 *   variables: {
 *   },
 * });
 */
export function useFavoritePlaylistsIdQuery(baseOptions?: Apollo.QueryHookOptions<IFavoritePlaylistsIdQuery, IFavoritePlaylistsIdQueryVariables>) {
        const options = {...defaultOptions, ...baseOptions}
        return Apollo.useQuery<IFavoritePlaylistsIdQuery, IFavoritePlaylistsIdQueryVariables>(FavoritePlaylistsIdDocument, options);
      }
export function useFavoritePlaylistsIdLazyQuery(baseOptions?: Apollo.LazyQueryHookOptions<IFavoritePlaylistsIdQuery, IFavoritePlaylistsIdQueryVariables>) {
          const options = {...defaultOptions, ...baseOptions}
          return Apollo.useLazyQuery<IFavoritePlaylistsIdQuery, IFavoritePlaylistsIdQueryVariables>(FavoritePlaylistsIdDocument, options);
        }
export type FavoritePlaylistsIdQueryHookResult = ReturnType<typeof useFavoritePlaylistsIdQuery>;
export type FavoritePlaylistsIdLazyQueryHookResult = ReturnType<typeof useFavoritePlaylistsIdLazyQuery>;
export type FavoritePlaylistsIdQueryResult = Apollo.QueryResult<IFavoritePlaylistsIdQuery, IFavoritePlaylistsIdQueryVariables>;
export function refetchFavoritePlaylistsIdQuery(variables?: IFavoritePlaylistsIdQueryVariables) {
      return { query: FavoritePlaylistsIdDocument, variables: variables }
    }
export const PlaylistsFavoriteTrackDocument = gql`
    mutation PlaylistsFavoriteTrack($playlistId: Int!, $trackId: Int!) {
  createPlaylistEntry(playlistId: $playlistId, trackId: $trackId) {
    id
    playlist {
      id
      numTracks
      entries {
        id
      }
    }
    track {
      id
      inFavorites
    }
  }
}
    `;
export type IPlaylistsFavoriteTrackMutationFn = Apollo.MutationFunction<IPlaylistsFavoriteTrackMutation, IPlaylistsFavoriteTrackMutationVariables>;

/**
 * __usePlaylistsFavoriteTrackMutation__
 *
 * To run a mutation, you first call `usePlaylistsFavoriteTrackMutation` within a React component and pass it any options that fit your needs.
 * When your component renders, `usePlaylistsFavoriteTrackMutation` returns a tuple that includes:
 * - A mutate function that you can call at any time to execute the mutation
 * - An object with fields that represent the current status of the mutation's execution
 *
 * @param baseOptions options that will be passed into the mutation, supported options are listed on: https://www.apollographql.com/docs/react/api/react-hooks/#options-2;
 *
 * @example
 * const [playlistsFavoriteTrackMutation, { data, loading, error }] = usePlaylistsFavoriteTrackMutation({
 *   variables: {
 *      playlistId: // value for 'playlistId'
 *      trackId: // value for 'trackId'
 *   },
 * });
 */
export function usePlaylistsFavoriteTrackMutation(baseOptions?: Apollo.MutationHookOptions<IPlaylistsFavoriteTrackMutation, IPlaylistsFavoriteTrackMutationVariables>) {
        const options = {...defaultOptions, ...baseOptions}
        return Apollo.useMutation<IPlaylistsFavoriteTrackMutation, IPlaylistsFavoriteTrackMutationVariables>(PlaylistsFavoriteTrackDocument, options);
      }
export type PlaylistsFavoriteTrackMutationHookResult = ReturnType<typeof usePlaylistsFavoriteTrackMutation>;
export type PlaylistsFavoriteTrackMutationResult = Apollo.MutationResult<IPlaylistsFavoriteTrackMutation>;
export type PlaylistsFavoriteTrackMutationOptions = Apollo.BaseMutationOptions<IPlaylistsFavoriteTrackMutation, IPlaylistsFavoriteTrackMutationVariables>;
export const PlaylistsUnfavoriteTrackDocument = gql`
    mutation PlaylistsUnfavoriteTrack($trackId: Int!) {
  delPlaylistEntries(playlistId: 1, trackId: $trackId) {
    playlist {
      id
      numTracks
      entries {
        id
      }
    }
    track {
      id
      inFavorites
    }
  }
}
    `;
export type IPlaylistsUnfavoriteTrackMutationFn = Apollo.MutationFunction<IPlaylistsUnfavoriteTrackMutation, IPlaylistsUnfavoriteTrackMutationVariables>;

/**
 * __usePlaylistsUnfavoriteTrackMutation__
 *
 * To run a mutation, you first call `usePlaylistsUnfavoriteTrackMutation` within a React component and pass it any options that fit your needs.
 * When your component renders, `usePlaylistsUnfavoriteTrackMutation` returns a tuple that includes:
 * - A mutate function that you can call at any time to execute the mutation
 * - An object with fields that represent the current status of the mutation's execution
 *
 * @param baseOptions options that will be passed into the mutation, supported options are listed on: https://www.apollographql.com/docs/react/api/react-hooks/#options-2;
 *
 * @example
 * const [playlistsUnfavoriteTrackMutation, { data, loading, error }] = usePlaylistsUnfavoriteTrackMutation({
 *   variables: {
 *      trackId: // value for 'trackId'
 *   },
 * });
 */
export function usePlaylistsUnfavoriteTrackMutation(baseOptions?: Apollo.MutationHookOptions<IPlaylistsUnfavoriteTrackMutation, IPlaylistsUnfavoriteTrackMutationVariables>) {
        const options = {...defaultOptions, ...baseOptions}
        return Apollo.useMutation<IPlaylistsUnfavoriteTrackMutation, IPlaylistsUnfavoriteTrackMutationVariables>(PlaylistsUnfavoriteTrackDocument, options);
      }
export type PlaylistsUnfavoriteTrackMutationHookResult = ReturnType<typeof usePlaylistsUnfavoriteTrackMutation>;
export type PlaylistsUnfavoriteTrackMutationResult = Apollo.MutationResult<IPlaylistsUnfavoriteTrackMutation>;
export type PlaylistsUnfavoriteTrackMutationOptions = Apollo.BaseMutationOptions<IPlaylistsUnfavoriteTrackMutation, IPlaylistsUnfavoriteTrackMutationVariables>;
export const FetchCollectionsChooserDocument = gql`
    query FetchCollectionsChooser($types: [CollectionType!]) {
  collections(types: $types) {
    results {
      ...CollectionFields
    }
  }
}
    ${CollectionFieldsFragmentDoc}`;

/**
 * __useFetchCollectionsChooserQuery__
 *
 * To run a query within a React component, call `useFetchCollectionsChooserQuery` and pass it any options that fit your needs.
 * When your component renders, `useFetchCollectionsChooserQuery` returns an object from Apollo Client that contains loading, error, and data properties
 * you can use to render your UI.
 *
 * @param baseOptions options that will be passed into the query, supported options are listed on: https://www.apollographql.com/docs/react/api/react-hooks/#options;
 *
 * @example
 * const { data, loading, error } = useFetchCollectionsChooserQuery({
 *   variables: {
 *      types: // value for 'types'
 *   },
 * });
 */
export function useFetchCollectionsChooserQuery(baseOptions?: Apollo.QueryHookOptions<IFetchCollectionsChooserQuery, IFetchCollectionsChooserQueryVariables>) {
        const options = {...defaultOptions, ...baseOptions}
        return Apollo.useQuery<IFetchCollectionsChooserQuery, IFetchCollectionsChooserQueryVariables>(FetchCollectionsChooserDocument, options);
      }
export function useFetchCollectionsChooserLazyQuery(baseOptions?: Apollo.LazyQueryHookOptions<IFetchCollectionsChooserQuery, IFetchCollectionsChooserQueryVariables>) {
          const options = {...defaultOptions, ...baseOptions}
          return Apollo.useLazyQuery<IFetchCollectionsChooserQuery, IFetchCollectionsChooserQueryVariables>(FetchCollectionsChooserDocument, options);
        }
export type FetchCollectionsChooserQueryHookResult = ReturnType<typeof useFetchCollectionsChooserQuery>;
export type FetchCollectionsChooserLazyQueryHookResult = ReturnType<typeof useFetchCollectionsChooserLazyQuery>;
export type FetchCollectionsChooserQueryResult = Apollo.QueryResult<IFetchCollectionsChooserQuery, IFetchCollectionsChooserQueryVariables>;
export function refetchFetchCollectionsChooserQuery(variables?: IFetchCollectionsChooserQueryVariables) {
      return { query: FetchCollectionsChooserDocument, variables: variables }
    }
export const StarCollectionChooserDocument = gql`
    mutation StarCollectionChooser($id: Int!) {
  starCollection(id: $id) {
    id
    starred
  }
}
    `;
export type IStarCollectionChooserMutationFn = Apollo.MutationFunction<IStarCollectionChooserMutation, IStarCollectionChooserMutationVariables>;

/**
 * __useStarCollectionChooserMutation__
 *
 * To run a mutation, you first call `useStarCollectionChooserMutation` within a React component and pass it any options that fit your needs.
 * When your component renders, `useStarCollectionChooserMutation` returns a tuple that includes:
 * - A mutate function that you can call at any time to execute the mutation
 * - An object with fields that represent the current status of the mutation's execution
 *
 * @param baseOptions options that will be passed into the mutation, supported options are listed on: https://www.apollographql.com/docs/react/api/react-hooks/#options-2;
 *
 * @example
 * const [starCollectionChooserMutation, { data, loading, error }] = useStarCollectionChooserMutation({
 *   variables: {
 *      id: // value for 'id'
 *   },
 * });
 */
export function useStarCollectionChooserMutation(baseOptions?: Apollo.MutationHookOptions<IStarCollectionChooserMutation, IStarCollectionChooserMutationVariables>) {
        const options = {...defaultOptions, ...baseOptions}
        return Apollo.useMutation<IStarCollectionChooserMutation, IStarCollectionChooserMutationVariables>(StarCollectionChooserDocument, options);
      }
export type StarCollectionChooserMutationHookResult = ReturnType<typeof useStarCollectionChooserMutation>;
export type StarCollectionChooserMutationResult = Apollo.MutationResult<IStarCollectionChooserMutation>;
export type StarCollectionChooserMutationOptions = Apollo.BaseMutationOptions<IStarCollectionChooserMutation, IStarCollectionChooserMutationVariables>;
export const UnstarCollectionChooserDocument = gql`
    mutation UnstarCollectionChooser($id: Int!) {
  unstarCollection(id: $id) {
    id
    starred
  }
}
    `;
export type IUnstarCollectionChooserMutationFn = Apollo.MutationFunction<IUnstarCollectionChooserMutation, IUnstarCollectionChooserMutationVariables>;

/**
 * __useUnstarCollectionChooserMutation__
 *
 * To run a mutation, you first call `useUnstarCollectionChooserMutation` within a React component and pass it any options that fit your needs.
 * When your component renders, `useUnstarCollectionChooserMutation` returns a tuple that includes:
 * - A mutate function that you can call at any time to execute the mutation
 * - An object with fields that represent the current status of the mutation's execution
 *
 * @param baseOptions options that will be passed into the mutation, supported options are listed on: https://www.apollographql.com/docs/react/api/react-hooks/#options-2;
 *
 * @example
 * const [unstarCollectionChooserMutation, { data, loading, error }] = useUnstarCollectionChooserMutation({
 *   variables: {
 *      id: // value for 'id'
 *   },
 * });
 */
export function useUnstarCollectionChooserMutation(baseOptions?: Apollo.MutationHookOptions<IUnstarCollectionChooserMutation, IUnstarCollectionChooserMutationVariables>) {
        const options = {...defaultOptions, ...baseOptions}
        return Apollo.useMutation<IUnstarCollectionChooserMutation, IUnstarCollectionChooserMutationVariables>(UnstarCollectionChooserDocument, options);
      }
export type UnstarCollectionChooserMutationHookResult = ReturnType<typeof useUnstarCollectionChooserMutation>;
export type UnstarCollectionChooserMutationResult = Apollo.MutationResult<IUnstarCollectionChooserMutation>;
export type UnstarCollectionChooserMutationOptions = Apollo.BaseMutationOptions<IUnstarCollectionChooserMutation, IUnstarCollectionChooserMutationVariables>;
export const ArtistsFetchArtistDocument = gql`
    query ArtistsFetchArtist($id: Int!) {
  artist(id: $id) {
    ...ArtistFields
  }
}
    ${ArtistFieldsFragmentDoc}`;

/**
 * __useArtistsFetchArtistQuery__
 *
 * To run a query within a React component, call `useArtistsFetchArtistQuery` and pass it any options that fit your needs.
 * When your component renders, `useArtistsFetchArtistQuery` returns an object from Apollo Client that contains loading, error, and data properties
 * you can use to render your UI.
 *
 * @param baseOptions options that will be passed into the query, supported options are listed on: https://www.apollographql.com/docs/react/api/react-hooks/#options;
 *
 * @example
 * const { data, loading, error } = useArtistsFetchArtistQuery({
 *   variables: {
 *      id: // value for 'id'
 *   },
 * });
 */
export function useArtistsFetchArtistQuery(baseOptions: Apollo.QueryHookOptions<IArtistsFetchArtistQuery, IArtistsFetchArtistQueryVariables>) {
        const options = {...defaultOptions, ...baseOptions}
        return Apollo.useQuery<IArtistsFetchArtistQuery, IArtistsFetchArtistQueryVariables>(ArtistsFetchArtistDocument, options);
      }
export function useArtistsFetchArtistLazyQuery(baseOptions?: Apollo.LazyQueryHookOptions<IArtistsFetchArtistQuery, IArtistsFetchArtistQueryVariables>) {
          const options = {...defaultOptions, ...baseOptions}
          return Apollo.useLazyQuery<IArtistsFetchArtistQuery, IArtistsFetchArtistQueryVariables>(ArtistsFetchArtistDocument, options);
        }
export type ArtistsFetchArtistQueryHookResult = ReturnType<typeof useArtistsFetchArtistQuery>;
export type ArtistsFetchArtistLazyQueryHookResult = ReturnType<typeof useArtistsFetchArtistLazyQuery>;
export type ArtistsFetchArtistQueryResult = Apollo.QueryResult<IArtistsFetchArtistQuery, IArtistsFetchArtistQueryVariables>;
export function refetchArtistsFetchArtistQuery(variables?: IArtistsFetchArtistQueryVariables) {
      return { query: ArtistsFetchArtistDocument, variables: variables }
    }
export const FetchArtistsChooserDocument = gql`
    query FetchArtistsChooser {
  artists {
    results {
      ...ArtistFields
    }
  }
}
    ${ArtistFieldsFragmentDoc}`;

/**
 * __useFetchArtistsChooserQuery__
 *
 * To run a query within a React component, call `useFetchArtistsChooserQuery` and pass it any options that fit your needs.
 * When your component renders, `useFetchArtistsChooserQuery` returns an object from Apollo Client that contains loading, error, and data properties
 * you can use to render your UI.
 *
 * @param baseOptions options that will be passed into the query, supported options are listed on: https://www.apollographql.com/docs/react/api/react-hooks/#options;
 *
 * @example
 * const { data, loading, error } = useFetchArtistsChooserQuery({
 *   variables: {
 *   },
 * });
 */
export function useFetchArtistsChooserQuery(baseOptions?: Apollo.QueryHookOptions<IFetchArtistsChooserQuery, IFetchArtistsChooserQueryVariables>) {
        const options = {...defaultOptions, ...baseOptions}
        return Apollo.useQuery<IFetchArtistsChooserQuery, IFetchArtistsChooserQueryVariables>(FetchArtistsChooserDocument, options);
      }
export function useFetchArtistsChooserLazyQuery(baseOptions?: Apollo.LazyQueryHookOptions<IFetchArtistsChooserQuery, IFetchArtistsChooserQueryVariables>) {
          const options = {...defaultOptions, ...baseOptions}
          return Apollo.useLazyQuery<IFetchArtistsChooserQuery, IFetchArtistsChooserQueryVariables>(FetchArtistsChooserDocument, options);
        }
export type FetchArtistsChooserQueryHookResult = ReturnType<typeof useFetchArtistsChooserQuery>;
export type FetchArtistsChooserLazyQueryHookResult = ReturnType<typeof useFetchArtistsChooserLazyQuery>;
export type FetchArtistsChooserQueryResult = Apollo.QueryResult<IFetchArtistsChooserQuery, IFetchArtistsChooserQueryVariables>;
export function refetchFetchArtistsChooserQuery(variables?: IFetchArtistsChooserQueryVariables) {
      return { query: FetchArtistsChooserDocument, variables: variables }
    }
export const StarArtistChooserDocument = gql`
    mutation StarArtistChooser($id: Int!) {
  starArtist(id: $id) {
    id
    starred
  }
}
    `;
export type IStarArtistChooserMutationFn = Apollo.MutationFunction<IStarArtistChooserMutation, IStarArtistChooserMutationVariables>;

/**
 * __useStarArtistChooserMutation__
 *
 * To run a mutation, you first call `useStarArtistChooserMutation` within a React component and pass it any options that fit your needs.
 * When your component renders, `useStarArtistChooserMutation` returns a tuple that includes:
 * - A mutate function that you can call at any time to execute the mutation
 * - An object with fields that represent the current status of the mutation's execution
 *
 * @param baseOptions options that will be passed into the mutation, supported options are listed on: https://www.apollographql.com/docs/react/api/react-hooks/#options-2;
 *
 * @example
 * const [starArtistChooserMutation, { data, loading, error }] = useStarArtistChooserMutation({
 *   variables: {
 *      id: // value for 'id'
 *   },
 * });
 */
export function useStarArtistChooserMutation(baseOptions?: Apollo.MutationHookOptions<IStarArtistChooserMutation, IStarArtistChooserMutationVariables>) {
        const options = {...defaultOptions, ...baseOptions}
        return Apollo.useMutation<IStarArtistChooserMutation, IStarArtistChooserMutationVariables>(StarArtistChooserDocument, options);
      }
export type StarArtistChooserMutationHookResult = ReturnType<typeof useStarArtistChooserMutation>;
export type StarArtistChooserMutationResult = Apollo.MutationResult<IStarArtistChooserMutation>;
export type StarArtistChooserMutationOptions = Apollo.BaseMutationOptions<IStarArtistChooserMutation, IStarArtistChooserMutationVariables>;
export const UnstarArtistChooserDocument = gql`
    mutation UnstarArtistChooser($id: Int!) {
  unstarArtist(id: $id) {
    id
    starred
  }
}
    `;
export type IUnstarArtistChooserMutationFn = Apollo.MutationFunction<IUnstarArtistChooserMutation, IUnstarArtistChooserMutationVariables>;

/**
 * __useUnstarArtistChooserMutation__
 *
 * To run a mutation, you first call `useUnstarArtistChooserMutation` within a React component and pass it any options that fit your needs.
 * When your component renders, `useUnstarArtistChooserMutation` returns a tuple that includes:
 * - A mutate function that you can call at any time to execute the mutation
 * - An object with fields that represent the current status of the mutation's execution
 *
 * @param baseOptions options that will be passed into the mutation, supported options are listed on: https://www.apollographql.com/docs/react/api/react-hooks/#options-2;
 *
 * @example
 * const [unstarArtistChooserMutation, { data, loading, error }] = useUnstarArtistChooserMutation({
 *   variables: {
 *      id: // value for 'id'
 *   },
 * });
 */
export function useUnstarArtistChooserMutation(baseOptions?: Apollo.MutationHookOptions<IUnstarArtistChooserMutation, IUnstarArtistChooserMutationVariables>) {
        const options = {...defaultOptions, ...baseOptions}
        return Apollo.useMutation<IUnstarArtistChooserMutation, IUnstarArtistChooserMutationVariables>(UnstarArtistChooserDocument, options);
      }
export type UnstarArtistChooserMutationHookResult = ReturnType<typeof useUnstarArtistChooserMutation>;
export type UnstarArtistChooserMutationResult = Apollo.MutationResult<IUnstarArtistChooserMutation>;
export type UnstarArtistChooserMutationOptions = Apollo.BaseMutationOptions<IUnstarArtistChooserMutation, IUnstarArtistChooserMutationVariables>;
export const CollageFetchCollageDocument = gql`
    query CollageFetchCollage($id: Int!) {
  collection(id: $id) {
    ...CollectionFields
  }
}
    ${CollectionFieldsFragmentDoc}`;

/**
 * __useCollageFetchCollageQuery__
 *
 * To run a query within a React component, call `useCollageFetchCollageQuery` and pass it any options that fit your needs.
 * When your component renders, `useCollageFetchCollageQuery` returns an object from Apollo Client that contains loading, error, and data properties
 * you can use to render your UI.
 *
 * @param baseOptions options that will be passed into the query, supported options are listed on: https://www.apollographql.com/docs/react/api/react-hooks/#options;
 *
 * @example
 * const { data, loading, error } = useCollageFetchCollageQuery({
 *   variables: {
 *      id: // value for 'id'
 *   },
 * });
 */
export function useCollageFetchCollageQuery(baseOptions: Apollo.QueryHookOptions<ICollageFetchCollageQuery, ICollageFetchCollageQueryVariables>) {
        const options = {...defaultOptions, ...baseOptions}
        return Apollo.useQuery<ICollageFetchCollageQuery, ICollageFetchCollageQueryVariables>(CollageFetchCollageDocument, options);
      }
export function useCollageFetchCollageLazyQuery(baseOptions?: Apollo.LazyQueryHookOptions<ICollageFetchCollageQuery, ICollageFetchCollageQueryVariables>) {
          const options = {...defaultOptions, ...baseOptions}
          return Apollo.useLazyQuery<ICollageFetchCollageQuery, ICollageFetchCollageQueryVariables>(CollageFetchCollageDocument, options);
        }
export type CollageFetchCollageQueryHookResult = ReturnType<typeof useCollageFetchCollageQuery>;
export type CollageFetchCollageLazyQueryHookResult = ReturnType<typeof useCollageFetchCollageLazyQuery>;
export type CollageFetchCollageQueryResult = Apollo.QueryResult<ICollageFetchCollageQuery, ICollageFetchCollageQueryVariables>;
export function refetchCollageFetchCollageQuery(variables?: ICollageFetchCollageQueryVariables) {
      return { query: CollageFetchCollageDocument, variables: variables }
    }
export const RecentlyAddedFetchReleasesDocument = gql`
    query RecentlyAddedFetchReleases {
  releases(sort: RECENTLY_ADDED, asc: false, page: 1, perPage: 10) {
    results {
      ...ReleaseFields
    }
  }
}
    ${ReleaseFieldsFragmentDoc}`;

/**
 * __useRecentlyAddedFetchReleasesQuery__
 *
 * To run a query within a React component, call `useRecentlyAddedFetchReleasesQuery` and pass it any options that fit your needs.
 * When your component renders, `useRecentlyAddedFetchReleasesQuery` returns an object from Apollo Client that contains loading, error, and data properties
 * you can use to render your UI.
 *
 * @param baseOptions options that will be passed into the query, supported options are listed on: https://www.apollographql.com/docs/react/api/react-hooks/#options;
 *
 * @example
 * const { data, loading, error } = useRecentlyAddedFetchReleasesQuery({
 *   variables: {
 *   },
 * });
 */
export function useRecentlyAddedFetchReleasesQuery(baseOptions?: Apollo.QueryHookOptions<IRecentlyAddedFetchReleasesQuery, IRecentlyAddedFetchReleasesQueryVariables>) {
        const options = {...defaultOptions, ...baseOptions}
        return Apollo.useQuery<IRecentlyAddedFetchReleasesQuery, IRecentlyAddedFetchReleasesQueryVariables>(RecentlyAddedFetchReleasesDocument, options);
      }
export function useRecentlyAddedFetchReleasesLazyQuery(baseOptions?: Apollo.LazyQueryHookOptions<IRecentlyAddedFetchReleasesQuery, IRecentlyAddedFetchReleasesQueryVariables>) {
          const options = {...defaultOptions, ...baseOptions}
          return Apollo.useLazyQuery<IRecentlyAddedFetchReleasesQuery, IRecentlyAddedFetchReleasesQueryVariables>(RecentlyAddedFetchReleasesDocument, options);
        }
export type RecentlyAddedFetchReleasesQueryHookResult = ReturnType<typeof useRecentlyAddedFetchReleasesQuery>;
export type RecentlyAddedFetchReleasesLazyQueryHookResult = ReturnType<typeof useRecentlyAddedFetchReleasesLazyQuery>;
export type RecentlyAddedFetchReleasesQueryResult = Apollo.QueryResult<IRecentlyAddedFetchReleasesQuery, IRecentlyAddedFetchReleasesQueryVariables>;
export function refetchRecentlyAddedFetchReleasesQuery(variables?: IRecentlyAddedFetchReleasesQueryVariables) {
      return { query: RecentlyAddedFetchReleasesDocument, variables: variables }
    }
export const GenresFetchGenreDocument = gql`
    query GenresFetchGenre($id: Int!) {
  collection(id: $id) {
    ...CollectionFields
  }
}
    ${CollectionFieldsFragmentDoc}`;

/**
 * __useGenresFetchGenreQuery__
 *
 * To run a query within a React component, call `useGenresFetchGenreQuery` and pass it any options that fit your needs.
 * When your component renders, `useGenresFetchGenreQuery` returns an object from Apollo Client that contains loading, error, and data properties
 * you can use to render your UI.
 *
 * @param baseOptions options that will be passed into the query, supported options are listed on: https://www.apollographql.com/docs/react/api/react-hooks/#options;
 *
 * @example
 * const { data, loading, error } = useGenresFetchGenreQuery({
 *   variables: {
 *      id: // value for 'id'
 *   },
 * });
 */
export function useGenresFetchGenreQuery(baseOptions: Apollo.QueryHookOptions<IGenresFetchGenreQuery, IGenresFetchGenreQueryVariables>) {
        const options = {...defaultOptions, ...baseOptions}
        return Apollo.useQuery<IGenresFetchGenreQuery, IGenresFetchGenreQueryVariables>(GenresFetchGenreDocument, options);
      }
export function useGenresFetchGenreLazyQuery(baseOptions?: Apollo.LazyQueryHookOptions<IGenresFetchGenreQuery, IGenresFetchGenreQueryVariables>) {
          const options = {...defaultOptions, ...baseOptions}
          return Apollo.useLazyQuery<IGenresFetchGenreQuery, IGenresFetchGenreQueryVariables>(GenresFetchGenreDocument, options);
        }
export type GenresFetchGenreQueryHookResult = ReturnType<typeof useGenresFetchGenreQuery>;
export type GenresFetchGenreLazyQueryHookResult = ReturnType<typeof useGenresFetchGenreLazyQuery>;
export type GenresFetchGenreQueryResult = Apollo.QueryResult<IGenresFetchGenreQuery, IGenresFetchGenreQueryVariables>;
export function refetchGenresFetchGenreQuery(variables?: IGenresFetchGenreQueryVariables) {
      return { query: GenresFetchGenreDocument, variables: variables }
    }
export const InvitesFetchInvitesDocument = gql`
    query InvitesFetchInvites {
  invites {
    total
    results {
      ...InviteFields
    }
  }
}
    ${InviteFieldsFragmentDoc}`;

/**
 * __useInvitesFetchInvitesQuery__
 *
 * To run a query within a React component, call `useInvitesFetchInvitesQuery` and pass it any options that fit your needs.
 * When your component renders, `useInvitesFetchInvitesQuery` returns an object from Apollo Client that contains loading, error, and data properties
 * you can use to render your UI.
 *
 * @param baseOptions options that will be passed into the query, supported options are listed on: https://www.apollographql.com/docs/react/api/react-hooks/#options;
 *
 * @example
 * const { data, loading, error } = useInvitesFetchInvitesQuery({
 *   variables: {
 *   },
 * });
 */
export function useInvitesFetchInvitesQuery(baseOptions?: Apollo.QueryHookOptions<IInvitesFetchInvitesQuery, IInvitesFetchInvitesQueryVariables>) {
        const options = {...defaultOptions, ...baseOptions}
        return Apollo.useQuery<IInvitesFetchInvitesQuery, IInvitesFetchInvitesQueryVariables>(InvitesFetchInvitesDocument, options);
      }
export function useInvitesFetchInvitesLazyQuery(baseOptions?: Apollo.LazyQueryHookOptions<IInvitesFetchInvitesQuery, IInvitesFetchInvitesQueryVariables>) {
          const options = {...defaultOptions, ...baseOptions}
          return Apollo.useLazyQuery<IInvitesFetchInvitesQuery, IInvitesFetchInvitesQueryVariables>(InvitesFetchInvitesDocument, options);
        }
export type InvitesFetchInvitesQueryHookResult = ReturnType<typeof useInvitesFetchInvitesQuery>;
export type InvitesFetchInvitesLazyQueryHookResult = ReturnType<typeof useInvitesFetchInvitesLazyQuery>;
export type InvitesFetchInvitesQueryResult = Apollo.QueryResult<IInvitesFetchInvitesQuery, IInvitesFetchInvitesQueryVariables>;
export function refetchInvitesFetchInvitesQuery(variables?: IInvitesFetchInvitesQueryVariables) {
      return { query: InvitesFetchInvitesDocument, variables: variables }
    }
export const InvitesCreateInviteDocument = gql`
    mutation InvitesCreateInvite {
  createInvite {
    ...InviteFields
  }
}
    ${InviteFieldsFragmentDoc}`;
export type IInvitesCreateInviteMutationFn = Apollo.MutationFunction<IInvitesCreateInviteMutation, IInvitesCreateInviteMutationVariables>;

/**
 * __useInvitesCreateInviteMutation__
 *
 * To run a mutation, you first call `useInvitesCreateInviteMutation` within a React component and pass it any options that fit your needs.
 * When your component renders, `useInvitesCreateInviteMutation` returns a tuple that includes:
 * - A mutate function that you can call at any time to execute the mutation
 * - An object with fields that represent the current status of the mutation's execution
 *
 * @param baseOptions options that will be passed into the mutation, supported options are listed on: https://www.apollographql.com/docs/react/api/react-hooks/#options-2;
 *
 * @example
 * const [invitesCreateInviteMutation, { data, loading, error }] = useInvitesCreateInviteMutation({
 *   variables: {
 *   },
 * });
 */
export function useInvitesCreateInviteMutation(baseOptions?: Apollo.MutationHookOptions<IInvitesCreateInviteMutation, IInvitesCreateInviteMutationVariables>) {
        const options = {...defaultOptions, ...baseOptions}
        return Apollo.useMutation<IInvitesCreateInviteMutation, IInvitesCreateInviteMutationVariables>(InvitesCreateInviteDocument, options);
      }
export type InvitesCreateInviteMutationHookResult = ReturnType<typeof useInvitesCreateInviteMutation>;
export type InvitesCreateInviteMutationResult = Apollo.MutationResult<IInvitesCreateInviteMutation>;
export type InvitesCreateInviteMutationOptions = Apollo.BaseMutationOptions<IInvitesCreateInviteMutation, IInvitesCreateInviteMutationVariables>;
export const LabelFetchLabelDocument = gql`
    query LabelFetchLabel($id: Int!) {
  collection(id: $id) {
    ...CollectionFields
  }
}
    ${CollectionFieldsFragmentDoc}`;

/**
 * __useLabelFetchLabelQuery__
 *
 * To run a query within a React component, call `useLabelFetchLabelQuery` and pass it any options that fit your needs.
 * When your component renders, `useLabelFetchLabelQuery` returns an object from Apollo Client that contains loading, error, and data properties
 * you can use to render your UI.
 *
 * @param baseOptions options that will be passed into the query, supported options are listed on: https://www.apollographql.com/docs/react/api/react-hooks/#options;
 *
 * @example
 * const { data, loading, error } = useLabelFetchLabelQuery({
 *   variables: {
 *      id: // value for 'id'
 *   },
 * });
 */
export function useLabelFetchLabelQuery(baseOptions: Apollo.QueryHookOptions<ILabelFetchLabelQuery, ILabelFetchLabelQueryVariables>) {
        const options = {...defaultOptions, ...baseOptions}
        return Apollo.useQuery<ILabelFetchLabelQuery, ILabelFetchLabelQueryVariables>(LabelFetchLabelDocument, options);
      }
export function useLabelFetchLabelLazyQuery(baseOptions?: Apollo.LazyQueryHookOptions<ILabelFetchLabelQuery, ILabelFetchLabelQueryVariables>) {
          const options = {...defaultOptions, ...baseOptions}
          return Apollo.useLazyQuery<ILabelFetchLabelQuery, ILabelFetchLabelQueryVariables>(LabelFetchLabelDocument, options);
        }
export type LabelFetchLabelQueryHookResult = ReturnType<typeof useLabelFetchLabelQuery>;
export type LabelFetchLabelLazyQueryHookResult = ReturnType<typeof useLabelFetchLabelLazyQuery>;
export type LabelFetchLabelQueryResult = Apollo.QueryResult<ILabelFetchLabelQuery, ILabelFetchLabelQueryVariables>;
export function refetchLabelFetchLabelQuery(variables?: ILabelFetchLabelQueryVariables) {
      return { query: LabelFetchLabelDocument, variables: variables }
    }
export const NowPlayingInfoFetchReleaseDocument = gql`
    query NowPlayingInfoFetchRelease($id: Int!) {
  release(id: $id) {
    ...FullReleaseFields
  }
}
    ${FullReleaseFieldsFragmentDoc}`;

/**
 * __useNowPlayingInfoFetchReleaseQuery__
 *
 * To run a query within a React component, call `useNowPlayingInfoFetchReleaseQuery` and pass it any options that fit your needs.
 * When your component renders, `useNowPlayingInfoFetchReleaseQuery` returns an object from Apollo Client that contains loading, error, and data properties
 * you can use to render your UI.
 *
 * @param baseOptions options that will be passed into the query, supported options are listed on: https://www.apollographql.com/docs/react/api/react-hooks/#options;
 *
 * @example
 * const { data, loading, error } = useNowPlayingInfoFetchReleaseQuery({
 *   variables: {
 *      id: // value for 'id'
 *   },
 * });
 */
export function useNowPlayingInfoFetchReleaseQuery(baseOptions: Apollo.QueryHookOptions<INowPlayingInfoFetchReleaseQuery, INowPlayingInfoFetchReleaseQueryVariables>) {
        const options = {...defaultOptions, ...baseOptions}
        return Apollo.useQuery<INowPlayingInfoFetchReleaseQuery, INowPlayingInfoFetchReleaseQueryVariables>(NowPlayingInfoFetchReleaseDocument, options);
      }
export function useNowPlayingInfoFetchReleaseLazyQuery(baseOptions?: Apollo.LazyQueryHookOptions<INowPlayingInfoFetchReleaseQuery, INowPlayingInfoFetchReleaseQueryVariables>) {
          const options = {...defaultOptions, ...baseOptions}
          return Apollo.useLazyQuery<INowPlayingInfoFetchReleaseQuery, INowPlayingInfoFetchReleaseQueryVariables>(NowPlayingInfoFetchReleaseDocument, options);
        }
export type NowPlayingInfoFetchReleaseQueryHookResult = ReturnType<typeof useNowPlayingInfoFetchReleaseQuery>;
export type NowPlayingInfoFetchReleaseLazyQueryHookResult = ReturnType<typeof useNowPlayingInfoFetchReleaseLazyQuery>;
export type NowPlayingInfoFetchReleaseQueryResult = Apollo.QueryResult<INowPlayingInfoFetchReleaseQuery, INowPlayingInfoFetchReleaseQueryVariables>;
export function refetchNowPlayingInfoFetchReleaseQuery(variables?: INowPlayingInfoFetchReleaseQueryVariables) {
      return { query: NowPlayingInfoFetchReleaseDocument, variables: variables }
    }
export const FetchPlaylistsChooserDocument = gql`
    query FetchPlaylistsChooser($types: [PlaylistType!]) {
  playlists(types: $types) {
    results {
      ...PlaylistFields
    }
  }
}
    ${PlaylistFieldsFragmentDoc}`;

/**
 * __useFetchPlaylistsChooserQuery__
 *
 * To run a query within a React component, call `useFetchPlaylistsChooserQuery` and pass it any options that fit your needs.
 * When your component renders, `useFetchPlaylistsChooserQuery` returns an object from Apollo Client that contains loading, error, and data properties
 * you can use to render your UI.
 *
 * @param baseOptions options that will be passed into the query, supported options are listed on: https://www.apollographql.com/docs/react/api/react-hooks/#options;
 *
 * @example
 * const { data, loading, error } = useFetchPlaylistsChooserQuery({
 *   variables: {
 *      types: // value for 'types'
 *   },
 * });
 */
export function useFetchPlaylistsChooserQuery(baseOptions?: Apollo.QueryHookOptions<IFetchPlaylistsChooserQuery, IFetchPlaylistsChooserQueryVariables>) {
        const options = {...defaultOptions, ...baseOptions}
        return Apollo.useQuery<IFetchPlaylistsChooserQuery, IFetchPlaylistsChooserQueryVariables>(FetchPlaylistsChooserDocument, options);
      }
export function useFetchPlaylistsChooserLazyQuery(baseOptions?: Apollo.LazyQueryHookOptions<IFetchPlaylistsChooserQuery, IFetchPlaylistsChooserQueryVariables>) {
          const options = {...defaultOptions, ...baseOptions}
          return Apollo.useLazyQuery<IFetchPlaylistsChooserQuery, IFetchPlaylistsChooserQueryVariables>(FetchPlaylistsChooserDocument, options);
        }
export type FetchPlaylistsChooserQueryHookResult = ReturnType<typeof useFetchPlaylistsChooserQuery>;
export type FetchPlaylistsChooserLazyQueryHookResult = ReturnType<typeof useFetchPlaylistsChooserLazyQuery>;
export type FetchPlaylistsChooserQueryResult = Apollo.QueryResult<IFetchPlaylistsChooserQuery, IFetchPlaylistsChooserQueryVariables>;
export function refetchFetchPlaylistsChooserQuery(variables?: IFetchPlaylistsChooserQueryVariables) {
      return { query: FetchPlaylistsChooserDocument, variables: variables }
    }
export const StarPlaylistChooserDocument = gql`
    mutation StarPlaylistChooser($id: Int!) {
  starPlaylist(id: $id) {
    id
    starred
  }
}
    `;
export type IStarPlaylistChooserMutationFn = Apollo.MutationFunction<IStarPlaylistChooserMutation, IStarPlaylistChooserMutationVariables>;

/**
 * __useStarPlaylistChooserMutation__
 *
 * To run a mutation, you first call `useStarPlaylistChooserMutation` within a React component and pass it any options that fit your needs.
 * When your component renders, `useStarPlaylistChooserMutation` returns a tuple that includes:
 * - A mutate function that you can call at any time to execute the mutation
 * - An object with fields that represent the current status of the mutation's execution
 *
 * @param baseOptions options that will be passed into the mutation, supported options are listed on: https://www.apollographql.com/docs/react/api/react-hooks/#options-2;
 *
 * @example
 * const [starPlaylistChooserMutation, { data, loading, error }] = useStarPlaylistChooserMutation({
 *   variables: {
 *      id: // value for 'id'
 *   },
 * });
 */
export function useStarPlaylistChooserMutation(baseOptions?: Apollo.MutationHookOptions<IStarPlaylistChooserMutation, IStarPlaylistChooserMutationVariables>) {
        const options = {...defaultOptions, ...baseOptions}
        return Apollo.useMutation<IStarPlaylistChooserMutation, IStarPlaylistChooserMutationVariables>(StarPlaylistChooserDocument, options);
      }
export type StarPlaylistChooserMutationHookResult = ReturnType<typeof useStarPlaylistChooserMutation>;
export type StarPlaylistChooserMutationResult = Apollo.MutationResult<IStarPlaylistChooserMutation>;
export type StarPlaylistChooserMutationOptions = Apollo.BaseMutationOptions<IStarPlaylistChooserMutation, IStarPlaylistChooserMutationVariables>;
export const UnstarPlaylistChooserDocument = gql`
    mutation UnstarPlaylistChooser($id: Int!) {
  unstarPlaylist(id: $id) {
    id
    starred
  }
}
    `;
export type IUnstarPlaylistChooserMutationFn = Apollo.MutationFunction<IUnstarPlaylistChooserMutation, IUnstarPlaylistChooserMutationVariables>;

/**
 * __useUnstarPlaylistChooserMutation__
 *
 * To run a mutation, you first call `useUnstarPlaylistChooserMutation` within a React component and pass it any options that fit your needs.
 * When your component renders, `useUnstarPlaylistChooserMutation` returns a tuple that includes:
 * - A mutate function that you can call at any time to execute the mutation
 * - An object with fields that represent the current status of the mutation's execution
 *
 * @param baseOptions options that will be passed into the mutation, supported options are listed on: https://www.apollographql.com/docs/react/api/react-hooks/#options-2;
 *
 * @example
 * const [unstarPlaylistChooserMutation, { data, loading, error }] = useUnstarPlaylistChooserMutation({
 *   variables: {
 *      id: // value for 'id'
 *   },
 * });
 */
export function useUnstarPlaylistChooserMutation(baseOptions?: Apollo.MutationHookOptions<IUnstarPlaylistChooserMutation, IUnstarPlaylistChooserMutationVariables>) {
        const options = {...defaultOptions, ...baseOptions}
        return Apollo.useMutation<IUnstarPlaylistChooserMutation, IUnstarPlaylistChooserMutationVariables>(UnstarPlaylistChooserDocument, options);
      }
export type UnstarPlaylistChooserMutationHookResult = ReturnType<typeof useUnstarPlaylistChooserMutation>;
export type UnstarPlaylistChooserMutationResult = Apollo.MutationResult<IUnstarPlaylistChooserMutation>;
export type UnstarPlaylistChooserMutationOptions = Apollo.BaseMutationOptions<IUnstarPlaylistChooserMutation, IUnstarPlaylistChooserMutationVariables>;
export const PlaylistsFetchPlaylistDocument = gql`
    query PlaylistsFetchPlaylist($id: Int!) {
  playlist(id: $id) {
    ...PlaylistFields
  }
}
    ${PlaylistFieldsFragmentDoc}`;

/**
 * __usePlaylistsFetchPlaylistQuery__
 *
 * To run a query within a React component, call `usePlaylistsFetchPlaylistQuery` and pass it any options that fit your needs.
 * When your component renders, `usePlaylistsFetchPlaylistQuery` returns an object from Apollo Client that contains loading, error, and data properties
 * you can use to render your UI.
 *
 * @param baseOptions options that will be passed into the query, supported options are listed on: https://www.apollographql.com/docs/react/api/react-hooks/#options;
 *
 * @example
 * const { data, loading, error } = usePlaylistsFetchPlaylistQuery({
 *   variables: {
 *      id: // value for 'id'
 *   },
 * });
 */
export function usePlaylistsFetchPlaylistQuery(baseOptions: Apollo.QueryHookOptions<IPlaylistsFetchPlaylistQuery, IPlaylistsFetchPlaylistQueryVariables>) {
        const options = {...defaultOptions, ...baseOptions}
        return Apollo.useQuery<IPlaylistsFetchPlaylistQuery, IPlaylistsFetchPlaylistQueryVariables>(PlaylistsFetchPlaylistDocument, options);
      }
export function usePlaylistsFetchPlaylistLazyQuery(baseOptions?: Apollo.LazyQueryHookOptions<IPlaylistsFetchPlaylistQuery, IPlaylistsFetchPlaylistQueryVariables>) {
          const options = {...defaultOptions, ...baseOptions}
          return Apollo.useLazyQuery<IPlaylistsFetchPlaylistQuery, IPlaylistsFetchPlaylistQueryVariables>(PlaylistsFetchPlaylistDocument, options);
        }
export type PlaylistsFetchPlaylistQueryHookResult = ReturnType<typeof usePlaylistsFetchPlaylistQuery>;
export type PlaylistsFetchPlaylistLazyQueryHookResult = ReturnType<typeof usePlaylistsFetchPlaylistLazyQuery>;
export type PlaylistsFetchPlaylistQueryResult = Apollo.QueryResult<IPlaylistsFetchPlaylistQuery, IPlaylistsFetchPlaylistQueryVariables>;
export function refetchPlaylistsFetchPlaylistQuery(variables?: IPlaylistsFetchPlaylistQueryVariables) {
      return { query: PlaylistsFetchPlaylistDocument, variables: variables }
    }
export const PlaylistsFetchTracksDocument = gql`
    query PlaylistsFetchTracks($id: Int!) {
  playlist(id: $id) {
    id
    entries {
      id
      track {
        ...TrackFields
      }
    }
  }
}
    ${TrackFieldsFragmentDoc}`;

/**
 * __usePlaylistsFetchTracksQuery__
 *
 * To run a query within a React component, call `usePlaylistsFetchTracksQuery` and pass it any options that fit your needs.
 * When your component renders, `usePlaylistsFetchTracksQuery` returns an object from Apollo Client that contains loading, error, and data properties
 * you can use to render your UI.
 *
 * @param baseOptions options that will be passed into the query, supported options are listed on: https://www.apollographql.com/docs/react/api/react-hooks/#options;
 *
 * @example
 * const { data, loading, error } = usePlaylistsFetchTracksQuery({
 *   variables: {
 *      id: // value for 'id'
 *   },
 * });
 */
export function usePlaylistsFetchTracksQuery(baseOptions: Apollo.QueryHookOptions<IPlaylistsFetchTracksQuery, IPlaylistsFetchTracksQueryVariables>) {
        const options = {...defaultOptions, ...baseOptions}
        return Apollo.useQuery<IPlaylistsFetchTracksQuery, IPlaylistsFetchTracksQueryVariables>(PlaylistsFetchTracksDocument, options);
      }
export function usePlaylistsFetchTracksLazyQuery(baseOptions?: Apollo.LazyQueryHookOptions<IPlaylistsFetchTracksQuery, IPlaylistsFetchTracksQueryVariables>) {
          const options = {...defaultOptions, ...baseOptions}
          return Apollo.useLazyQuery<IPlaylistsFetchTracksQuery, IPlaylistsFetchTracksQueryVariables>(PlaylistsFetchTracksDocument, options);
        }
export type PlaylistsFetchTracksQueryHookResult = ReturnType<typeof usePlaylistsFetchTracksQuery>;
export type PlaylistsFetchTracksLazyQueryHookResult = ReturnType<typeof usePlaylistsFetchTracksLazyQuery>;
export type PlaylistsFetchTracksQueryResult = Apollo.QueryResult<IPlaylistsFetchTracksQuery, IPlaylistsFetchTracksQueryVariables>;
export function refetchPlaylistsFetchTracksQuery(variables?: IPlaylistsFetchTracksQueryVariables) {
      return { query: PlaylistsFetchTracksDocument, variables: variables }
    }
export const InFavoritesFetchFavoritesIdDocument = gql`
    query InFavoritesFetchFavoritesId {
  user {
    id
    favoritesCollectionId
  }
}
    `;

/**
 * __useInFavoritesFetchFavoritesIdQuery__
 *
 * To run a query within a React component, call `useInFavoritesFetchFavoritesIdQuery` and pass it any options that fit your needs.
 * When your component renders, `useInFavoritesFetchFavoritesIdQuery` returns an object from Apollo Client that contains loading, error, and data properties
 * you can use to render your UI.
 *
 * @param baseOptions options that will be passed into the query, supported options are listed on: https://www.apollographql.com/docs/react/api/react-hooks/#options;
 *
 * @example
 * const { data, loading, error } = useInFavoritesFetchFavoritesIdQuery({
 *   variables: {
 *   },
 * });
 */
export function useInFavoritesFetchFavoritesIdQuery(baseOptions?: Apollo.QueryHookOptions<IInFavoritesFetchFavoritesIdQuery, IInFavoritesFetchFavoritesIdQueryVariables>) {
        const options = {...defaultOptions, ...baseOptions}
        return Apollo.useQuery<IInFavoritesFetchFavoritesIdQuery, IInFavoritesFetchFavoritesIdQueryVariables>(InFavoritesFetchFavoritesIdDocument, options);
      }
export function useInFavoritesFetchFavoritesIdLazyQuery(baseOptions?: Apollo.LazyQueryHookOptions<IInFavoritesFetchFavoritesIdQuery, IInFavoritesFetchFavoritesIdQueryVariables>) {
          const options = {...defaultOptions, ...baseOptions}
          return Apollo.useLazyQuery<IInFavoritesFetchFavoritesIdQuery, IInFavoritesFetchFavoritesIdQueryVariables>(InFavoritesFetchFavoritesIdDocument, options);
        }
export type InFavoritesFetchFavoritesIdQueryHookResult = ReturnType<typeof useInFavoritesFetchFavoritesIdQuery>;
export type InFavoritesFetchFavoritesIdLazyQueryHookResult = ReturnType<typeof useInFavoritesFetchFavoritesIdLazyQuery>;
export type InFavoritesFetchFavoritesIdQueryResult = Apollo.QueryResult<IInFavoritesFetchFavoritesIdQuery, IInFavoritesFetchFavoritesIdQueryVariables>;
export function refetchInFavoritesFetchFavoritesIdQuery(variables?: IInFavoritesFetchFavoritesIdQueryVariables) {
      return { query: InFavoritesFetchFavoritesIdDocument, variables: variables }
    }
export const InFavoritesAddReleaseToCollectionDocument = gql`
    mutation InFavoritesAddReleaseToCollection($collectionId: Int!, $releaseId: Int!) {
  addReleaseToCollection(collectionId: $collectionId, releaseId: $releaseId) {
    collection {
      id
      numReleases
      lastUpdatedOn
    }
    release {
      id
      inInbox
      inFavorites
      genres {
        id
        name
      }
      labels {
        id
        name
      }
      collages {
        id
        name
      }
    }
  }
}
    `;
export type IInFavoritesAddReleaseToCollectionMutationFn = Apollo.MutationFunction<IInFavoritesAddReleaseToCollectionMutation, IInFavoritesAddReleaseToCollectionMutationVariables>;

/**
 * __useInFavoritesAddReleaseToCollectionMutation__
 *
 * To run a mutation, you first call `useInFavoritesAddReleaseToCollectionMutation` within a React component and pass it any options that fit your needs.
 * When your component renders, `useInFavoritesAddReleaseToCollectionMutation` returns a tuple that includes:
 * - A mutate function that you can call at any time to execute the mutation
 * - An object with fields that represent the current status of the mutation's execution
 *
 * @param baseOptions options that will be passed into the mutation, supported options are listed on: https://www.apollographql.com/docs/react/api/react-hooks/#options-2;
 *
 * @example
 * const [inFavoritesAddReleaseToCollectionMutation, { data, loading, error }] = useInFavoritesAddReleaseToCollectionMutation({
 *   variables: {
 *      collectionId: // value for 'collectionId'
 *      releaseId: // value for 'releaseId'
 *   },
 * });
 */
export function useInFavoritesAddReleaseToCollectionMutation(baseOptions?: Apollo.MutationHookOptions<IInFavoritesAddReleaseToCollectionMutation, IInFavoritesAddReleaseToCollectionMutationVariables>) {
        const options = {...defaultOptions, ...baseOptions}
        return Apollo.useMutation<IInFavoritesAddReleaseToCollectionMutation, IInFavoritesAddReleaseToCollectionMutationVariables>(InFavoritesAddReleaseToCollectionDocument, options);
      }
export type InFavoritesAddReleaseToCollectionMutationHookResult = ReturnType<typeof useInFavoritesAddReleaseToCollectionMutation>;
export type InFavoritesAddReleaseToCollectionMutationResult = Apollo.MutationResult<IInFavoritesAddReleaseToCollectionMutation>;
export type InFavoritesAddReleaseToCollectionMutationOptions = Apollo.BaseMutationOptions<IInFavoritesAddReleaseToCollectionMutation, IInFavoritesAddReleaseToCollectionMutationVariables>;
export const InFavoritesDelReleaseFromCollectionDocument = gql`
    mutation InFavoritesDelReleaseFromCollection($collectionId: Int!, $releaseId: Int!) {
  delReleaseFromCollection(collectionId: $collectionId, releaseId: $releaseId) {
    collection {
      id
      numReleases
      lastUpdatedOn
    }
    release {
      id
      inInbox
      inFavorites
      genres {
        id
        name
      }
      labels {
        id
        name
      }
      collages {
        id
        name
      }
    }
  }
}
    `;
export type IInFavoritesDelReleaseFromCollectionMutationFn = Apollo.MutationFunction<IInFavoritesDelReleaseFromCollectionMutation, IInFavoritesDelReleaseFromCollectionMutationVariables>;

/**
 * __useInFavoritesDelReleaseFromCollectionMutation__
 *
 * To run a mutation, you first call `useInFavoritesDelReleaseFromCollectionMutation` within a React component and pass it any options that fit your needs.
 * When your component renders, `useInFavoritesDelReleaseFromCollectionMutation` returns a tuple that includes:
 * - A mutate function that you can call at any time to execute the mutation
 * - An object with fields that represent the current status of the mutation's execution
 *
 * @param baseOptions options that will be passed into the mutation, supported options are listed on: https://www.apollographql.com/docs/react/api/react-hooks/#options-2;
 *
 * @example
 * const [inFavoritesDelReleaseFromCollectionMutation, { data, loading, error }] = useInFavoritesDelReleaseFromCollectionMutation({
 *   variables: {
 *      collectionId: // value for 'collectionId'
 *      releaseId: // value for 'releaseId'
 *   },
 * });
 */
export function useInFavoritesDelReleaseFromCollectionMutation(baseOptions?: Apollo.MutationHookOptions<IInFavoritesDelReleaseFromCollectionMutation, IInFavoritesDelReleaseFromCollectionMutationVariables>) {
        const options = {...defaultOptions, ...baseOptions}
        return Apollo.useMutation<IInFavoritesDelReleaseFromCollectionMutation, IInFavoritesDelReleaseFromCollectionMutationVariables>(InFavoritesDelReleaseFromCollectionDocument, options);
      }
export type InFavoritesDelReleaseFromCollectionMutationHookResult = ReturnType<typeof useInFavoritesDelReleaseFromCollectionMutation>;
export type InFavoritesDelReleaseFromCollectionMutationResult = Apollo.MutationResult<IInFavoritesDelReleaseFromCollectionMutation>;
export type InFavoritesDelReleaseFromCollectionMutationOptions = Apollo.BaseMutationOptions<IInFavoritesDelReleaseFromCollectionMutation, IInFavoritesDelReleaseFromCollectionMutationVariables>;
export const InInboxFetchInboxIdDocument = gql`
    query InInboxFetchInboxId {
  user {
    id
    inboxCollectionId
  }
}
    `;

/**
 * __useInInboxFetchInboxIdQuery__
 *
 * To run a query within a React component, call `useInInboxFetchInboxIdQuery` and pass it any options that fit your needs.
 * When your component renders, `useInInboxFetchInboxIdQuery` returns an object from Apollo Client that contains loading, error, and data properties
 * you can use to render your UI.
 *
 * @param baseOptions options that will be passed into the query, supported options are listed on: https://www.apollographql.com/docs/react/api/react-hooks/#options;
 *
 * @example
 * const { data, loading, error } = useInInboxFetchInboxIdQuery({
 *   variables: {
 *   },
 * });
 */
export function useInInboxFetchInboxIdQuery(baseOptions?: Apollo.QueryHookOptions<IInInboxFetchInboxIdQuery, IInInboxFetchInboxIdQueryVariables>) {
        const options = {...defaultOptions, ...baseOptions}
        return Apollo.useQuery<IInInboxFetchInboxIdQuery, IInInboxFetchInboxIdQueryVariables>(InInboxFetchInboxIdDocument, options);
      }
export function useInInboxFetchInboxIdLazyQuery(baseOptions?: Apollo.LazyQueryHookOptions<IInInboxFetchInboxIdQuery, IInInboxFetchInboxIdQueryVariables>) {
          const options = {...defaultOptions, ...baseOptions}
          return Apollo.useLazyQuery<IInInboxFetchInboxIdQuery, IInInboxFetchInboxIdQueryVariables>(InInboxFetchInboxIdDocument, options);
        }
export type InInboxFetchInboxIdQueryHookResult = ReturnType<typeof useInInboxFetchInboxIdQuery>;
export type InInboxFetchInboxIdLazyQueryHookResult = ReturnType<typeof useInInboxFetchInboxIdLazyQuery>;
export type InInboxFetchInboxIdQueryResult = Apollo.QueryResult<IInInboxFetchInboxIdQuery, IInInboxFetchInboxIdQueryVariables>;
export function refetchInInboxFetchInboxIdQuery(variables?: IInInboxFetchInboxIdQueryVariables) {
      return { query: InInboxFetchInboxIdDocument, variables: variables }
    }
export const InInboxAddReleaseToCollectionDocument = gql`
    mutation InInboxAddReleaseToCollection($collectionId: Int!, $releaseId: Int!) {
  addReleaseToCollection(collectionId: $collectionId, releaseId: $releaseId) {
    collection {
      id
      numReleases
      lastUpdatedOn
    }
    release {
      id
      inInbox
      inFavorites
      genres {
        id
        name
      }
      labels {
        id
        name
      }
      collages {
        id
        name
      }
    }
  }
}
    `;
export type IInInboxAddReleaseToCollectionMutationFn = Apollo.MutationFunction<IInInboxAddReleaseToCollectionMutation, IInInboxAddReleaseToCollectionMutationVariables>;

/**
 * __useInInboxAddReleaseToCollectionMutation__
 *
 * To run a mutation, you first call `useInInboxAddReleaseToCollectionMutation` within a React component and pass it any options that fit your needs.
 * When your component renders, `useInInboxAddReleaseToCollectionMutation` returns a tuple that includes:
 * - A mutate function that you can call at any time to execute the mutation
 * - An object with fields that represent the current status of the mutation's execution
 *
 * @param baseOptions options that will be passed into the mutation, supported options are listed on: https://www.apollographql.com/docs/react/api/react-hooks/#options-2;
 *
 * @example
 * const [inInboxAddReleaseToCollectionMutation, { data, loading, error }] = useInInboxAddReleaseToCollectionMutation({
 *   variables: {
 *      collectionId: // value for 'collectionId'
 *      releaseId: // value for 'releaseId'
 *   },
 * });
 */
export function useInInboxAddReleaseToCollectionMutation(baseOptions?: Apollo.MutationHookOptions<IInInboxAddReleaseToCollectionMutation, IInInboxAddReleaseToCollectionMutationVariables>) {
        const options = {...defaultOptions, ...baseOptions}
        return Apollo.useMutation<IInInboxAddReleaseToCollectionMutation, IInInboxAddReleaseToCollectionMutationVariables>(InInboxAddReleaseToCollectionDocument, options);
      }
export type InInboxAddReleaseToCollectionMutationHookResult = ReturnType<typeof useInInboxAddReleaseToCollectionMutation>;
export type InInboxAddReleaseToCollectionMutationResult = Apollo.MutationResult<IInInboxAddReleaseToCollectionMutation>;
export type InInboxAddReleaseToCollectionMutationOptions = Apollo.BaseMutationOptions<IInInboxAddReleaseToCollectionMutation, IInInboxAddReleaseToCollectionMutationVariables>;
export const InInboxDelReleaseFromCollectionDocument = gql`
    mutation InInboxDelReleaseFromCollection($collectionId: Int!, $releaseId: Int!) {
  delReleaseFromCollection(collectionId: $collectionId, releaseId: $releaseId) {
    collection {
      id
      numReleases
      lastUpdatedOn
    }
    release {
      id
      inInbox
      inFavorites
      genres {
        id
        name
      }
      labels {
        id
        name
      }
      collages {
        id
        name
      }
    }
  }
}
    `;
export type IInInboxDelReleaseFromCollectionMutationFn = Apollo.MutationFunction<IInInboxDelReleaseFromCollectionMutation, IInInboxDelReleaseFromCollectionMutationVariables>;

/**
 * __useInInboxDelReleaseFromCollectionMutation__
 *
 * To run a mutation, you first call `useInInboxDelReleaseFromCollectionMutation` within a React component and pass it any options that fit your needs.
 * When your component renders, `useInInboxDelReleaseFromCollectionMutation` returns a tuple that includes:
 * - A mutate function that you can call at any time to execute the mutation
 * - An object with fields that represent the current status of the mutation's execution
 *
 * @param baseOptions options that will be passed into the mutation, supported options are listed on: https://www.apollographql.com/docs/react/api/react-hooks/#options-2;
 *
 * @example
 * const [inInboxDelReleaseFromCollectionMutation, { data, loading, error }] = useInInboxDelReleaseFromCollectionMutation({
 *   variables: {
 *      collectionId: // value for 'collectionId'
 *      releaseId: // value for 'releaseId'
 *   },
 * });
 */
export function useInInboxDelReleaseFromCollectionMutation(baseOptions?: Apollo.MutationHookOptions<IInInboxDelReleaseFromCollectionMutation, IInInboxDelReleaseFromCollectionMutationVariables>) {
        const options = {...defaultOptions, ...baseOptions}
        return Apollo.useMutation<IInInboxDelReleaseFromCollectionMutation, IInInboxDelReleaseFromCollectionMutationVariables>(InInboxDelReleaseFromCollectionDocument, options);
      }
export type InInboxDelReleaseFromCollectionMutationHookResult = ReturnType<typeof useInInboxDelReleaseFromCollectionMutation>;
export type InInboxDelReleaseFromCollectionMutationResult = Apollo.MutationResult<IInInboxDelReleaseFromCollectionMutation>;
export type InInboxDelReleaseFromCollectionMutationOptions = Apollo.BaseMutationOptions<IInInboxDelReleaseFromCollectionMutation, IInInboxDelReleaseFromCollectionMutationVariables>;
export const ReleaseUpdateReleaseRatingDocument = gql`
    mutation ReleaseUpdateReleaseRating($id: Int!, $rating: Int) {
  updateRelease(id: $id, rating: $rating) {
    id
    rating
  }
}
    `;
export type IReleaseUpdateReleaseRatingMutationFn = Apollo.MutationFunction<IReleaseUpdateReleaseRatingMutation, IReleaseUpdateReleaseRatingMutationVariables>;

/**
 * __useReleaseUpdateReleaseRatingMutation__
 *
 * To run a mutation, you first call `useReleaseUpdateReleaseRatingMutation` within a React component and pass it any options that fit your needs.
 * When your component renders, `useReleaseUpdateReleaseRatingMutation` returns a tuple that includes:
 * - A mutate function that you can call at any time to execute the mutation
 * - An object with fields that represent the current status of the mutation's execution
 *
 * @param baseOptions options that will be passed into the mutation, supported options are listed on: https://www.apollographql.com/docs/react/api/react-hooks/#options-2;
 *
 * @example
 * const [releaseUpdateReleaseRatingMutation, { data, loading, error }] = useReleaseUpdateReleaseRatingMutation({
 *   variables: {
 *      id: // value for 'id'
 *      rating: // value for 'rating'
 *   },
 * });
 */
export function useReleaseUpdateReleaseRatingMutation(baseOptions?: Apollo.MutationHookOptions<IReleaseUpdateReleaseRatingMutation, IReleaseUpdateReleaseRatingMutationVariables>) {
        const options = {...defaultOptions, ...baseOptions}
        return Apollo.useMutation<IReleaseUpdateReleaseRatingMutation, IReleaseUpdateReleaseRatingMutationVariables>(ReleaseUpdateReleaseRatingDocument, options);
      }
export type ReleaseUpdateReleaseRatingMutationHookResult = ReturnType<typeof useReleaseUpdateReleaseRatingMutation>;
export type ReleaseUpdateReleaseRatingMutationResult = Apollo.MutationResult<IReleaseUpdateReleaseRatingMutation>;
export type ReleaseUpdateReleaseRatingMutationOptions = Apollo.BaseMutationOptions<IReleaseUpdateReleaseRatingMutation, IReleaseUpdateReleaseRatingMutationVariables>;
export const ReleaseFetchReleaseDocument = gql`
    query ReleaseFetchRelease($id: Int!) {
  release(id: $id) {
    ...FullReleaseFields
  }
}
    ${FullReleaseFieldsFragmentDoc}`;

/**
 * __useReleaseFetchReleaseQuery__
 *
 * To run a query within a React component, call `useReleaseFetchReleaseQuery` and pass it any options that fit your needs.
 * When your component renders, `useReleaseFetchReleaseQuery` returns an object from Apollo Client that contains loading, error, and data properties
 * you can use to render your UI.
 *
 * @param baseOptions options that will be passed into the query, supported options are listed on: https://www.apollographql.com/docs/react/api/react-hooks/#options;
 *
 * @example
 * const { data, loading, error } = useReleaseFetchReleaseQuery({
 *   variables: {
 *      id: // value for 'id'
 *   },
 * });
 */
export function useReleaseFetchReleaseQuery(baseOptions: Apollo.QueryHookOptions<IReleaseFetchReleaseQuery, IReleaseFetchReleaseQueryVariables>) {
        const options = {...defaultOptions, ...baseOptions}
        return Apollo.useQuery<IReleaseFetchReleaseQuery, IReleaseFetchReleaseQueryVariables>(ReleaseFetchReleaseDocument, options);
      }
export function useReleaseFetchReleaseLazyQuery(baseOptions?: Apollo.LazyQueryHookOptions<IReleaseFetchReleaseQuery, IReleaseFetchReleaseQueryVariables>) {
          const options = {...defaultOptions, ...baseOptions}
          return Apollo.useLazyQuery<IReleaseFetchReleaseQuery, IReleaseFetchReleaseQueryVariables>(ReleaseFetchReleaseDocument, options);
        }
export type ReleaseFetchReleaseQueryHookResult = ReturnType<typeof useReleaseFetchReleaseQuery>;
export type ReleaseFetchReleaseLazyQueryHookResult = ReturnType<typeof useReleaseFetchReleaseLazyQuery>;
export type ReleaseFetchReleaseQueryResult = Apollo.QueryResult<IReleaseFetchReleaseQuery, IReleaseFetchReleaseQueryVariables>;
export function refetchReleaseFetchReleaseQuery(variables?: IReleaseFetchReleaseQueryVariables) {
      return { query: ReleaseFetchReleaseDocument, variables: variables }
    }
export const SettingsFetchUserDocument = gql`
    query SettingsFetchUser {
  user {
    ...UserFields
  }
}
    ${UserFieldsFragmentDoc}`;

/**
 * __useSettingsFetchUserQuery__
 *
 * To run a query within a React component, call `useSettingsFetchUserQuery` and pass it any options that fit your needs.
 * When your component renders, `useSettingsFetchUserQuery` returns an object from Apollo Client that contains loading, error, and data properties
 * you can use to render your UI.
 *
 * @param baseOptions options that will be passed into the query, supported options are listed on: https://www.apollographql.com/docs/react/api/react-hooks/#options;
 *
 * @example
 * const { data, loading, error } = useSettingsFetchUserQuery({
 *   variables: {
 *   },
 * });
 */
export function useSettingsFetchUserQuery(baseOptions?: Apollo.QueryHookOptions<ISettingsFetchUserQuery, ISettingsFetchUserQueryVariables>) {
        const options = {...defaultOptions, ...baseOptions}
        return Apollo.useQuery<ISettingsFetchUserQuery, ISettingsFetchUserQueryVariables>(SettingsFetchUserDocument, options);
      }
export function useSettingsFetchUserLazyQuery(baseOptions?: Apollo.LazyQueryHookOptions<ISettingsFetchUserQuery, ISettingsFetchUserQueryVariables>) {
          const options = {...defaultOptions, ...baseOptions}
          return Apollo.useLazyQuery<ISettingsFetchUserQuery, ISettingsFetchUserQueryVariables>(SettingsFetchUserDocument, options);
        }
export type SettingsFetchUserQueryHookResult = ReturnType<typeof useSettingsFetchUserQuery>;
export type SettingsFetchUserLazyQueryHookResult = ReturnType<typeof useSettingsFetchUserLazyQuery>;
export type SettingsFetchUserQueryResult = Apollo.QueryResult<ISettingsFetchUserQuery, ISettingsFetchUserQueryVariables>;
export function refetchSettingsFetchUserQuery(variables?: ISettingsFetchUserQueryVariables) {
      return { query: SettingsFetchUserDocument, variables: variables }
    }
export const SettingsUpdateUserDocument = gql`
    mutation SettingsUpdateUser($nickname: String) {
  updateUser(nickname: $nickname) {
    id
    nickname
  }
}
    `;
export type ISettingsUpdateUserMutationFn = Apollo.MutationFunction<ISettingsUpdateUserMutation, ISettingsUpdateUserMutationVariables>;

/**
 * __useSettingsUpdateUserMutation__
 *
 * To run a mutation, you first call `useSettingsUpdateUserMutation` within a React component and pass it any options that fit your needs.
 * When your component renders, `useSettingsUpdateUserMutation` returns a tuple that includes:
 * - A mutate function that you can call at any time to execute the mutation
 * - An object with fields that represent the current status of the mutation's execution
 *
 * @param baseOptions options that will be passed into the mutation, supported options are listed on: https://www.apollographql.com/docs/react/api/react-hooks/#options-2;
 *
 * @example
 * const [settingsUpdateUserMutation, { data, loading, error }] = useSettingsUpdateUserMutation({
 *   variables: {
 *      nickname: // value for 'nickname'
 *   },
 * });
 */
export function useSettingsUpdateUserMutation(baseOptions?: Apollo.MutationHookOptions<ISettingsUpdateUserMutation, ISettingsUpdateUserMutationVariables>) {
        const options = {...defaultOptions, ...baseOptions}
        return Apollo.useMutation<ISettingsUpdateUserMutation, ISettingsUpdateUserMutationVariables>(SettingsUpdateUserDocument, options);
      }
export type SettingsUpdateUserMutationHookResult = ReturnType<typeof useSettingsUpdateUserMutation>;
export type SettingsUpdateUserMutationResult = Apollo.MutationResult<ISettingsUpdateUserMutation>;
export type SettingsUpdateUserMutationOptions = Apollo.BaseMutationOptions<ISettingsUpdateUserMutation, ISettingsUpdateUserMutationVariables>;
export const YearsFetchReleaseYearsDocument = gql`
    query YearsFetchReleaseYears {
  releaseYears
}
    `;

/**
 * __useYearsFetchReleaseYearsQuery__
 *
 * To run a query within a React component, call `useYearsFetchReleaseYearsQuery` and pass it any options that fit your needs.
 * When your component renders, `useYearsFetchReleaseYearsQuery` returns an object from Apollo Client that contains loading, error, and data properties
 * you can use to render your UI.
 *
 * @param baseOptions options that will be passed into the query, supported options are listed on: https://www.apollographql.com/docs/react/api/react-hooks/#options;
 *
 * @example
 * const { data, loading, error } = useYearsFetchReleaseYearsQuery({
 *   variables: {
 *   },
 * });
 */
export function useYearsFetchReleaseYearsQuery(baseOptions?: Apollo.QueryHookOptions<IYearsFetchReleaseYearsQuery, IYearsFetchReleaseYearsQueryVariables>) {
        const options = {...defaultOptions, ...baseOptions}
        return Apollo.useQuery<IYearsFetchReleaseYearsQuery, IYearsFetchReleaseYearsQueryVariables>(YearsFetchReleaseYearsDocument, options);
      }
export function useYearsFetchReleaseYearsLazyQuery(baseOptions?: Apollo.LazyQueryHookOptions<IYearsFetchReleaseYearsQuery, IYearsFetchReleaseYearsQueryVariables>) {
          const options = {...defaultOptions, ...baseOptions}
          return Apollo.useLazyQuery<IYearsFetchReleaseYearsQuery, IYearsFetchReleaseYearsQueryVariables>(YearsFetchReleaseYearsDocument, options);
        }
export type YearsFetchReleaseYearsQueryHookResult = ReturnType<typeof useYearsFetchReleaseYearsQuery>;
export type YearsFetchReleaseYearsLazyQueryHookResult = ReturnType<typeof useYearsFetchReleaseYearsLazyQuery>;
export type YearsFetchReleaseYearsQueryResult = Apollo.QueryResult<IYearsFetchReleaseYearsQuery, IYearsFetchReleaseYearsQueryVariables>;
export function refetchYearsFetchReleaseYearsQuery(variables?: IYearsFetchReleaseYearsQueryVariables) {
      return { query: YearsFetchReleaseYearsDocument, variables: variables }
    }
export type ArtistKeySpecifier = ('id' | 'name' | 'starred' | 'numReleases' | 'imageId' | 'releases' | 'topGenres' | ArtistKeySpecifier)[];
export type ArtistFieldPolicy = {
	id?: FieldPolicy<any> | FieldReadFunction<any>,
	name?: FieldPolicy<any> | FieldReadFunction<any>,
	starred?: FieldPolicy<any> | FieldReadFunction<any>,
	numReleases?: FieldPolicy<any> | FieldReadFunction<any>,
	imageId?: FieldPolicy<any> | FieldReadFunction<any>,
	releases?: FieldPolicy<any> | FieldReadFunction<any>,
	topGenres?: FieldPolicy<any> | FieldReadFunction<any>
};
export type ArtistWithRoleKeySpecifier = ('artist' | 'role' | ArtistWithRoleKeySpecifier)[];
export type ArtistWithRoleFieldPolicy = {
	artist?: FieldPolicy<any> | FieldReadFunction<any>,
	role?: FieldPolicy<any> | FieldReadFunction<any>
};
export type ArtistsKeySpecifier = ('total' | 'results' | ArtistsKeySpecifier)[];
export type ArtistsFieldPolicy = {
	total?: FieldPolicy<any> | FieldReadFunction<any>,
	results?: FieldPolicy<any> | FieldReadFunction<any>
};
export type CollectionKeySpecifier = ('id' | 'name' | 'starred' | 'type' | 'numReleases' | 'lastUpdatedOn' | 'imageId' | 'releases' | 'topGenres' | 'user' | CollectionKeySpecifier)[];
export type CollectionFieldPolicy = {
	id?: FieldPolicy<any> | FieldReadFunction<any>,
	name?: FieldPolicy<any> | FieldReadFunction<any>,
	starred?: FieldPolicy<any> | FieldReadFunction<any>,
	type?: FieldPolicy<any> | FieldReadFunction<any>,
	numReleases?: FieldPolicy<any> | FieldReadFunction<any>,
	lastUpdatedOn?: FieldPolicy<any> | FieldReadFunction<any>,
	imageId?: FieldPolicy<any> | FieldReadFunction<any>,
	releases?: FieldPolicy<any> | FieldReadFunction<any>,
	topGenres?: FieldPolicy<any> | FieldReadFunction<any>,
	user?: FieldPolicy<any> | FieldReadFunction<any>
};
export type CollectionAndReleaseKeySpecifier = ('collection' | 'release' | CollectionAndReleaseKeySpecifier)[];
export type CollectionAndReleaseFieldPolicy = {
	collection?: FieldPolicy<any> | FieldReadFunction<any>,
	release?: FieldPolicy<any> | FieldReadFunction<any>
};
export type CollectionsKeySpecifier = ('total' | 'results' | CollectionsKeySpecifier)[];
export type CollectionsFieldPolicy = {
	total?: FieldPolicy<any> | FieldReadFunction<any>,
	results?: FieldPolicy<any> | FieldReadFunction<any>
};
export type InviteKeySpecifier = ('id' | 'code' | 'createdBy' | 'createdAt' | 'usedBy' | InviteKeySpecifier)[];
export type InviteFieldPolicy = {
	id?: FieldPolicy<any> | FieldReadFunction<any>,
	code?: FieldPolicy<any> | FieldReadFunction<any>,
	createdBy?: FieldPolicy<any> | FieldReadFunction<any>,
	createdAt?: FieldPolicy<any> | FieldReadFunction<any>,
	usedBy?: FieldPolicy<any> | FieldReadFunction<any>
};
export type InvitesKeySpecifier = ('total' | 'results' | InvitesKeySpecifier)[];
export type InvitesFieldPolicy = {
	total?: FieldPolicy<any> | FieldReadFunction<any>,
	results?: FieldPolicy<any> | FieldReadFunction<any>
};
export type MutationKeySpecifier = ('updateUser' | 'newToken' | 'createArtist' | 'updateArtist' | 'starArtist' | 'unstarArtist' | 'createCollection' | 'updateCollection' | 'starCollection' | 'unstarCollection' | 'addReleaseToCollection' | 'delReleaseFromCollection' | 'createInvite' | 'createPlaylist' | 'updatePlaylist' | 'starPlaylist' | 'unstarPlaylist' | 'createPlaylistEntry' | 'delPlaylistEntry' | 'delPlaylistEntries' | 'updatePlaylistEntry' | 'createRelease' | 'updateRelease' | 'addArtistToRelease' | 'delArtistFromRelease' | 'updateTrack' | 'addArtistToTrack' | 'delArtistFromTrack' | MutationKeySpecifier)[];
export type MutationFieldPolicy = {
	updateUser?: FieldPolicy<any> | FieldReadFunction<any>,
	newToken?: FieldPolicy<any> | FieldReadFunction<any>,
	createArtist?: FieldPolicy<any> | FieldReadFunction<any>,
	updateArtist?: FieldPolicy<any> | FieldReadFunction<any>,
	starArtist?: FieldPolicy<any> | FieldReadFunction<any>,
	unstarArtist?: FieldPolicy<any> | FieldReadFunction<any>,
	createCollection?: FieldPolicy<any> | FieldReadFunction<any>,
	updateCollection?: FieldPolicy<any> | FieldReadFunction<any>,
	starCollection?: FieldPolicy<any> | FieldReadFunction<any>,
	unstarCollection?: FieldPolicy<any> | FieldReadFunction<any>,
	addReleaseToCollection?: FieldPolicy<any> | FieldReadFunction<any>,
	delReleaseFromCollection?: FieldPolicy<any> | FieldReadFunction<any>,
	createInvite?: FieldPolicy<any> | FieldReadFunction<any>,
	createPlaylist?: FieldPolicy<any> | FieldReadFunction<any>,
	updatePlaylist?: FieldPolicy<any> | FieldReadFunction<any>,
	starPlaylist?: FieldPolicy<any> | FieldReadFunction<any>,
	unstarPlaylist?: FieldPolicy<any> | FieldReadFunction<any>,
	createPlaylistEntry?: FieldPolicy<any> | FieldReadFunction<any>,
	delPlaylistEntry?: FieldPolicy<any> | FieldReadFunction<any>,
	delPlaylistEntries?: FieldPolicy<any> | FieldReadFunction<any>,
	updatePlaylistEntry?: FieldPolicy<any> | FieldReadFunction<any>,
	createRelease?: FieldPolicy<any> | FieldReadFunction<any>,
	updateRelease?: FieldPolicy<any> | FieldReadFunction<any>,
	addArtistToRelease?: FieldPolicy<any> | FieldReadFunction<any>,
	delArtistFromRelease?: FieldPolicy<any> | FieldReadFunction<any>,
	updateTrack?: FieldPolicy<any> | FieldReadFunction<any>,
	addArtistToTrack?: FieldPolicy<any> | FieldReadFunction<any>,
	delArtistFromTrack?: FieldPolicy<any> | FieldReadFunction<any>
};
export type PlaylistKeySpecifier = ('id' | 'name' | 'starred' | 'type' | 'numTracks' | 'lastUpdatedOn' | 'imageId' | 'entries' | 'topGenres' | 'user' | PlaylistKeySpecifier)[];
export type PlaylistFieldPolicy = {
	id?: FieldPolicy<any> | FieldReadFunction<any>,
	name?: FieldPolicy<any> | FieldReadFunction<any>,
	starred?: FieldPolicy<any> | FieldReadFunction<any>,
	type?: FieldPolicy<any> | FieldReadFunction<any>,
	numTracks?: FieldPolicy<any> | FieldReadFunction<any>,
	lastUpdatedOn?: FieldPolicy<any> | FieldReadFunction<any>,
	imageId?: FieldPolicy<any> | FieldReadFunction<any>,
	entries?: FieldPolicy<any> | FieldReadFunction<any>,
	topGenres?: FieldPolicy<any> | FieldReadFunction<any>,
	user?: FieldPolicy<any> | FieldReadFunction<any>
};
export type PlaylistAndTrackKeySpecifier = ('playlist' | 'track' | PlaylistAndTrackKeySpecifier)[];
export type PlaylistAndTrackFieldPolicy = {
	playlist?: FieldPolicy<any> | FieldReadFunction<any>,
	track?: FieldPolicy<any> | FieldReadFunction<any>
};
export type PlaylistEntryKeySpecifier = ('id' | 'playlistId' | 'trackId' | 'position' | 'addedOn' | 'playlist' | 'track' | PlaylistEntryKeySpecifier)[];
export type PlaylistEntryFieldPolicy = {
	id?: FieldPolicy<any> | FieldReadFunction<any>,
	playlistId?: FieldPolicy<any> | FieldReadFunction<any>,
	trackId?: FieldPolicy<any> | FieldReadFunction<any>,
	position?: FieldPolicy<any> | FieldReadFunction<any>,
	addedOn?: FieldPolicy<any> | FieldReadFunction<any>,
	playlist?: FieldPolicy<any> | FieldReadFunction<any>,
	track?: FieldPolicy<any> | FieldReadFunction<any>
};
export type PlaylistsKeySpecifier = ('total' | 'results' | PlaylistsKeySpecifier)[];
export type PlaylistsFieldPolicy = {
	total?: FieldPolicy<any> | FieldReadFunction<any>,
	results?: FieldPolicy<any> | FieldReadFunction<any>
};
export type QueryKeySpecifier = ('user' | 'artists' | 'artist' | 'artistFromName' | 'collections' | 'collection' | 'collectionFromNameTypeUser' | 'invites' | 'invite' | 'playlists' | 'playlist' | 'playlistFromNameTypeUser' | 'releases' | 'release' | 'tracks' | 'track' | 'releaseYears' | QueryKeySpecifier)[];
export type QueryFieldPolicy = {
	user?: FieldPolicy<any> | FieldReadFunction<any>,
	artists?: FieldPolicy<any> | FieldReadFunction<any>,
	artist?: FieldPolicy<any> | FieldReadFunction<any>,
	artistFromName?: FieldPolicy<any> | FieldReadFunction<any>,
	collections?: FieldPolicy<any> | FieldReadFunction<any>,
	collection?: FieldPolicy<any> | FieldReadFunction<any>,
	collectionFromNameTypeUser?: FieldPolicy<any> | FieldReadFunction<any>,
	invites?: FieldPolicy<any> | FieldReadFunction<any>,
	invite?: FieldPolicy<any> | FieldReadFunction<any>,
	playlists?: FieldPolicy<any> | FieldReadFunction<any>,
	playlist?: FieldPolicy<any> | FieldReadFunction<any>,
	playlistFromNameTypeUser?: FieldPolicy<any> | FieldReadFunction<any>,
	releases?: FieldPolicy<any> | FieldReadFunction<any>,
	release?: FieldPolicy<any> | FieldReadFunction<any>,
	tracks?: FieldPolicy<any> | FieldReadFunction<any>,
	track?: FieldPolicy<any> | FieldReadFunction<any>,
	releaseYears?: FieldPolicy<any> | FieldReadFunction<any>
};
export type ReleaseKeySpecifier = ('id' | 'title' | 'releaseType' | 'addedOn' | 'inInbox' | 'inFavorites' | 'releaseYear' | 'releaseDate' | 'rating' | 'numTracks' | 'runtime' | 'imageId' | 'artists' | 'tracks' | 'genres' | 'labels' | 'collages' | ReleaseKeySpecifier)[];
export type ReleaseFieldPolicy = {
	id?: FieldPolicy<any> | FieldReadFunction<any>,
	title?: FieldPolicy<any> | FieldReadFunction<any>,
	releaseType?: FieldPolicy<any> | FieldReadFunction<any>,
	addedOn?: FieldPolicy<any> | FieldReadFunction<any>,
	inInbox?: FieldPolicy<any> | FieldReadFunction<any>,
	inFavorites?: FieldPolicy<any> | FieldReadFunction<any>,
	releaseYear?: FieldPolicy<any> | FieldReadFunction<any>,
	releaseDate?: FieldPolicy<any> | FieldReadFunction<any>,
	rating?: FieldPolicy<any> | FieldReadFunction<any>,
	numTracks?: FieldPolicy<any> | FieldReadFunction<any>,
	runtime?: FieldPolicy<any> | FieldReadFunction<any>,
	imageId?: FieldPolicy<any> | FieldReadFunction<any>,
	artists?: FieldPolicy<any> | FieldReadFunction<any>,
	tracks?: FieldPolicy<any> | FieldReadFunction<any>,
	genres?: FieldPolicy<any> | FieldReadFunction<any>,
	labels?: FieldPolicy<any> | FieldReadFunction<any>,
	collages?: FieldPolicy<any> | FieldReadFunction<any>
};
export type ReleaseAndArtistKeySpecifier = ('release' | 'artist' | ReleaseAndArtistKeySpecifier)[];
export type ReleaseAndArtistFieldPolicy = {
	release?: FieldPolicy<any> | FieldReadFunction<any>,
	artist?: FieldPolicy<any> | FieldReadFunction<any>
};
export type ReleasesKeySpecifier = ('total' | 'results' | ReleasesKeySpecifier)[];
export type ReleasesFieldPolicy = {
	total?: FieldPolicy<any> | FieldReadFunction<any>,
	results?: FieldPolicy<any> | FieldReadFunction<any>
};
export type TokenKeySpecifier = ('hex' | TokenKeySpecifier)[];
export type TokenFieldPolicy = {
	hex?: FieldPolicy<any> | FieldReadFunction<any>
};
export type TopGenreKeySpecifier = ('genre' | 'numMatches' | TopGenreKeySpecifier)[];
export type TopGenreFieldPolicy = {
	genre?: FieldPolicy<any> | FieldReadFunction<any>,
	numMatches?: FieldPolicy<any> | FieldReadFunction<any>
};
export type TrackKeySpecifier = ('id' | 'title' | 'duration' | 'trackNumber' | 'discNumber' | 'inFavorites' | 'release' | 'artists' | TrackKeySpecifier)[];
export type TrackFieldPolicy = {
	id?: FieldPolicy<any> | FieldReadFunction<any>,
	title?: FieldPolicy<any> | FieldReadFunction<any>,
	duration?: FieldPolicy<any> | FieldReadFunction<any>,
	trackNumber?: FieldPolicy<any> | FieldReadFunction<any>,
	discNumber?: FieldPolicy<any> | FieldReadFunction<any>,
	inFavorites?: FieldPolicy<any> | FieldReadFunction<any>,
	release?: FieldPolicy<any> | FieldReadFunction<any>,
	artists?: FieldPolicy<any> | FieldReadFunction<any>
};
export type TrackAndArtistKeySpecifier = ('track' | 'trackArtist' | TrackAndArtistKeySpecifier)[];
export type TrackAndArtistFieldPolicy = {
	track?: FieldPolicy<any> | FieldReadFunction<any>,
	trackArtist?: FieldPolicy<any> | FieldReadFunction<any>
};
export type TracksKeySpecifier = ('total' | 'results' | TracksKeySpecifier)[];
export type TracksFieldPolicy = {
	total?: FieldPolicy<any> | FieldReadFunction<any>,
	results?: FieldPolicy<any> | FieldReadFunction<any>
};
export type UserKeySpecifier = ('id' | 'nickname' | 'inboxCollectionId' | 'favoritesCollectionId' | 'favoritesPlaylistId' | UserKeySpecifier)[];
export type UserFieldPolicy = {
	id?: FieldPolicy<any> | FieldReadFunction<any>,
	nickname?: FieldPolicy<any> | FieldReadFunction<any>,
	inboxCollectionId?: FieldPolicy<any> | FieldReadFunction<any>,
	favoritesCollectionId?: FieldPolicy<any> | FieldReadFunction<any>,
	favoritesPlaylistId?: FieldPolicy<any> | FieldReadFunction<any>
};
export type TypedTypePolicies = TypePolicies & {
	Artist?: Omit<TypePolicy, "fields" | "keyFields"> & {
		keyFields?: false | ArtistKeySpecifier | (() => undefined | ArtistKeySpecifier),
		fields?: ArtistFieldPolicy,
	},
	ArtistWithRole?: Omit<TypePolicy, "fields" | "keyFields"> & {
		keyFields?: false | ArtistWithRoleKeySpecifier | (() => undefined | ArtistWithRoleKeySpecifier),
		fields?: ArtistWithRoleFieldPolicy,
	},
	Artists?: Omit<TypePolicy, "fields" | "keyFields"> & {
		keyFields?: false | ArtistsKeySpecifier | (() => undefined | ArtistsKeySpecifier),
		fields?: ArtistsFieldPolicy,
	},
	Collection?: Omit<TypePolicy, "fields" | "keyFields"> & {
		keyFields?: false | CollectionKeySpecifier | (() => undefined | CollectionKeySpecifier),
		fields?: CollectionFieldPolicy,
	},
	CollectionAndRelease?: Omit<TypePolicy, "fields" | "keyFields"> & {
		keyFields?: false | CollectionAndReleaseKeySpecifier | (() => undefined | CollectionAndReleaseKeySpecifier),
		fields?: CollectionAndReleaseFieldPolicy,
	},
	Collections?: Omit<TypePolicy, "fields" | "keyFields"> & {
		keyFields?: false | CollectionsKeySpecifier | (() => undefined | CollectionsKeySpecifier),
		fields?: CollectionsFieldPolicy,
	},
	Invite?: Omit<TypePolicy, "fields" | "keyFields"> & {
		keyFields?: false | InviteKeySpecifier | (() => undefined | InviteKeySpecifier),
		fields?: InviteFieldPolicy,
	},
	Invites?: Omit<TypePolicy, "fields" | "keyFields"> & {
		keyFields?: false | InvitesKeySpecifier | (() => undefined | InvitesKeySpecifier),
		fields?: InvitesFieldPolicy,
	},
	Mutation?: Omit<TypePolicy, "fields" | "keyFields"> & {
		keyFields?: false | MutationKeySpecifier | (() => undefined | MutationKeySpecifier),
		fields?: MutationFieldPolicy,
	},
	Playlist?: Omit<TypePolicy, "fields" | "keyFields"> & {
		keyFields?: false | PlaylistKeySpecifier | (() => undefined | PlaylistKeySpecifier),
		fields?: PlaylistFieldPolicy,
	},
	PlaylistAndTrack?: Omit<TypePolicy, "fields" | "keyFields"> & {
		keyFields?: false | PlaylistAndTrackKeySpecifier | (() => undefined | PlaylistAndTrackKeySpecifier),
		fields?: PlaylistAndTrackFieldPolicy,
	},
	PlaylistEntry?: Omit<TypePolicy, "fields" | "keyFields"> & {
		keyFields?: false | PlaylistEntryKeySpecifier | (() => undefined | PlaylistEntryKeySpecifier),
		fields?: PlaylistEntryFieldPolicy,
	},
	Playlists?: Omit<TypePolicy, "fields" | "keyFields"> & {
		keyFields?: false | PlaylistsKeySpecifier | (() => undefined | PlaylistsKeySpecifier),
		fields?: PlaylistsFieldPolicy,
	},
	Query?: Omit<TypePolicy, "fields" | "keyFields"> & {
		keyFields?: false | QueryKeySpecifier | (() => undefined | QueryKeySpecifier),
		fields?: QueryFieldPolicy,
	},
	Release?: Omit<TypePolicy, "fields" | "keyFields"> & {
		keyFields?: false | ReleaseKeySpecifier | (() => undefined | ReleaseKeySpecifier),
		fields?: ReleaseFieldPolicy,
	},
	ReleaseAndArtist?: Omit<TypePolicy, "fields" | "keyFields"> & {
		keyFields?: false | ReleaseAndArtistKeySpecifier | (() => undefined | ReleaseAndArtistKeySpecifier),
		fields?: ReleaseAndArtistFieldPolicy,
	},
	Releases?: Omit<TypePolicy, "fields" | "keyFields"> & {
		keyFields?: false | ReleasesKeySpecifier | (() => undefined | ReleasesKeySpecifier),
		fields?: ReleasesFieldPolicy,
	},
	Token?: Omit<TypePolicy, "fields" | "keyFields"> & {
		keyFields?: false | TokenKeySpecifier | (() => undefined | TokenKeySpecifier),
		fields?: TokenFieldPolicy,
	},
	TopGenre?: Omit<TypePolicy, "fields" | "keyFields"> & {
		keyFields?: false | TopGenreKeySpecifier | (() => undefined | TopGenreKeySpecifier),
		fields?: TopGenreFieldPolicy,
	},
	Track?: Omit<TypePolicy, "fields" | "keyFields"> & {
		keyFields?: false | TrackKeySpecifier | (() => undefined | TrackKeySpecifier),
		fields?: TrackFieldPolicy,
	},
	TrackAndArtist?: Omit<TypePolicy, "fields" | "keyFields"> & {
		keyFields?: false | TrackAndArtistKeySpecifier | (() => undefined | TrackAndArtistKeySpecifier),
		fields?: TrackAndArtistFieldPolicy,
	},
	Tracks?: Omit<TypePolicy, "fields" | "keyFields"> & {
		keyFields?: false | TracksKeySpecifier | (() => undefined | TracksKeySpecifier),
		fields?: TracksFieldPolicy,
	},
	User?: Omit<TypePolicy, "fields" | "keyFields"> & {
		keyFields?: false | UserKeySpecifier | (() => undefined | UserKeySpecifier),
		fields?: UserFieldPolicy,
	}
};