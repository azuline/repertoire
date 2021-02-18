import { gql } from '@apollo/client';
import * as Apollo from '@apollo/client';
import { FieldPolicy, FieldReadFunction, TypePolicies, TypePolicy } from '@apollo/client/cache';
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
  PosixTime: number;
};


export type IQuery = {
  __typename?: 'Query';
  artist: Maybe<IArtist>;
  artistFromName: Maybe<IArtist>;
  collection: Maybe<ICollection>;
  collectionFromNameAndType: Maybe<ICollection>;
  playlist: Maybe<IPlaylist>;
  playlistFromNameAndType: Maybe<IPlaylist>;
  release: Maybe<IRelease>;
  track: Maybe<ITrack>;
  /** Fetch the currently authenticated user. */
  user: Maybe<IUser>;
  /** Fetch all artists. */
  artists: Maybe<IArtists>;
  /** Fetch all collections (of one or more types). */
  collections: Maybe<ICollections>;
  /** Fetch all playlists (of one or more types). */
  playlists: Maybe<IPlaylists>;
  /** Search for releases matching a certain criteria. */
  releases: Maybe<IReleases>;
  /** Fetch all existing release years sorted in descending order. */
  releaseYears: Maybe<Array<Maybe<Scalars['Int']>>>;
};


export type IQueryArtistArgs = {
  id: Scalars['Int'];
};


export type IQueryArtistFromNameArgs = {
  name: Scalars['String'];
};


export type IQueryCollectionArgs = {
  id: Scalars['Int'];
};


export type IQueryCollectionFromNameAndTypeArgs = {
  name: Scalars['String'];
  type: ICollectionType;
};


export type IQueryPlaylistArgs = {
  id: Scalars['Int'];
};


export type IQueryPlaylistFromNameAndTypeArgs = {
  name: Scalars['String'];
  type: IPlaylistType;
};


export type IQueryReleaseArgs = {
  id: Scalars['Int'];
};


export type IQueryTrackArgs = {
  id: Scalars['Int'];
};


export type IQueryCollectionsArgs = {
  types: Maybe<Array<Maybe<ICollectionType>>>;
};


export type IQueryPlaylistsArgs = {
  types: Maybe<Array<Maybe<IPlaylistType>>>;
};


export type IQueryReleasesArgs = {
  search: Maybe<Scalars['String']>;
  collectionIds: Maybe<Array<Maybe<Scalars['Int']>>>;
  artistIds: Maybe<Array<Maybe<Scalars['Int']>>>;
  releaseTypes: Maybe<Array<Maybe<IReleaseType>>>;
  years: Maybe<Array<Maybe<Scalars['Int']>>>;
  ratings: Maybe<Array<Maybe<Scalars['Int']>>>;
  page: Maybe<Scalars['Int']>;
  perPage: Maybe<Scalars['Int']>;
  sort: Maybe<IReleaseSort>;
  asc: Maybe<Scalars['Boolean']>;
};

export type IMutation = {
  __typename?: 'Mutation';
  createArtist: Maybe<IArtist>;
  updateArtist: Maybe<IArtist>;
  createCollection: Maybe<ICollection>;
  updateCollection: Maybe<ICollection>;
  addReleaseToCollection: Maybe<ICollectionAndRelease>;
  delReleaseFromCollection: Maybe<ICollectionAndRelease>;
  createPlaylist: Maybe<IPlaylist>;
  updatePlaylist: Maybe<IPlaylist>;
  createPlaylistEntry: Maybe<IPlaylistEntry>;
  delPlaylistEntry: Maybe<IPlaylist>;
  updatePlaylistEntry: Maybe<IPlaylistEntry>;
  createRelease: Maybe<IRelease>;
  updateRelease: Maybe<IRelease>;
  addArtistToRelease: Maybe<IReleaseAndArtist>;
  delArtistFromRelease: Maybe<IReleaseAndArtist>;
  updateTrack: Maybe<ITrack>;
  addArtistToTrack: Maybe<ITrackAndArtist>;
  delArtistFromTrack: Maybe<ITrackAndArtist>;
  /** Update the authenticated user. */
  updateUser: Maybe<IUser>;
  /**
   * Generate a new authentication token for the current user. Invalidate the
   * old one.
   */
  newToken: Maybe<IToken>;
};


export type IMutationCreateArtistArgs = {
  name: Scalars['String'];
  starred: Maybe<Scalars['Boolean']>;
};


export type IMutationUpdateArtistArgs = {
  id: Scalars['Int'];
  name: Maybe<Scalars['String']>;
  starred: Maybe<Scalars['Boolean']>;
};


export type IMutationCreateCollectionArgs = {
  name: Scalars['String'];
  type: ICollectionType;
  starred: Maybe<Scalars['Boolean']>;
};


export type IMutationUpdateCollectionArgs = {
  id: Scalars['Int'];
  name: Maybe<Scalars['String']>;
  starred: Maybe<Scalars['Boolean']>;
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
  starred: Maybe<Scalars['Boolean']>;
};


export type IMutationUpdatePlaylistArgs = {
  id: Scalars['Int'];
  name: Maybe<Scalars['String']>;
  starred: Maybe<Scalars['Boolean']>;
};


export type IMutationCreatePlaylistEntryArgs = {
  playlistId: Scalars['Int'];
  trackId: Scalars['Int'];
};


export type IMutationDelPlaylistEntryArgs = {
  id: Scalars['Int'];
};


export type IMutationUpdatePlaylistEntryArgs = {
  id: Scalars['Int'];
  position: Scalars['Int'];
};


export type IMutationCreateReleaseArgs = {
  title: Scalars['String'];
  artistIds: Array<Maybe<Scalars['Int']>>;
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
};


export type IMutationDelArtistFromReleaseArgs = {
  releaseId: Scalars['Int'];
  artistId: Scalars['Int'];
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


export type IMutationUpdateUserArgs = {
  nickname: Maybe<Scalars['String']>;
};

export type IArtist = {
  __typename?: 'Artist';
  id: Scalars['Int'];
  name: Scalars['String'];
  starred: Scalars['Boolean'];
  numReleases: Scalars['Int'];
  /** The image ID of one of the artist's releases. Potentially null. */
  imageId: Maybe<Scalars['Int']>;
  releases: Array<Maybe<IRelease>>;
  /** The top genres of the artist, compiled from their releases. */
  topGenres: Array<Maybe<ITopGenre>>;
};

export type IArtists = {
  __typename?: 'Artists';
  results: Array<Maybe<IArtist>>;
};

export type ICollection = {
  __typename?: 'Collection';
  id: Scalars['Int'];
  name: Scalars['String'];
  starred: Scalars['Boolean'];
  type: ICollectionType;
  numReleases: Scalars['Int'];
  /** The last datetime a release was added to the collection. */
  lastUpdatedOn: Maybe<Scalars['PosixTime']>;
  /** The image ID of a release in the collection. Potentially null. */
  imageId: Maybe<Scalars['Int']>;
  releases: Array<Maybe<IRelease>>;
  /** The top genres of the collection, compiled from its releases. */
  topGenres: Array<Maybe<ITopGenre>>;
};

export type ICollections = {
  __typename?: 'Collections';
  results: Array<Maybe<ICollection>>;
};

export type IPlaylist = {
  __typename?: 'Playlist';
  id: Scalars['Int'];
  name: Scalars['String'];
  starred: Scalars['Boolean'];
  type: IPlaylistType;
  numTracks: Scalars['Int'];
  /** The last datetime a release was added to the playlist. */
  lastUpdatedOn: Maybe<Scalars['PosixTime']>;
  /** The image ID of a track in the playlst. Potentially null. */
  imageId: Maybe<Scalars['Int']>;
  entries: Array<Maybe<IPlaylistEntry>>;
  /** The top genres of the playlist, compiled from its tracks. */
  topGenres: Array<Maybe<ITopGenre>>;
};

export type IPlaylists = {
  __typename?: 'Playlists';
  results: Array<Maybe<IPlaylist>>;
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

export type IRelease = {
  __typename?: 'Release';
  id: Scalars['Int'];
  title: Scalars['String'];
  releaseType: IReleaseType;
  addedOn: Scalars['PosixTime'];
  inInbox: Scalars['Boolean'];
  inFavorites: Scalars['Boolean'];
  releaseYear: Maybe<Scalars['Int']>;
  /** The date that the release was released in YYYY-MM-DD format (Optional). */
  releaseDate: Maybe<Scalars['String']>;
  /** The release rating, either null or an int on the interval [1, 10]. */
  rating: Maybe<Scalars['Int']>;
  numTracks: Scalars['Int'];
  /** The total runtime (sum of track durations). */
  runtime: Scalars['Int'];
  /** The image ID of the release's cover image. Potentially null. */
  imageId: Maybe<Scalars['Int']>;
  artists: Array<Maybe<IArtist>>;
  tracks: Array<Maybe<ITrack>>;
  genres: Array<Maybe<ICollection>>;
  labels: Array<Maybe<ICollection>>;
  collages: Array<Maybe<ICollection>>;
};

export type IReleases = {
  __typename?: 'Releases';
  /** The total number of releases matching the query across all pages. */
  total: Scalars['Int'];
  /** The releases on the current page. */
  results: Array<Maybe<IRelease>>;
};

export type ITrack = {
  __typename?: 'Track';
  id: Scalars['Int'];
  title: Scalars['String'];
  duration: Scalars['Int'];
  trackNumber: Scalars['String'];
  discNumber: Scalars['String'];
  release: IRelease;
  artists: Array<Maybe<ITrackArtist>>;
};

export type ITrackArtist = {
  __typename?: 'TrackArtist';
  artist: IArtist;
  /** The role that the artist has on the track. */
  role: IArtistRole;
};

/** A type that represents the top genres of an artist/collection. */
export type ITopGenre = {
  __typename?: 'TopGenre';
  genre: ICollection;
  /** The number of releases in the artist/collection that match this genre. */
  numMatches: Scalars['Int'];
};

export type IUser = {
  __typename?: 'User';
  id: Scalars['Int'];
  nickname: Scalars['String'];
};

export type IToken = {
  __typename?: 'Token';
  hex: Scalars['String'];
};

export type ICollectionAndRelease = {
  __typename?: 'CollectionAndRelease';
  collection: ICollection;
  release: IRelease;
};

export type IReleaseAndArtist = {
  __typename?: 'ReleaseAndArtist';
  release: IRelease;
  artist: IArtist;
};

export type ITrackAndArtist = {
  __typename?: 'TrackAndArtist';
  track: ITrack;
  trackArtist: ITrackArtist;
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

export enum ICollectionType {
  System = 'SYSTEM',
  Collage = 'COLLAGE',
  Label = 'LABEL',
  Genre = 'GENRE'
}

export enum IReleaseSort {
  RecentlyAdded = 'RECENTLY_ADDED',
  Title = 'TITLE',
  Year = 'YEAR',
  Rating = 'RATING',
  Random = 'RANDOM'
}

export enum IPlaylistType {
  System = 'SYSTEM',
  Playlist = 'PLAYLIST'
}

export type IHeaderFetchUserQueryVariables = Exact<{ [key: string]: never; }>;


export type IHeaderFetchUserQuery = (
  { __typename?: 'Query' }
  & { user: Maybe<(
    { __typename?: 'User' }
    & IUserFieldsFragment
  )> }
);

export type IPagedReleasesFetchReleasesQueryVariables = Exact<{
  search: Maybe<Scalars['String']>;
  collectionIds: Maybe<Array<Maybe<Scalars['Int']>> | Maybe<Scalars['Int']>>;
  artistIds: Maybe<Array<Maybe<Scalars['Int']>> | Maybe<Scalars['Int']>>;
  releaseTypes: Maybe<Array<Maybe<IReleaseType>> | Maybe<IReleaseType>>;
  years: Maybe<Array<Maybe<Scalars['Int']>> | Maybe<Scalars['Int']>>;
  ratings: Maybe<Array<Maybe<Scalars['Int']>> | Maybe<Scalars['Int']>>;
  page: Maybe<Scalars['Int']>;
  perPage: Maybe<Scalars['Int']>;
  sort: Maybe<IReleaseSort>;
  asc: Maybe<Scalars['Boolean']>;
}>;


export type IPagedReleasesFetchReleasesQuery = (
  { __typename?: 'Query' }
  & { releases: Maybe<(
    { __typename?: 'Releases' }
    & Pick<IReleases, 'total'>
    & { results: Array<Maybe<(
      { __typename?: 'Release' }
      & { artists: Array<Maybe<(
        { __typename?: 'Artist' }
        & Pick<IArtist, 'id' | 'name'>
      )>>, genres: Array<Maybe<(
        { __typename?: 'Collection' }
        & Pick<ICollection, 'id' | 'name'>
      )>> }
      & IReleaseFieldsFragment
    )>> }
  )> }
);

export type ICollectionChooserFetchCollectionsQueryVariables = Exact<{
  types: Maybe<Array<Maybe<ICollectionType>> | Maybe<ICollectionType>>;
}>;


export type ICollectionChooserFetchCollectionsQuery = (
  { __typename?: 'Query' }
  & { collections: Maybe<(
    { __typename?: 'Collections' }
    & { results: Array<Maybe<(
      { __typename?: 'Collection' }
      & ICollectionFieldsFragment
    )>> }
  )> }
);

export type ICollectionChooserUpdateCollectionStarredMutationVariables = Exact<{
  id: Scalars['Int'];
  starred: Maybe<Scalars['Boolean']>;
}>;


export type ICollectionChooserUpdateCollectionStarredMutation = (
  { __typename?: 'Mutation' }
  & { updateCollection: Maybe<(
    { __typename?: 'Collection' }
    & Pick<ICollection, 'id' | 'starred'>
  )> }
);

export type IUserFieldsFragment = (
  { __typename?: 'User' }
  & Pick<IUser, 'id' | 'nickname'>
);

export type IReleaseFieldsFragment = (
  { __typename?: 'Release' }
  & Pick<IRelease, 'id' | 'title' | 'releaseType' | 'addedOn' | 'inInbox' | 'inFavorites' | 'releaseYear' | 'releaseDate' | 'rating' | 'numTracks' | 'runtime' | 'imageId'>
);

export type IArtistFieldsFragment = (
  { __typename?: 'Artist' }
  & Pick<IArtist, 'id' | 'name' | 'starred' | 'numReleases' | 'imageId'>
);

export type ICollectionFieldsFragment = (
  { __typename?: 'Collection' }
  & Pick<ICollection, 'id' | 'name' | 'starred' | 'type' | 'numReleases' | 'lastUpdatedOn' | 'imageId'>
);

export type ITrackFieldsFragment = (
  { __typename?: 'Track' }
  & Pick<ITrack, 'id' | 'title' | 'duration' | 'trackNumber' | 'discNumber'>
);

export type IFullReleaseFieldsFragment = (
  { __typename?: 'Release' }
  & { artists: Array<Maybe<(
    { __typename?: 'Artist' }
    & Pick<IArtist, 'id' | 'name'>
  )>>, collages: Array<Maybe<(
    { __typename?: 'Collection' }
    & Pick<ICollection, 'id' | 'name'>
  )>>, labels: Array<Maybe<(
    { __typename?: 'Collection' }
    & Pick<ICollection, 'id' | 'name'>
  )>>, genres: Array<Maybe<(
    { __typename?: 'Collection' }
    & Pick<ICollection, 'id' | 'name'>
  )>>, tracks: Array<Maybe<(
    { __typename?: 'Track' }
    & { release: (
      { __typename?: 'Release' }
      & Pick<IRelease, 'id' | 'imageId'>
    ), artists: Array<Maybe<(
      { __typename?: 'TrackArtist' }
      & Pick<ITrackArtist, 'role'>
      & { artist: (
        { __typename?: 'Artist' }
        & Pick<IArtist, 'id' | 'name'>
      ) }
    )>> }
    & ITrackFieldsFragment
  )>> }
  & IReleaseFieldsFragment
);

export type IArtistsFetchArtistQueryVariables = Exact<{
  id: Scalars['Int'];
}>;


export type IArtistsFetchArtistQuery = (
  { __typename?: 'Query' }
  & { artist: Maybe<(
    { __typename?: 'Artist' }
    & IArtistFieldsFragment
  )> }
);

export type IArtistChooserFetchArtistsQueryVariables = Exact<{ [key: string]: never; }>;


export type IArtistChooserFetchArtistsQuery = (
  { __typename?: 'Query' }
  & { artists: Maybe<(
    { __typename?: 'Artists' }
    & { results: Array<Maybe<(
      { __typename?: 'Artist' }
      & IArtistFieldsFragment
    )>> }
  )> }
);

export type IArtistChooserUpdateArtistStarredMutationVariables = Exact<{
  id: Scalars['Int'];
  starred: Maybe<Scalars['Boolean']>;
}>;


export type IArtistChooserUpdateArtistStarredMutation = (
  { __typename?: 'Mutation' }
  & { updateArtist: Maybe<(
    { __typename?: 'Artist' }
    & Pick<IArtist, 'id' | 'starred'>
  )> }
);

export type ICollageFetchCollageQueryVariables = Exact<{
  id: Scalars['Int'];
}>;


export type ICollageFetchCollageQuery = (
  { __typename?: 'Query' }
  & { collection: Maybe<(
    { __typename?: 'Collection' }
    & ICollectionFieldsFragment
  )> }
);

export type IRecentlyAddedFetchReleasesQueryVariables = Exact<{ [key: string]: never; }>;


export type IRecentlyAddedFetchReleasesQuery = (
  { __typename?: 'Query' }
  & { releases: Maybe<(
    { __typename?: 'Releases' }
    & { results: Array<Maybe<(
      { __typename?: 'Release' }
      & { artists: Array<Maybe<(
        { __typename?: 'Artist' }
        & Pick<IArtist, 'id' | 'name'>
      )>>, genres: Array<Maybe<(
        { __typename?: 'Collection' }
        & Pick<ICollection, 'id' | 'name'>
      )>> }
      & IReleaseFieldsFragment
    )>> }
  )> }
);

export type IGenresFetchGenreQueryVariables = Exact<{
  id: Scalars['Int'];
}>;


export type IGenresFetchGenreQuery = (
  { __typename?: 'Query' }
  & { collection: Maybe<(
    { __typename?: 'Collection' }
    & ICollectionFieldsFragment
  )> }
);

export type ILabelFetchLabelQueryVariables = Exact<{
  id: Scalars['Int'];
}>;


export type ILabelFetchLabelQuery = (
  { __typename?: 'Query' }
  & { collection: Maybe<(
    { __typename?: 'Collection' }
    & ICollectionFieldsFragment
  )> }
);

export type INowPlayingInfoFetchReleaseQueryVariables = Exact<{
  id: Scalars['Int'];
}>;


export type INowPlayingInfoFetchReleaseQuery = (
  { __typename?: 'Query' }
  & { release: Maybe<(
    { __typename?: 'Release' }
    & IFullReleaseFieldsFragment
  )> }
);

export type IInFavoritesAddReleaseToCollectionMutationVariables = Exact<{
  collectionId: Scalars['Int'];
  releaseId: Scalars['Int'];
}>;


export type IInFavoritesAddReleaseToCollectionMutation = (
  { __typename?: 'Mutation' }
  & { addReleaseToCollection: Maybe<(
    { __typename?: 'CollectionAndRelease' }
    & { collection: (
      { __typename?: 'Collection' }
      & Pick<ICollection, 'id' | 'numReleases' | 'lastUpdatedOn'>
    ), release: (
      { __typename?: 'Release' }
      & Pick<IRelease, 'id' | 'inInbox' | 'inFavorites'>
      & { genres: Array<Maybe<(
        { __typename?: 'Collection' }
        & Pick<ICollection, 'id' | 'name'>
      )>>, labels: Array<Maybe<(
        { __typename?: 'Collection' }
        & Pick<ICollection, 'id' | 'name'>
      )>>, collages: Array<Maybe<(
        { __typename?: 'Collection' }
        & Pick<ICollection, 'id' | 'name'>
      )>> }
    ) }
  )> }
);

export type IInFavoritesDelReleaseFromCollectionMutationVariables = Exact<{
  collectionId: Scalars['Int'];
  releaseId: Scalars['Int'];
}>;


export type IInFavoritesDelReleaseFromCollectionMutation = (
  { __typename?: 'Mutation' }
  & { delReleaseFromCollection: Maybe<(
    { __typename?: 'CollectionAndRelease' }
    & { collection: (
      { __typename?: 'Collection' }
      & Pick<ICollection, 'id' | 'numReleases' | 'lastUpdatedOn'>
    ), release: (
      { __typename?: 'Release' }
      & Pick<IRelease, 'id' | 'inInbox' | 'inFavorites'>
      & { genres: Array<Maybe<(
        { __typename?: 'Collection' }
        & Pick<ICollection, 'id' | 'name'>
      )>>, labels: Array<Maybe<(
        { __typename?: 'Collection' }
        & Pick<ICollection, 'id' | 'name'>
      )>>, collages: Array<Maybe<(
        { __typename?: 'Collection' }
        & Pick<ICollection, 'id' | 'name'>
      )>> }
    ) }
  )> }
);

export type IInInboxAddReleaseToCollectionMutationVariables = Exact<{
  collectionId: Scalars['Int'];
  releaseId: Scalars['Int'];
}>;


export type IInInboxAddReleaseToCollectionMutation = (
  { __typename?: 'Mutation' }
  & { addReleaseToCollection: Maybe<(
    { __typename?: 'CollectionAndRelease' }
    & { collection: (
      { __typename?: 'Collection' }
      & Pick<ICollection, 'id' | 'numReleases' | 'lastUpdatedOn'>
    ), release: (
      { __typename?: 'Release' }
      & Pick<IRelease, 'id' | 'inInbox' | 'inFavorites'>
      & { genres: Array<Maybe<(
        { __typename?: 'Collection' }
        & Pick<ICollection, 'id' | 'name'>
      )>>, labels: Array<Maybe<(
        { __typename?: 'Collection' }
        & Pick<ICollection, 'id' | 'name'>
      )>>, collages: Array<Maybe<(
        { __typename?: 'Collection' }
        & Pick<ICollection, 'id' | 'name'>
      )>> }
    ) }
  )> }
);

export type IInInboxDelReleaseFromCollectionMutationVariables = Exact<{
  collectionId: Scalars['Int'];
  releaseId: Scalars['Int'];
}>;


export type IInInboxDelReleaseFromCollectionMutation = (
  { __typename?: 'Mutation' }
  & { delReleaseFromCollection: Maybe<(
    { __typename?: 'CollectionAndRelease' }
    & { collection: (
      { __typename?: 'Collection' }
      & Pick<ICollection, 'id' | 'numReleases' | 'lastUpdatedOn'>
    ), release: (
      { __typename?: 'Release' }
      & Pick<IRelease, 'id' | 'inInbox' | 'inFavorites'>
      & { genres: Array<Maybe<(
        { __typename?: 'Collection' }
        & Pick<ICollection, 'id' | 'name'>
      )>>, labels: Array<Maybe<(
        { __typename?: 'Collection' }
        & Pick<ICollection, 'id' | 'name'>
      )>>, collages: Array<Maybe<(
        { __typename?: 'Collection' }
        & Pick<ICollection, 'id' | 'name'>
      )>> }
    ) }
  )> }
);

export type IReleaseUpdateReleaseRatingMutationVariables = Exact<{
  id: Scalars['Int'];
  rating: Maybe<Scalars['Int']>;
}>;


export type IReleaseUpdateReleaseRatingMutation = (
  { __typename?: 'Mutation' }
  & { updateRelease: Maybe<(
    { __typename?: 'Release' }
    & Pick<IRelease, 'id' | 'rating'>
  )> }
);

export type IReleaseFetchReleaseQueryVariables = Exact<{
  id: Scalars['Int'];
}>;


export type IReleaseFetchReleaseQuery = (
  { __typename?: 'Query' }
  & { release: Maybe<(
    { __typename?: 'Release' }
    & IFullReleaseFieldsFragment
  )> }
);

export type ISettingsFetchUserQueryVariables = Exact<{ [key: string]: never; }>;


export type ISettingsFetchUserQuery = (
  { __typename?: 'Query' }
  & { user: Maybe<(
    { __typename?: 'User' }
    & IUserFieldsFragment
  )> }
);

export type ISettingsUpdateUserMutationVariables = Exact<{
  nickname: Maybe<Scalars['String']>;
}>;


export type ISettingsUpdateUserMutation = (
  { __typename?: 'Mutation' }
  & { updateUser: Maybe<(
    { __typename?: 'User' }
    & Pick<IUser, 'id' | 'nickname'>
  )> }
);

export type IYearsFetchReleaseYearsQueryVariables = Exact<{ [key: string]: never; }>;


export type IYearsFetchReleaseYearsQuery = (
  { __typename?: 'Query' }
  & Pick<IQuery, 'releaseYears'>
);

export const UserFieldsFragmentDoc = gql`
    fragment UserFields on User {
  id
  nickname
}
    `;
export const ArtistFieldsFragmentDoc = gql`
    fragment ArtistFields on Artist {
  id
  name
  starred
  numReleases
  imageId
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
}
    `;
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
}
    `;
export const TrackFieldsFragmentDoc = gql`
    fragment TrackFields on Track {
  id
  title
  duration
  trackNumber
  discNumber
}
    `;
export const FullReleaseFieldsFragmentDoc = gql`
    fragment FullReleaseFields on Release {
  ...ReleaseFields
  artists {
    id
    name
  }
  collages {
    id
    name
  }
  labels {
    id
    name
  }
  genres {
    id
    name
  }
  tracks {
    ...TrackFields
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
        return Apollo.useQuery<IHeaderFetchUserQuery, IHeaderFetchUserQueryVariables>(HeaderFetchUserDocument, baseOptions);
      }
export function useHeaderFetchUserLazyQuery(baseOptions?: Apollo.LazyQueryHookOptions<IHeaderFetchUserQuery, IHeaderFetchUserQueryVariables>) {
          return Apollo.useLazyQuery<IHeaderFetchUserQuery, IHeaderFetchUserQueryVariables>(HeaderFetchUserDocument, baseOptions);
        }
export type HeaderFetchUserQueryHookResult = ReturnType<typeof useHeaderFetchUserQuery>;
export type HeaderFetchUserLazyQueryHookResult = ReturnType<typeof useHeaderFetchUserLazyQuery>;
export type HeaderFetchUserQueryResult = Apollo.QueryResult<IHeaderFetchUserQuery, IHeaderFetchUserQueryVariables>;
export const PagedReleasesFetchReleasesDocument = gql`
    query PagedReleasesFetchReleases($search: String, $collectionIds: [Int], $artistIds: [Int], $releaseTypes: [ReleaseType], $years: [Int], $ratings: [Int], $page: Int, $perPage: Int, $sort: ReleaseSort, $asc: Boolean) {
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
      artists {
        id
        name
      }
      genres {
        id
        name
      }
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
        return Apollo.useQuery<IPagedReleasesFetchReleasesQuery, IPagedReleasesFetchReleasesQueryVariables>(PagedReleasesFetchReleasesDocument, baseOptions);
      }
export function usePagedReleasesFetchReleasesLazyQuery(baseOptions?: Apollo.LazyQueryHookOptions<IPagedReleasesFetchReleasesQuery, IPagedReleasesFetchReleasesQueryVariables>) {
          return Apollo.useLazyQuery<IPagedReleasesFetchReleasesQuery, IPagedReleasesFetchReleasesQueryVariables>(PagedReleasesFetchReleasesDocument, baseOptions);
        }
export type PagedReleasesFetchReleasesQueryHookResult = ReturnType<typeof usePagedReleasesFetchReleasesQuery>;
export type PagedReleasesFetchReleasesLazyQueryHookResult = ReturnType<typeof usePagedReleasesFetchReleasesLazyQuery>;
export type PagedReleasesFetchReleasesQueryResult = Apollo.QueryResult<IPagedReleasesFetchReleasesQuery, IPagedReleasesFetchReleasesQueryVariables>;
export const CollectionChooserFetchCollectionsDocument = gql`
    query CollectionChooserFetchCollections($types: [CollectionType]) {
  collections(types: $types) {
    results {
      ...CollectionFields
    }
  }
}
    ${CollectionFieldsFragmentDoc}`;

/**
 * __useCollectionChooserFetchCollectionsQuery__
 *
 * To run a query within a React component, call `useCollectionChooserFetchCollectionsQuery` and pass it any options that fit your needs.
 * When your component renders, `useCollectionChooserFetchCollectionsQuery` returns an object from Apollo Client that contains loading, error, and data properties
 * you can use to render your UI.
 *
 * @param baseOptions options that will be passed into the query, supported options are listed on: https://www.apollographql.com/docs/react/api/react-hooks/#options;
 *
 * @example
 * const { data, loading, error } = useCollectionChooserFetchCollectionsQuery({
 *   variables: {
 *      types: // value for 'types'
 *   },
 * });
 */
export function useCollectionChooserFetchCollectionsQuery(baseOptions?: Apollo.QueryHookOptions<ICollectionChooserFetchCollectionsQuery, ICollectionChooserFetchCollectionsQueryVariables>) {
        return Apollo.useQuery<ICollectionChooserFetchCollectionsQuery, ICollectionChooserFetchCollectionsQueryVariables>(CollectionChooserFetchCollectionsDocument, baseOptions);
      }
export function useCollectionChooserFetchCollectionsLazyQuery(baseOptions?: Apollo.LazyQueryHookOptions<ICollectionChooserFetchCollectionsQuery, ICollectionChooserFetchCollectionsQueryVariables>) {
          return Apollo.useLazyQuery<ICollectionChooserFetchCollectionsQuery, ICollectionChooserFetchCollectionsQueryVariables>(CollectionChooserFetchCollectionsDocument, baseOptions);
        }
export type CollectionChooserFetchCollectionsQueryHookResult = ReturnType<typeof useCollectionChooserFetchCollectionsQuery>;
export type CollectionChooserFetchCollectionsLazyQueryHookResult = ReturnType<typeof useCollectionChooserFetchCollectionsLazyQuery>;
export type CollectionChooserFetchCollectionsQueryResult = Apollo.QueryResult<ICollectionChooserFetchCollectionsQuery, ICollectionChooserFetchCollectionsQueryVariables>;
export const CollectionChooserUpdateCollectionStarredDocument = gql`
    mutation CollectionChooserUpdateCollectionStarred($id: Int!, $starred: Boolean) {
  updateCollection(id: $id, starred: $starred) {
    id
    starred
  }
}
    `;
export type ICollectionChooserUpdateCollectionStarredMutationFn = Apollo.MutationFunction<ICollectionChooserUpdateCollectionStarredMutation, ICollectionChooserUpdateCollectionStarredMutationVariables>;

/**
 * __useCollectionChooserUpdateCollectionStarredMutation__
 *
 * To run a mutation, you first call `useCollectionChooserUpdateCollectionStarredMutation` within a React component and pass it any options that fit your needs.
 * When your component renders, `useCollectionChooserUpdateCollectionStarredMutation` returns a tuple that includes:
 * - A mutate function that you can call at any time to execute the mutation
 * - An object with fields that represent the current status of the mutation's execution
 *
 * @param baseOptions options that will be passed into the mutation, supported options are listed on: https://www.apollographql.com/docs/react/api/react-hooks/#options-2;
 *
 * @example
 * const [collectionChooserUpdateCollectionStarredMutation, { data, loading, error }] = useCollectionChooserUpdateCollectionStarredMutation({
 *   variables: {
 *      id: // value for 'id'
 *      starred: // value for 'starred'
 *   },
 * });
 */
export function useCollectionChooserUpdateCollectionStarredMutation(baseOptions?: Apollo.MutationHookOptions<ICollectionChooserUpdateCollectionStarredMutation, ICollectionChooserUpdateCollectionStarredMutationVariables>) {
        return Apollo.useMutation<ICollectionChooserUpdateCollectionStarredMutation, ICollectionChooserUpdateCollectionStarredMutationVariables>(CollectionChooserUpdateCollectionStarredDocument, baseOptions);
      }
export type CollectionChooserUpdateCollectionStarredMutationHookResult = ReturnType<typeof useCollectionChooserUpdateCollectionStarredMutation>;
export type CollectionChooserUpdateCollectionStarredMutationResult = Apollo.MutationResult<ICollectionChooserUpdateCollectionStarredMutation>;
export type CollectionChooserUpdateCollectionStarredMutationOptions = Apollo.BaseMutationOptions<ICollectionChooserUpdateCollectionStarredMutation, ICollectionChooserUpdateCollectionStarredMutationVariables>;
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
        return Apollo.useQuery<IArtistsFetchArtistQuery, IArtistsFetchArtistQueryVariables>(ArtistsFetchArtistDocument, baseOptions);
      }
export function useArtistsFetchArtistLazyQuery(baseOptions?: Apollo.LazyQueryHookOptions<IArtistsFetchArtistQuery, IArtistsFetchArtistQueryVariables>) {
          return Apollo.useLazyQuery<IArtistsFetchArtistQuery, IArtistsFetchArtistQueryVariables>(ArtistsFetchArtistDocument, baseOptions);
        }
export type ArtistsFetchArtistQueryHookResult = ReturnType<typeof useArtistsFetchArtistQuery>;
export type ArtistsFetchArtistLazyQueryHookResult = ReturnType<typeof useArtistsFetchArtistLazyQuery>;
export type ArtistsFetchArtistQueryResult = Apollo.QueryResult<IArtistsFetchArtistQuery, IArtistsFetchArtistQueryVariables>;
export const ArtistChooserFetchArtistsDocument = gql`
    query ArtistChooserFetchArtists {
  artists {
    results {
      ...ArtistFields
    }
  }
}
    ${ArtistFieldsFragmentDoc}`;

/**
 * __useArtistChooserFetchArtistsQuery__
 *
 * To run a query within a React component, call `useArtistChooserFetchArtistsQuery` and pass it any options that fit your needs.
 * When your component renders, `useArtistChooserFetchArtistsQuery` returns an object from Apollo Client that contains loading, error, and data properties
 * you can use to render your UI.
 *
 * @param baseOptions options that will be passed into the query, supported options are listed on: https://www.apollographql.com/docs/react/api/react-hooks/#options;
 *
 * @example
 * const { data, loading, error } = useArtistChooserFetchArtistsQuery({
 *   variables: {
 *   },
 * });
 */
export function useArtistChooserFetchArtistsQuery(baseOptions?: Apollo.QueryHookOptions<IArtistChooserFetchArtistsQuery, IArtistChooserFetchArtistsQueryVariables>) {
        return Apollo.useQuery<IArtistChooserFetchArtistsQuery, IArtistChooserFetchArtistsQueryVariables>(ArtistChooserFetchArtistsDocument, baseOptions);
      }
export function useArtistChooserFetchArtistsLazyQuery(baseOptions?: Apollo.LazyQueryHookOptions<IArtistChooserFetchArtistsQuery, IArtistChooserFetchArtistsQueryVariables>) {
          return Apollo.useLazyQuery<IArtistChooserFetchArtistsQuery, IArtistChooserFetchArtistsQueryVariables>(ArtistChooserFetchArtistsDocument, baseOptions);
        }
export type ArtistChooserFetchArtistsQueryHookResult = ReturnType<typeof useArtistChooserFetchArtistsQuery>;
export type ArtistChooserFetchArtistsLazyQueryHookResult = ReturnType<typeof useArtistChooserFetchArtistsLazyQuery>;
export type ArtistChooserFetchArtistsQueryResult = Apollo.QueryResult<IArtistChooserFetchArtistsQuery, IArtistChooserFetchArtistsQueryVariables>;
export const ArtistChooserUpdateArtistStarredDocument = gql`
    mutation ArtistChooserUpdateArtistStarred($id: Int!, $starred: Boolean) {
  updateArtist(id: $id, starred: $starred) {
    id
    starred
  }
}
    `;
export type IArtistChooserUpdateArtistStarredMutationFn = Apollo.MutationFunction<IArtistChooserUpdateArtistStarredMutation, IArtistChooserUpdateArtistStarredMutationVariables>;

/**
 * __useArtistChooserUpdateArtistStarredMutation__
 *
 * To run a mutation, you first call `useArtistChooserUpdateArtistStarredMutation` within a React component and pass it any options that fit your needs.
 * When your component renders, `useArtistChooserUpdateArtistStarredMutation` returns a tuple that includes:
 * - A mutate function that you can call at any time to execute the mutation
 * - An object with fields that represent the current status of the mutation's execution
 *
 * @param baseOptions options that will be passed into the mutation, supported options are listed on: https://www.apollographql.com/docs/react/api/react-hooks/#options-2;
 *
 * @example
 * const [artistChooserUpdateArtistStarredMutation, { data, loading, error }] = useArtistChooserUpdateArtistStarredMutation({
 *   variables: {
 *      id: // value for 'id'
 *      starred: // value for 'starred'
 *   },
 * });
 */
export function useArtistChooserUpdateArtistStarredMutation(baseOptions?: Apollo.MutationHookOptions<IArtistChooserUpdateArtistStarredMutation, IArtistChooserUpdateArtistStarredMutationVariables>) {
        return Apollo.useMutation<IArtistChooserUpdateArtistStarredMutation, IArtistChooserUpdateArtistStarredMutationVariables>(ArtistChooserUpdateArtistStarredDocument, baseOptions);
      }
export type ArtistChooserUpdateArtistStarredMutationHookResult = ReturnType<typeof useArtistChooserUpdateArtistStarredMutation>;
export type ArtistChooserUpdateArtistStarredMutationResult = Apollo.MutationResult<IArtistChooserUpdateArtistStarredMutation>;
export type ArtistChooserUpdateArtistStarredMutationOptions = Apollo.BaseMutationOptions<IArtistChooserUpdateArtistStarredMutation, IArtistChooserUpdateArtistStarredMutationVariables>;
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
        return Apollo.useQuery<ICollageFetchCollageQuery, ICollageFetchCollageQueryVariables>(CollageFetchCollageDocument, baseOptions);
      }
export function useCollageFetchCollageLazyQuery(baseOptions?: Apollo.LazyQueryHookOptions<ICollageFetchCollageQuery, ICollageFetchCollageQueryVariables>) {
          return Apollo.useLazyQuery<ICollageFetchCollageQuery, ICollageFetchCollageQueryVariables>(CollageFetchCollageDocument, baseOptions);
        }
export type CollageFetchCollageQueryHookResult = ReturnType<typeof useCollageFetchCollageQuery>;
export type CollageFetchCollageLazyQueryHookResult = ReturnType<typeof useCollageFetchCollageLazyQuery>;
export type CollageFetchCollageQueryResult = Apollo.QueryResult<ICollageFetchCollageQuery, ICollageFetchCollageQueryVariables>;
export const RecentlyAddedFetchReleasesDocument = gql`
    query RecentlyAddedFetchReleases {
  releases(sort: RECENTLY_ADDED, asc: false, page: 1, perPage: 10) {
    results {
      ...ReleaseFields
      artists {
        id
        name
      }
      genres {
        id
        name
      }
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
        return Apollo.useQuery<IRecentlyAddedFetchReleasesQuery, IRecentlyAddedFetchReleasesQueryVariables>(RecentlyAddedFetchReleasesDocument, baseOptions);
      }
export function useRecentlyAddedFetchReleasesLazyQuery(baseOptions?: Apollo.LazyQueryHookOptions<IRecentlyAddedFetchReleasesQuery, IRecentlyAddedFetchReleasesQueryVariables>) {
          return Apollo.useLazyQuery<IRecentlyAddedFetchReleasesQuery, IRecentlyAddedFetchReleasesQueryVariables>(RecentlyAddedFetchReleasesDocument, baseOptions);
        }
export type RecentlyAddedFetchReleasesQueryHookResult = ReturnType<typeof useRecentlyAddedFetchReleasesQuery>;
export type RecentlyAddedFetchReleasesLazyQueryHookResult = ReturnType<typeof useRecentlyAddedFetchReleasesLazyQuery>;
export type RecentlyAddedFetchReleasesQueryResult = Apollo.QueryResult<IRecentlyAddedFetchReleasesQuery, IRecentlyAddedFetchReleasesQueryVariables>;
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
        return Apollo.useQuery<IGenresFetchGenreQuery, IGenresFetchGenreQueryVariables>(GenresFetchGenreDocument, baseOptions);
      }
export function useGenresFetchGenreLazyQuery(baseOptions?: Apollo.LazyQueryHookOptions<IGenresFetchGenreQuery, IGenresFetchGenreQueryVariables>) {
          return Apollo.useLazyQuery<IGenresFetchGenreQuery, IGenresFetchGenreQueryVariables>(GenresFetchGenreDocument, baseOptions);
        }
export type GenresFetchGenreQueryHookResult = ReturnType<typeof useGenresFetchGenreQuery>;
export type GenresFetchGenreLazyQueryHookResult = ReturnType<typeof useGenresFetchGenreLazyQuery>;
export type GenresFetchGenreQueryResult = Apollo.QueryResult<IGenresFetchGenreQuery, IGenresFetchGenreQueryVariables>;
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
        return Apollo.useQuery<ILabelFetchLabelQuery, ILabelFetchLabelQueryVariables>(LabelFetchLabelDocument, baseOptions);
      }
export function useLabelFetchLabelLazyQuery(baseOptions?: Apollo.LazyQueryHookOptions<ILabelFetchLabelQuery, ILabelFetchLabelQueryVariables>) {
          return Apollo.useLazyQuery<ILabelFetchLabelQuery, ILabelFetchLabelQueryVariables>(LabelFetchLabelDocument, baseOptions);
        }
export type LabelFetchLabelQueryHookResult = ReturnType<typeof useLabelFetchLabelQuery>;
export type LabelFetchLabelLazyQueryHookResult = ReturnType<typeof useLabelFetchLabelLazyQuery>;
export type LabelFetchLabelQueryResult = Apollo.QueryResult<ILabelFetchLabelQuery, ILabelFetchLabelQueryVariables>;
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
        return Apollo.useQuery<INowPlayingInfoFetchReleaseQuery, INowPlayingInfoFetchReleaseQueryVariables>(NowPlayingInfoFetchReleaseDocument, baseOptions);
      }
export function useNowPlayingInfoFetchReleaseLazyQuery(baseOptions?: Apollo.LazyQueryHookOptions<INowPlayingInfoFetchReleaseQuery, INowPlayingInfoFetchReleaseQueryVariables>) {
          return Apollo.useLazyQuery<INowPlayingInfoFetchReleaseQuery, INowPlayingInfoFetchReleaseQueryVariables>(NowPlayingInfoFetchReleaseDocument, baseOptions);
        }
export type NowPlayingInfoFetchReleaseQueryHookResult = ReturnType<typeof useNowPlayingInfoFetchReleaseQuery>;
export type NowPlayingInfoFetchReleaseLazyQueryHookResult = ReturnType<typeof useNowPlayingInfoFetchReleaseLazyQuery>;
export type NowPlayingInfoFetchReleaseQueryResult = Apollo.QueryResult<INowPlayingInfoFetchReleaseQuery, INowPlayingInfoFetchReleaseQueryVariables>;
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
        return Apollo.useMutation<IInFavoritesAddReleaseToCollectionMutation, IInFavoritesAddReleaseToCollectionMutationVariables>(InFavoritesAddReleaseToCollectionDocument, baseOptions);
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
        return Apollo.useMutation<IInFavoritesDelReleaseFromCollectionMutation, IInFavoritesDelReleaseFromCollectionMutationVariables>(InFavoritesDelReleaseFromCollectionDocument, baseOptions);
      }
export type InFavoritesDelReleaseFromCollectionMutationHookResult = ReturnType<typeof useInFavoritesDelReleaseFromCollectionMutation>;
export type InFavoritesDelReleaseFromCollectionMutationResult = Apollo.MutationResult<IInFavoritesDelReleaseFromCollectionMutation>;
export type InFavoritesDelReleaseFromCollectionMutationOptions = Apollo.BaseMutationOptions<IInFavoritesDelReleaseFromCollectionMutation, IInFavoritesDelReleaseFromCollectionMutationVariables>;
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
        return Apollo.useMutation<IInInboxAddReleaseToCollectionMutation, IInInboxAddReleaseToCollectionMutationVariables>(InInboxAddReleaseToCollectionDocument, baseOptions);
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
        return Apollo.useMutation<IInInboxDelReleaseFromCollectionMutation, IInInboxDelReleaseFromCollectionMutationVariables>(InInboxDelReleaseFromCollectionDocument, baseOptions);
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
        return Apollo.useMutation<IReleaseUpdateReleaseRatingMutation, IReleaseUpdateReleaseRatingMutationVariables>(ReleaseUpdateReleaseRatingDocument, baseOptions);
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
        return Apollo.useQuery<IReleaseFetchReleaseQuery, IReleaseFetchReleaseQueryVariables>(ReleaseFetchReleaseDocument, baseOptions);
      }
export function useReleaseFetchReleaseLazyQuery(baseOptions?: Apollo.LazyQueryHookOptions<IReleaseFetchReleaseQuery, IReleaseFetchReleaseQueryVariables>) {
          return Apollo.useLazyQuery<IReleaseFetchReleaseQuery, IReleaseFetchReleaseQueryVariables>(ReleaseFetchReleaseDocument, baseOptions);
        }
export type ReleaseFetchReleaseQueryHookResult = ReturnType<typeof useReleaseFetchReleaseQuery>;
export type ReleaseFetchReleaseLazyQueryHookResult = ReturnType<typeof useReleaseFetchReleaseLazyQuery>;
export type ReleaseFetchReleaseQueryResult = Apollo.QueryResult<IReleaseFetchReleaseQuery, IReleaseFetchReleaseQueryVariables>;
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
        return Apollo.useQuery<ISettingsFetchUserQuery, ISettingsFetchUserQueryVariables>(SettingsFetchUserDocument, baseOptions);
      }
export function useSettingsFetchUserLazyQuery(baseOptions?: Apollo.LazyQueryHookOptions<ISettingsFetchUserQuery, ISettingsFetchUserQueryVariables>) {
          return Apollo.useLazyQuery<ISettingsFetchUserQuery, ISettingsFetchUserQueryVariables>(SettingsFetchUserDocument, baseOptions);
        }
export type SettingsFetchUserQueryHookResult = ReturnType<typeof useSettingsFetchUserQuery>;
export type SettingsFetchUserLazyQueryHookResult = ReturnType<typeof useSettingsFetchUserLazyQuery>;
export type SettingsFetchUserQueryResult = Apollo.QueryResult<ISettingsFetchUserQuery, ISettingsFetchUserQueryVariables>;
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
        return Apollo.useMutation<ISettingsUpdateUserMutation, ISettingsUpdateUserMutationVariables>(SettingsUpdateUserDocument, baseOptions);
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
        return Apollo.useQuery<IYearsFetchReleaseYearsQuery, IYearsFetchReleaseYearsQueryVariables>(YearsFetchReleaseYearsDocument, baseOptions);
      }
export function useYearsFetchReleaseYearsLazyQuery(baseOptions?: Apollo.LazyQueryHookOptions<IYearsFetchReleaseYearsQuery, IYearsFetchReleaseYearsQueryVariables>) {
          return Apollo.useLazyQuery<IYearsFetchReleaseYearsQuery, IYearsFetchReleaseYearsQueryVariables>(YearsFetchReleaseYearsDocument, baseOptions);
        }
export type YearsFetchReleaseYearsQueryHookResult = ReturnType<typeof useYearsFetchReleaseYearsQuery>;
export type YearsFetchReleaseYearsLazyQueryHookResult = ReturnType<typeof useYearsFetchReleaseYearsLazyQuery>;
export type YearsFetchReleaseYearsQueryResult = Apollo.QueryResult<IYearsFetchReleaseYearsQuery, IYearsFetchReleaseYearsQueryVariables>;
export type QueryKeySpecifier = ('artist' | 'artistFromName' | 'collection' | 'collectionFromNameAndType' | 'playlist' | 'playlistFromNameAndType' | 'release' | 'track' | 'user' | 'artists' | 'collections' | 'playlists' | 'releases' | 'releaseYears' | QueryKeySpecifier)[];
export type QueryFieldPolicy = {
	artist?: FieldPolicy<any> | FieldReadFunction<any>,
	artistFromName?: FieldPolicy<any> | FieldReadFunction<any>,
	collection?: FieldPolicy<any> | FieldReadFunction<any>,
	collectionFromNameAndType?: FieldPolicy<any> | FieldReadFunction<any>,
	playlist?: FieldPolicy<any> | FieldReadFunction<any>,
	playlistFromNameAndType?: FieldPolicy<any> | FieldReadFunction<any>,
	release?: FieldPolicy<any> | FieldReadFunction<any>,
	track?: FieldPolicy<any> | FieldReadFunction<any>,
	user?: FieldPolicy<any> | FieldReadFunction<any>,
	artists?: FieldPolicy<any> | FieldReadFunction<any>,
	collections?: FieldPolicy<any> | FieldReadFunction<any>,
	playlists?: FieldPolicy<any> | FieldReadFunction<any>,
	releases?: FieldPolicy<any> | FieldReadFunction<any>,
	releaseYears?: FieldPolicy<any> | FieldReadFunction<any>
};
export type MutationKeySpecifier = ('createArtist' | 'updateArtist' | 'createCollection' | 'updateCollection' | 'addReleaseToCollection' | 'delReleaseFromCollection' | 'createPlaylist' | 'updatePlaylist' | 'createPlaylistEntry' | 'delPlaylistEntry' | 'updatePlaylistEntry' | 'createRelease' | 'updateRelease' | 'addArtistToRelease' | 'delArtistFromRelease' | 'updateTrack' | 'addArtistToTrack' | 'delArtistFromTrack' | 'updateUser' | 'newToken' | MutationKeySpecifier)[];
export type MutationFieldPolicy = {
	createArtist?: FieldPolicy<any> | FieldReadFunction<any>,
	updateArtist?: FieldPolicy<any> | FieldReadFunction<any>,
	createCollection?: FieldPolicy<any> | FieldReadFunction<any>,
	updateCollection?: FieldPolicy<any> | FieldReadFunction<any>,
	addReleaseToCollection?: FieldPolicy<any> | FieldReadFunction<any>,
	delReleaseFromCollection?: FieldPolicy<any> | FieldReadFunction<any>,
	createPlaylist?: FieldPolicy<any> | FieldReadFunction<any>,
	updatePlaylist?: FieldPolicy<any> | FieldReadFunction<any>,
	createPlaylistEntry?: FieldPolicy<any> | FieldReadFunction<any>,
	delPlaylistEntry?: FieldPolicy<any> | FieldReadFunction<any>,
	updatePlaylistEntry?: FieldPolicy<any> | FieldReadFunction<any>,
	createRelease?: FieldPolicy<any> | FieldReadFunction<any>,
	updateRelease?: FieldPolicy<any> | FieldReadFunction<any>,
	addArtistToRelease?: FieldPolicy<any> | FieldReadFunction<any>,
	delArtistFromRelease?: FieldPolicy<any> | FieldReadFunction<any>,
	updateTrack?: FieldPolicy<any> | FieldReadFunction<any>,
	addArtistToTrack?: FieldPolicy<any> | FieldReadFunction<any>,
	delArtistFromTrack?: FieldPolicy<any> | FieldReadFunction<any>,
	updateUser?: FieldPolicy<any> | FieldReadFunction<any>,
	newToken?: FieldPolicy<any> | FieldReadFunction<any>
};
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
export type ArtistsKeySpecifier = ('results' | ArtistsKeySpecifier)[];
export type ArtistsFieldPolicy = {
	results?: FieldPolicy<any> | FieldReadFunction<any>
};
export type CollectionKeySpecifier = ('id' | 'name' | 'starred' | 'type' | 'numReleases' | 'lastUpdatedOn' | 'imageId' | 'releases' | 'topGenres' | CollectionKeySpecifier)[];
export type CollectionFieldPolicy = {
	id?: FieldPolicy<any> | FieldReadFunction<any>,
	name?: FieldPolicy<any> | FieldReadFunction<any>,
	starred?: FieldPolicy<any> | FieldReadFunction<any>,
	type?: FieldPolicy<any> | FieldReadFunction<any>,
	numReleases?: FieldPolicy<any> | FieldReadFunction<any>,
	lastUpdatedOn?: FieldPolicy<any> | FieldReadFunction<any>,
	imageId?: FieldPolicy<any> | FieldReadFunction<any>,
	releases?: FieldPolicy<any> | FieldReadFunction<any>,
	topGenres?: FieldPolicy<any> | FieldReadFunction<any>
};
export type CollectionsKeySpecifier = ('results' | CollectionsKeySpecifier)[];
export type CollectionsFieldPolicy = {
	results?: FieldPolicy<any> | FieldReadFunction<any>
};
export type PlaylistKeySpecifier = ('id' | 'name' | 'starred' | 'type' | 'numTracks' | 'lastUpdatedOn' | 'imageId' | 'entries' | 'topGenres' | PlaylistKeySpecifier)[];
export type PlaylistFieldPolicy = {
	id?: FieldPolicy<any> | FieldReadFunction<any>,
	name?: FieldPolicy<any> | FieldReadFunction<any>,
	starred?: FieldPolicy<any> | FieldReadFunction<any>,
	type?: FieldPolicy<any> | FieldReadFunction<any>,
	numTracks?: FieldPolicy<any> | FieldReadFunction<any>,
	lastUpdatedOn?: FieldPolicy<any> | FieldReadFunction<any>,
	imageId?: FieldPolicy<any> | FieldReadFunction<any>,
	entries?: FieldPolicy<any> | FieldReadFunction<any>,
	topGenres?: FieldPolicy<any> | FieldReadFunction<any>
};
export type PlaylistsKeySpecifier = ('results' | PlaylistsKeySpecifier)[];
export type PlaylistsFieldPolicy = {
	results?: FieldPolicy<any> | FieldReadFunction<any>
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
export type ReleasesKeySpecifier = ('total' | 'results' | ReleasesKeySpecifier)[];
export type ReleasesFieldPolicy = {
	total?: FieldPolicy<any> | FieldReadFunction<any>,
	results?: FieldPolicy<any> | FieldReadFunction<any>
};
export type TrackKeySpecifier = ('id' | 'title' | 'duration' | 'trackNumber' | 'discNumber' | 'release' | 'artists' | TrackKeySpecifier)[];
export type TrackFieldPolicy = {
	id?: FieldPolicy<any> | FieldReadFunction<any>,
	title?: FieldPolicy<any> | FieldReadFunction<any>,
	duration?: FieldPolicy<any> | FieldReadFunction<any>,
	trackNumber?: FieldPolicy<any> | FieldReadFunction<any>,
	discNumber?: FieldPolicy<any> | FieldReadFunction<any>,
	release?: FieldPolicy<any> | FieldReadFunction<any>,
	artists?: FieldPolicy<any> | FieldReadFunction<any>
};
export type TrackArtistKeySpecifier = ('artist' | 'role' | TrackArtistKeySpecifier)[];
export type TrackArtistFieldPolicy = {
	artist?: FieldPolicy<any> | FieldReadFunction<any>,
	role?: FieldPolicy<any> | FieldReadFunction<any>
};
export type TopGenreKeySpecifier = ('genre' | 'numMatches' | TopGenreKeySpecifier)[];
export type TopGenreFieldPolicy = {
	genre?: FieldPolicy<any> | FieldReadFunction<any>,
	numMatches?: FieldPolicy<any> | FieldReadFunction<any>
};
export type UserKeySpecifier = ('id' | 'nickname' | UserKeySpecifier)[];
export type UserFieldPolicy = {
	id?: FieldPolicy<any> | FieldReadFunction<any>,
	nickname?: FieldPolicy<any> | FieldReadFunction<any>
};
export type TokenKeySpecifier = ('hex' | TokenKeySpecifier)[];
export type TokenFieldPolicy = {
	hex?: FieldPolicy<any> | FieldReadFunction<any>
};
export type CollectionAndReleaseKeySpecifier = ('collection' | 'release' | CollectionAndReleaseKeySpecifier)[];
export type CollectionAndReleaseFieldPolicy = {
	collection?: FieldPolicy<any> | FieldReadFunction<any>,
	release?: FieldPolicy<any> | FieldReadFunction<any>
};
export type ReleaseAndArtistKeySpecifier = ('release' | 'artist' | ReleaseAndArtistKeySpecifier)[];
export type ReleaseAndArtistFieldPolicy = {
	release?: FieldPolicy<any> | FieldReadFunction<any>,
	artist?: FieldPolicy<any> | FieldReadFunction<any>
};
export type TrackAndArtistKeySpecifier = ('track' | 'trackArtist' | TrackAndArtistKeySpecifier)[];
export type TrackAndArtistFieldPolicy = {
	track?: FieldPolicy<any> | FieldReadFunction<any>,
	trackArtist?: FieldPolicy<any> | FieldReadFunction<any>
};
export type TypedTypePolicies = TypePolicies & {
	Query?: Omit<TypePolicy, "fields" | "keyFields"> & {
		keyFields?: false | QueryKeySpecifier | (() => undefined | QueryKeySpecifier),
		fields?: QueryFieldPolicy,
	},
	Mutation?: Omit<TypePolicy, "fields" | "keyFields"> & {
		keyFields?: false | MutationKeySpecifier | (() => undefined | MutationKeySpecifier),
		fields?: MutationFieldPolicy,
	},
	Artist?: Omit<TypePolicy, "fields" | "keyFields"> & {
		keyFields?: false | ArtistKeySpecifier | (() => undefined | ArtistKeySpecifier),
		fields?: ArtistFieldPolicy,
	},
	Artists?: Omit<TypePolicy, "fields" | "keyFields"> & {
		keyFields?: false | ArtistsKeySpecifier | (() => undefined | ArtistsKeySpecifier),
		fields?: ArtistsFieldPolicy,
	},
	Collection?: Omit<TypePolicy, "fields" | "keyFields"> & {
		keyFields?: false | CollectionKeySpecifier | (() => undefined | CollectionKeySpecifier),
		fields?: CollectionFieldPolicy,
	},
	Collections?: Omit<TypePolicy, "fields" | "keyFields"> & {
		keyFields?: false | CollectionsKeySpecifier | (() => undefined | CollectionsKeySpecifier),
		fields?: CollectionsFieldPolicy,
	},
	Playlist?: Omit<TypePolicy, "fields" | "keyFields"> & {
		keyFields?: false | PlaylistKeySpecifier | (() => undefined | PlaylistKeySpecifier),
		fields?: PlaylistFieldPolicy,
	},
	Playlists?: Omit<TypePolicy, "fields" | "keyFields"> & {
		keyFields?: false | PlaylistsKeySpecifier | (() => undefined | PlaylistsKeySpecifier),
		fields?: PlaylistsFieldPolicy,
	},
	PlaylistEntry?: Omit<TypePolicy, "fields" | "keyFields"> & {
		keyFields?: false | PlaylistEntryKeySpecifier | (() => undefined | PlaylistEntryKeySpecifier),
		fields?: PlaylistEntryFieldPolicy,
	},
	Release?: Omit<TypePolicy, "fields" | "keyFields"> & {
		keyFields?: false | ReleaseKeySpecifier | (() => undefined | ReleaseKeySpecifier),
		fields?: ReleaseFieldPolicy,
	},
	Releases?: Omit<TypePolicy, "fields" | "keyFields"> & {
		keyFields?: false | ReleasesKeySpecifier | (() => undefined | ReleasesKeySpecifier),
		fields?: ReleasesFieldPolicy,
	},
	Track?: Omit<TypePolicy, "fields" | "keyFields"> & {
		keyFields?: false | TrackKeySpecifier | (() => undefined | TrackKeySpecifier),
		fields?: TrackFieldPolicy,
	},
	TrackArtist?: Omit<TypePolicy, "fields" | "keyFields"> & {
		keyFields?: false | TrackArtistKeySpecifier | (() => undefined | TrackArtistKeySpecifier),
		fields?: TrackArtistFieldPolicy,
	},
	TopGenre?: Omit<TypePolicy, "fields" | "keyFields"> & {
		keyFields?: false | TopGenreKeySpecifier | (() => undefined | TopGenreKeySpecifier),
		fields?: TopGenreFieldPolicy,
	},
	User?: Omit<TypePolicy, "fields" | "keyFields"> & {
		keyFields?: false | UserKeySpecifier | (() => undefined | UserKeySpecifier),
		fields?: UserFieldPolicy,
	},
	Token?: Omit<TypePolicy, "fields" | "keyFields"> & {
		keyFields?: false | TokenKeySpecifier | (() => undefined | TokenKeySpecifier),
		fields?: TokenFieldPolicy,
	},
	CollectionAndRelease?: Omit<TypePolicy, "fields" | "keyFields"> & {
		keyFields?: false | CollectionAndReleaseKeySpecifier | (() => undefined | CollectionAndReleaseKeySpecifier),
		fields?: CollectionAndReleaseFieldPolicy,
	},
	ReleaseAndArtist?: Omit<TypePolicy, "fields" | "keyFields"> & {
		keyFields?: false | ReleaseAndArtistKeySpecifier | (() => undefined | ReleaseAndArtistKeySpecifier),
		fields?: ReleaseAndArtistFieldPolicy,
	},
	TrackAndArtist?: Omit<TypePolicy, "fields" | "keyFields"> & {
		keyFields?: false | TrackAndArtistKeySpecifier | (() => undefined | TrackAndArtistKeySpecifier),
		fields?: TrackAndArtistFieldPolicy,
	}
};