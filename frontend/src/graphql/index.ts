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
  addTrackToPlaylist: Maybe<IPlaylistAndTrack>;
  delTrackFromPlaylist: Maybe<IPlaylistAndTrack>;
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


export type IMutationAddTrackToPlaylistArgs = {
  playlistId: Scalars['Int'];
  trackId: Scalars['Int'];
};


export type IMutationDelTrackFromPlaylistArgs = {
  playlistId: Scalars['Int'];
  trackId: Scalars['Int'];
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
  tracks: Array<Maybe<ITrack>>;
  /** The top genres of the playlist, compiled from its tracks. */
  topGenres: Array<Maybe<ITopGenre>>;
};

export type IPlaylists = {
  __typename?: 'Playlists';
  results: Array<Maybe<IPlaylist>>;
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

export type IPlaylistAndTrack = {
  __typename?: 'PlaylistAndTrack';
  playlist: IPlaylist;
  track: ITrack;
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

export type IFetchArtistsQueryVariables = Exact<{ [key: string]: never; }>;


export type IFetchArtistsQuery = (
  { __typename?: 'Query' }
  & { artists: Maybe<(
    { __typename?: 'Artists' }
    & { results: Array<Maybe<(
      { __typename?: 'Artist' }
      & IArtistFieldsFragment
    )>> }
  )> }
);

export type IFetchArtistQueryVariables = Exact<{
  id: Scalars['Int'];
}>;


export type IFetchArtistQuery = (
  { __typename?: 'Query' }
  & { artist: Maybe<(
    { __typename?: 'Artist' }
    & IArtistFieldsFragment
  )> }
);

export type IUpdateArtistMutationVariables = Exact<{
  id: Scalars['Int'];
  name: Maybe<Scalars['String']>;
  starred: Maybe<Scalars['Boolean']>;
}>;


export type IUpdateArtistMutation = (
  { __typename?: 'Mutation' }
  & { updateArtist: Maybe<(
    { __typename?: 'Artist' }
    & Pick<IArtist, 'id' | 'name' | 'starred'>
  )> }
);

export type IUpdateArtistStarredMutationVariables = Exact<{
  id: Scalars['Int'];
  starred: Maybe<Scalars['Boolean']>;
}>;


export type IUpdateArtistStarredMutation = (
  { __typename?: 'Mutation' }
  & { updateArtist: Maybe<(
    { __typename?: 'Artist' }
    & Pick<IArtist, 'id' | 'starred'>
  )> }
);

export type IFetchCollectionsQueryVariables = Exact<{
  types: Maybe<Array<Maybe<ICollectionType>> | Maybe<ICollectionType>>;
}>;


export type IFetchCollectionsQuery = (
  { __typename?: 'Query' }
  & { collections: Maybe<(
    { __typename?: 'Collections' }
    & { results: Array<Maybe<(
      { __typename?: 'Collection' }
      & ICollectionFieldsFragment
    )>> }
  )> }
);

export type IFetchCollectionQueryVariables = Exact<{
  id: Scalars['Int'];
}>;


export type IFetchCollectionQuery = (
  { __typename?: 'Query' }
  & { collection: Maybe<(
    { __typename?: 'Collection' }
    & ICollectionFieldsFragment
  )> }
);

export type IUpdateCollectionMutationVariables = Exact<{
  id: Scalars['Int'];
  name: Maybe<Scalars['String']>;
  starred: Maybe<Scalars['Boolean']>;
}>;


export type IUpdateCollectionMutation = (
  { __typename?: 'Mutation' }
  & { updateCollection: Maybe<(
    { __typename?: 'Collection' }
    & Pick<ICollection, 'id' | 'name' | 'starred'>
  )> }
);

export type IUpdateCollectionStarredMutationVariables = Exact<{
  id: Scalars['Int'];
  starred: Maybe<Scalars['Boolean']>;
}>;


export type IUpdateCollectionStarredMutation = (
  { __typename?: 'Mutation' }
  & { updateCollection: Maybe<(
    { __typename?: 'Collection' }
    & Pick<ICollection, 'id' | 'starred'>
  )> }
);

export type IAddReleaseToCollectionMutationVariables = Exact<{
  collectionId: Scalars['Int'];
  releaseId: Scalars['Int'];
}>;


export type IAddReleaseToCollectionMutation = (
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

export type IDelReleaseFromCollectionMutationVariables = Exact<{
  collectionId: Scalars['Int'];
  releaseId: Scalars['Int'];
}>;


export type IDelReleaseFromCollectionMutation = (
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

export type IFetchReleasesQueryVariables = Exact<{
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


export type IFetchReleasesQuery = (
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

export type IFetchReleasesRecentlyAddedQueryVariables = Exact<{ [key: string]: never; }>;


export type IFetchReleasesRecentlyAddedQuery = (
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

export type IFetchReleaseQueryVariables = Exact<{
  id: Scalars['Int'];
}>;


export type IFetchReleaseQuery = (
  { __typename?: 'Query' }
  & { release: Maybe<(
    { __typename?: 'Release' }
    & IFullReleaseFieldsFragment
  )> }
);

export type IFetchReleaseYearsQueryVariables = Exact<{ [key: string]: never; }>;


export type IFetchReleaseYearsQuery = (
  { __typename?: 'Query' }
  & Pick<IQuery, 'releaseYears'>
);

export type IUpdateReleaseMutationVariables = Exact<{
  id: Scalars['Int'];
  title: Maybe<Scalars['String']>;
  releaseType: Maybe<IReleaseType>;
  releaseYear: Maybe<Scalars['Int']>;
  releaseDate: Maybe<Scalars['String']>;
  rating: Maybe<Scalars['Int']>;
}>;


export type IUpdateReleaseMutation = (
  { __typename?: 'Mutation' }
  & { updateRelease: Maybe<(
    { __typename?: 'Release' }
    & Pick<IRelease, 'id' | 'title' | 'releaseType' | 'releaseYear' | 'releaseDate' | 'rating'>
  )> }
);

export type IUpdateReleaseRatingMutationVariables = Exact<{
  id: Scalars['Int'];
  rating: Maybe<Scalars['Int']>;
}>;


export type IUpdateReleaseRatingMutation = (
  { __typename?: 'Mutation' }
  & { updateRelease: Maybe<(
    { __typename?: 'Release' }
    & Pick<IRelease, 'id' | 'rating'>
  )> }
);

export type IFetchUserQueryVariables = Exact<{ [key: string]: never; }>;


export type IFetchUserQuery = (
  { __typename?: 'Query' }
  & { user: Maybe<(
    { __typename?: 'User' }
    & IUserFieldsFragment
  )> }
);

export type IUpdateUserMutationVariables = Exact<{
  nickname: Maybe<Scalars['String']>;
}>;


export type IUpdateUserMutation = (
  { __typename?: 'Mutation' }
  & { updateUser: Maybe<(
    { __typename?: 'User' }
    & Pick<IUser, 'id' | 'nickname'>
  )> }
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
export const FetchArtistsDocument = gql`
    query FetchArtists {
  artists {
    results {
      ...ArtistFields
    }
  }
}
    ${ArtistFieldsFragmentDoc}`;

/**
 * __useFetchArtistsQuery__
 *
 * To run a query within a React component, call `useFetchArtistsQuery` and pass it any options that fit your needs.
 * When your component renders, `useFetchArtistsQuery` returns an object from Apollo Client that contains loading, error, and data properties
 * you can use to render your UI.
 *
 * @param baseOptions options that will be passed into the query, supported options are listed on: https://www.apollographql.com/docs/react/api/react-hooks/#options;
 *
 * @example
 * const { data, loading, error } = useFetchArtistsQuery({
 *   variables: {
 *   },
 * });
 */
export function useFetchArtistsQuery(baseOptions?: Apollo.QueryHookOptions<IFetchArtistsQuery, IFetchArtistsQueryVariables>) {
        return Apollo.useQuery<IFetchArtistsQuery, IFetchArtistsQueryVariables>(FetchArtistsDocument, baseOptions);
      }
export function useFetchArtistsLazyQuery(baseOptions?: Apollo.LazyQueryHookOptions<IFetchArtistsQuery, IFetchArtistsQueryVariables>) {
          return Apollo.useLazyQuery<IFetchArtistsQuery, IFetchArtistsQueryVariables>(FetchArtistsDocument, baseOptions);
        }
export type FetchArtistsQueryHookResult = ReturnType<typeof useFetchArtistsQuery>;
export type FetchArtistsLazyQueryHookResult = ReturnType<typeof useFetchArtistsLazyQuery>;
export type FetchArtistsQueryResult = Apollo.QueryResult<IFetchArtistsQuery, IFetchArtistsQueryVariables>;
export const FetchArtistDocument = gql`
    query FetchArtist($id: Int!) {
  artist(id: $id) {
    ...ArtistFields
  }
}
    ${ArtistFieldsFragmentDoc}`;

/**
 * __useFetchArtistQuery__
 *
 * To run a query within a React component, call `useFetchArtistQuery` and pass it any options that fit your needs.
 * When your component renders, `useFetchArtistQuery` returns an object from Apollo Client that contains loading, error, and data properties
 * you can use to render your UI.
 *
 * @param baseOptions options that will be passed into the query, supported options are listed on: https://www.apollographql.com/docs/react/api/react-hooks/#options;
 *
 * @example
 * const { data, loading, error } = useFetchArtistQuery({
 *   variables: {
 *      id: // value for 'id'
 *   },
 * });
 */
export function useFetchArtistQuery(baseOptions: Apollo.QueryHookOptions<IFetchArtistQuery, IFetchArtistQueryVariables>) {
        return Apollo.useQuery<IFetchArtistQuery, IFetchArtistQueryVariables>(FetchArtistDocument, baseOptions);
      }
export function useFetchArtistLazyQuery(baseOptions?: Apollo.LazyQueryHookOptions<IFetchArtistQuery, IFetchArtistQueryVariables>) {
          return Apollo.useLazyQuery<IFetchArtistQuery, IFetchArtistQueryVariables>(FetchArtistDocument, baseOptions);
        }
export type FetchArtistQueryHookResult = ReturnType<typeof useFetchArtistQuery>;
export type FetchArtistLazyQueryHookResult = ReturnType<typeof useFetchArtistLazyQuery>;
export type FetchArtistQueryResult = Apollo.QueryResult<IFetchArtistQuery, IFetchArtistQueryVariables>;
export const UpdateArtistDocument = gql`
    mutation UpdateArtist($id: Int!, $name: String, $starred: Boolean) {
  updateArtist(id: $id, name: $name, starred: $starred) {
    id
    name
    starred
  }
}
    `;
export type IUpdateArtistMutationFn = Apollo.MutationFunction<IUpdateArtistMutation, IUpdateArtistMutationVariables>;

/**
 * __useUpdateArtistMutation__
 *
 * To run a mutation, you first call `useUpdateArtistMutation` within a React component and pass it any options that fit your needs.
 * When your component renders, `useUpdateArtistMutation` returns a tuple that includes:
 * - A mutate function that you can call at any time to execute the mutation
 * - An object with fields that represent the current status of the mutation's execution
 *
 * @param baseOptions options that will be passed into the mutation, supported options are listed on: https://www.apollographql.com/docs/react/api/react-hooks/#options-2;
 *
 * @example
 * const [updateArtistMutation, { data, loading, error }] = useUpdateArtistMutation({
 *   variables: {
 *      id: // value for 'id'
 *      name: // value for 'name'
 *      starred: // value for 'starred'
 *   },
 * });
 */
export function useUpdateArtistMutation(baseOptions?: Apollo.MutationHookOptions<IUpdateArtistMutation, IUpdateArtistMutationVariables>) {
        return Apollo.useMutation<IUpdateArtistMutation, IUpdateArtistMutationVariables>(UpdateArtistDocument, baseOptions);
      }
export type UpdateArtistMutationHookResult = ReturnType<typeof useUpdateArtistMutation>;
export type UpdateArtistMutationResult = Apollo.MutationResult<IUpdateArtistMutation>;
export type UpdateArtistMutationOptions = Apollo.BaseMutationOptions<IUpdateArtistMutation, IUpdateArtistMutationVariables>;
export const UpdateArtistStarredDocument = gql`
    mutation UpdateArtistStarred($id: Int!, $starred: Boolean) {
  updateArtist(id: $id, starred: $starred) {
    id
    starred
  }
}
    `;
export type IUpdateArtistStarredMutationFn = Apollo.MutationFunction<IUpdateArtistStarredMutation, IUpdateArtistStarredMutationVariables>;

/**
 * __useUpdateArtistStarredMutation__
 *
 * To run a mutation, you first call `useUpdateArtistStarredMutation` within a React component and pass it any options that fit your needs.
 * When your component renders, `useUpdateArtistStarredMutation` returns a tuple that includes:
 * - A mutate function that you can call at any time to execute the mutation
 * - An object with fields that represent the current status of the mutation's execution
 *
 * @param baseOptions options that will be passed into the mutation, supported options are listed on: https://www.apollographql.com/docs/react/api/react-hooks/#options-2;
 *
 * @example
 * const [updateArtistStarredMutation, { data, loading, error }] = useUpdateArtistStarredMutation({
 *   variables: {
 *      id: // value for 'id'
 *      starred: // value for 'starred'
 *   },
 * });
 */
export function useUpdateArtistStarredMutation(baseOptions?: Apollo.MutationHookOptions<IUpdateArtistStarredMutation, IUpdateArtistStarredMutationVariables>) {
        return Apollo.useMutation<IUpdateArtistStarredMutation, IUpdateArtistStarredMutationVariables>(UpdateArtistStarredDocument, baseOptions);
      }
export type UpdateArtistStarredMutationHookResult = ReturnType<typeof useUpdateArtistStarredMutation>;
export type UpdateArtistStarredMutationResult = Apollo.MutationResult<IUpdateArtistStarredMutation>;
export type UpdateArtistStarredMutationOptions = Apollo.BaseMutationOptions<IUpdateArtistStarredMutation, IUpdateArtistStarredMutationVariables>;
export const FetchCollectionsDocument = gql`
    query FetchCollections($types: [CollectionType]) {
  collections(types: $types) {
    results {
      ...CollectionFields
    }
  }
}
    ${CollectionFieldsFragmentDoc}`;

/**
 * __useFetchCollectionsQuery__
 *
 * To run a query within a React component, call `useFetchCollectionsQuery` and pass it any options that fit your needs.
 * When your component renders, `useFetchCollectionsQuery` returns an object from Apollo Client that contains loading, error, and data properties
 * you can use to render your UI.
 *
 * @param baseOptions options that will be passed into the query, supported options are listed on: https://www.apollographql.com/docs/react/api/react-hooks/#options;
 *
 * @example
 * const { data, loading, error } = useFetchCollectionsQuery({
 *   variables: {
 *      types: // value for 'types'
 *   },
 * });
 */
export function useFetchCollectionsQuery(baseOptions?: Apollo.QueryHookOptions<IFetchCollectionsQuery, IFetchCollectionsQueryVariables>) {
        return Apollo.useQuery<IFetchCollectionsQuery, IFetchCollectionsQueryVariables>(FetchCollectionsDocument, baseOptions);
      }
export function useFetchCollectionsLazyQuery(baseOptions?: Apollo.LazyQueryHookOptions<IFetchCollectionsQuery, IFetchCollectionsQueryVariables>) {
          return Apollo.useLazyQuery<IFetchCollectionsQuery, IFetchCollectionsQueryVariables>(FetchCollectionsDocument, baseOptions);
        }
export type FetchCollectionsQueryHookResult = ReturnType<typeof useFetchCollectionsQuery>;
export type FetchCollectionsLazyQueryHookResult = ReturnType<typeof useFetchCollectionsLazyQuery>;
export type FetchCollectionsQueryResult = Apollo.QueryResult<IFetchCollectionsQuery, IFetchCollectionsQueryVariables>;
export const FetchCollectionDocument = gql`
    query FetchCollection($id: Int!) {
  collection(id: $id) {
    ...CollectionFields
  }
}
    ${CollectionFieldsFragmentDoc}`;

/**
 * __useFetchCollectionQuery__
 *
 * To run a query within a React component, call `useFetchCollectionQuery` and pass it any options that fit your needs.
 * When your component renders, `useFetchCollectionQuery` returns an object from Apollo Client that contains loading, error, and data properties
 * you can use to render your UI.
 *
 * @param baseOptions options that will be passed into the query, supported options are listed on: https://www.apollographql.com/docs/react/api/react-hooks/#options;
 *
 * @example
 * const { data, loading, error } = useFetchCollectionQuery({
 *   variables: {
 *      id: // value for 'id'
 *   },
 * });
 */
export function useFetchCollectionQuery(baseOptions: Apollo.QueryHookOptions<IFetchCollectionQuery, IFetchCollectionQueryVariables>) {
        return Apollo.useQuery<IFetchCollectionQuery, IFetchCollectionQueryVariables>(FetchCollectionDocument, baseOptions);
      }
export function useFetchCollectionLazyQuery(baseOptions?: Apollo.LazyQueryHookOptions<IFetchCollectionQuery, IFetchCollectionQueryVariables>) {
          return Apollo.useLazyQuery<IFetchCollectionQuery, IFetchCollectionQueryVariables>(FetchCollectionDocument, baseOptions);
        }
export type FetchCollectionQueryHookResult = ReturnType<typeof useFetchCollectionQuery>;
export type FetchCollectionLazyQueryHookResult = ReturnType<typeof useFetchCollectionLazyQuery>;
export type FetchCollectionQueryResult = Apollo.QueryResult<IFetchCollectionQuery, IFetchCollectionQueryVariables>;
export const UpdateCollectionDocument = gql`
    mutation UpdateCollection($id: Int!, $name: String, $starred: Boolean) {
  updateCollection(id: $id, name: $name, starred: $starred) {
    id
    name
    starred
  }
}
    `;
export type IUpdateCollectionMutationFn = Apollo.MutationFunction<IUpdateCollectionMutation, IUpdateCollectionMutationVariables>;

/**
 * __useUpdateCollectionMutation__
 *
 * To run a mutation, you first call `useUpdateCollectionMutation` within a React component and pass it any options that fit your needs.
 * When your component renders, `useUpdateCollectionMutation` returns a tuple that includes:
 * - A mutate function that you can call at any time to execute the mutation
 * - An object with fields that represent the current status of the mutation's execution
 *
 * @param baseOptions options that will be passed into the mutation, supported options are listed on: https://www.apollographql.com/docs/react/api/react-hooks/#options-2;
 *
 * @example
 * const [updateCollectionMutation, { data, loading, error }] = useUpdateCollectionMutation({
 *   variables: {
 *      id: // value for 'id'
 *      name: // value for 'name'
 *      starred: // value for 'starred'
 *   },
 * });
 */
export function useUpdateCollectionMutation(baseOptions?: Apollo.MutationHookOptions<IUpdateCollectionMutation, IUpdateCollectionMutationVariables>) {
        return Apollo.useMutation<IUpdateCollectionMutation, IUpdateCollectionMutationVariables>(UpdateCollectionDocument, baseOptions);
      }
export type UpdateCollectionMutationHookResult = ReturnType<typeof useUpdateCollectionMutation>;
export type UpdateCollectionMutationResult = Apollo.MutationResult<IUpdateCollectionMutation>;
export type UpdateCollectionMutationOptions = Apollo.BaseMutationOptions<IUpdateCollectionMutation, IUpdateCollectionMutationVariables>;
export const UpdateCollectionStarredDocument = gql`
    mutation UpdateCollectionStarred($id: Int!, $starred: Boolean) {
  updateCollection(id: $id, starred: $starred) {
    id
    starred
  }
}
    `;
export type IUpdateCollectionStarredMutationFn = Apollo.MutationFunction<IUpdateCollectionStarredMutation, IUpdateCollectionStarredMutationVariables>;

/**
 * __useUpdateCollectionStarredMutation__
 *
 * To run a mutation, you first call `useUpdateCollectionStarredMutation` within a React component and pass it any options that fit your needs.
 * When your component renders, `useUpdateCollectionStarredMutation` returns a tuple that includes:
 * - A mutate function that you can call at any time to execute the mutation
 * - An object with fields that represent the current status of the mutation's execution
 *
 * @param baseOptions options that will be passed into the mutation, supported options are listed on: https://www.apollographql.com/docs/react/api/react-hooks/#options-2;
 *
 * @example
 * const [updateCollectionStarredMutation, { data, loading, error }] = useUpdateCollectionStarredMutation({
 *   variables: {
 *      id: // value for 'id'
 *      starred: // value for 'starred'
 *   },
 * });
 */
export function useUpdateCollectionStarredMutation(baseOptions?: Apollo.MutationHookOptions<IUpdateCollectionStarredMutation, IUpdateCollectionStarredMutationVariables>) {
        return Apollo.useMutation<IUpdateCollectionStarredMutation, IUpdateCollectionStarredMutationVariables>(UpdateCollectionStarredDocument, baseOptions);
      }
export type UpdateCollectionStarredMutationHookResult = ReturnType<typeof useUpdateCollectionStarredMutation>;
export type UpdateCollectionStarredMutationResult = Apollo.MutationResult<IUpdateCollectionStarredMutation>;
export type UpdateCollectionStarredMutationOptions = Apollo.BaseMutationOptions<IUpdateCollectionStarredMutation, IUpdateCollectionStarredMutationVariables>;
export const AddReleaseToCollectionDocument = gql`
    mutation AddReleaseToCollection($collectionId: Int!, $releaseId: Int!) {
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
export type IAddReleaseToCollectionMutationFn = Apollo.MutationFunction<IAddReleaseToCollectionMutation, IAddReleaseToCollectionMutationVariables>;

/**
 * __useAddReleaseToCollectionMutation__
 *
 * To run a mutation, you first call `useAddReleaseToCollectionMutation` within a React component and pass it any options that fit your needs.
 * When your component renders, `useAddReleaseToCollectionMutation` returns a tuple that includes:
 * - A mutate function that you can call at any time to execute the mutation
 * - An object with fields that represent the current status of the mutation's execution
 *
 * @param baseOptions options that will be passed into the mutation, supported options are listed on: https://www.apollographql.com/docs/react/api/react-hooks/#options-2;
 *
 * @example
 * const [addReleaseToCollectionMutation, { data, loading, error }] = useAddReleaseToCollectionMutation({
 *   variables: {
 *      collectionId: // value for 'collectionId'
 *      releaseId: // value for 'releaseId'
 *   },
 * });
 */
export function useAddReleaseToCollectionMutation(baseOptions?: Apollo.MutationHookOptions<IAddReleaseToCollectionMutation, IAddReleaseToCollectionMutationVariables>) {
        return Apollo.useMutation<IAddReleaseToCollectionMutation, IAddReleaseToCollectionMutationVariables>(AddReleaseToCollectionDocument, baseOptions);
      }
export type AddReleaseToCollectionMutationHookResult = ReturnType<typeof useAddReleaseToCollectionMutation>;
export type AddReleaseToCollectionMutationResult = Apollo.MutationResult<IAddReleaseToCollectionMutation>;
export type AddReleaseToCollectionMutationOptions = Apollo.BaseMutationOptions<IAddReleaseToCollectionMutation, IAddReleaseToCollectionMutationVariables>;
export const DelReleaseFromCollectionDocument = gql`
    mutation DelReleaseFromCollection($collectionId: Int!, $releaseId: Int!) {
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
export type IDelReleaseFromCollectionMutationFn = Apollo.MutationFunction<IDelReleaseFromCollectionMutation, IDelReleaseFromCollectionMutationVariables>;

/**
 * __useDelReleaseFromCollectionMutation__
 *
 * To run a mutation, you first call `useDelReleaseFromCollectionMutation` within a React component and pass it any options that fit your needs.
 * When your component renders, `useDelReleaseFromCollectionMutation` returns a tuple that includes:
 * - A mutate function that you can call at any time to execute the mutation
 * - An object with fields that represent the current status of the mutation's execution
 *
 * @param baseOptions options that will be passed into the mutation, supported options are listed on: https://www.apollographql.com/docs/react/api/react-hooks/#options-2;
 *
 * @example
 * const [delReleaseFromCollectionMutation, { data, loading, error }] = useDelReleaseFromCollectionMutation({
 *   variables: {
 *      collectionId: // value for 'collectionId'
 *      releaseId: // value for 'releaseId'
 *   },
 * });
 */
export function useDelReleaseFromCollectionMutation(baseOptions?: Apollo.MutationHookOptions<IDelReleaseFromCollectionMutation, IDelReleaseFromCollectionMutationVariables>) {
        return Apollo.useMutation<IDelReleaseFromCollectionMutation, IDelReleaseFromCollectionMutationVariables>(DelReleaseFromCollectionDocument, baseOptions);
      }
export type DelReleaseFromCollectionMutationHookResult = ReturnType<typeof useDelReleaseFromCollectionMutation>;
export type DelReleaseFromCollectionMutationResult = Apollo.MutationResult<IDelReleaseFromCollectionMutation>;
export type DelReleaseFromCollectionMutationOptions = Apollo.BaseMutationOptions<IDelReleaseFromCollectionMutation, IDelReleaseFromCollectionMutationVariables>;
export const FetchReleasesDocument = gql`
    query FetchReleases($search: String, $collectionIds: [Int], $artistIds: [Int], $releaseTypes: [ReleaseType], $years: [Int], $ratings: [Int], $page: Int, $perPage: Int, $sort: ReleaseSort, $asc: Boolean) {
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
 * __useFetchReleasesQuery__
 *
 * To run a query within a React component, call `useFetchReleasesQuery` and pass it any options that fit your needs.
 * When your component renders, `useFetchReleasesQuery` returns an object from Apollo Client that contains loading, error, and data properties
 * you can use to render your UI.
 *
 * @param baseOptions options that will be passed into the query, supported options are listed on: https://www.apollographql.com/docs/react/api/react-hooks/#options;
 *
 * @example
 * const { data, loading, error } = useFetchReleasesQuery({
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
export function useFetchReleasesQuery(baseOptions?: Apollo.QueryHookOptions<IFetchReleasesQuery, IFetchReleasesQueryVariables>) {
        return Apollo.useQuery<IFetchReleasesQuery, IFetchReleasesQueryVariables>(FetchReleasesDocument, baseOptions);
      }
export function useFetchReleasesLazyQuery(baseOptions?: Apollo.LazyQueryHookOptions<IFetchReleasesQuery, IFetchReleasesQueryVariables>) {
          return Apollo.useLazyQuery<IFetchReleasesQuery, IFetchReleasesQueryVariables>(FetchReleasesDocument, baseOptions);
        }
export type FetchReleasesQueryHookResult = ReturnType<typeof useFetchReleasesQuery>;
export type FetchReleasesLazyQueryHookResult = ReturnType<typeof useFetchReleasesLazyQuery>;
export type FetchReleasesQueryResult = Apollo.QueryResult<IFetchReleasesQuery, IFetchReleasesQueryVariables>;
export const FetchReleasesRecentlyAddedDocument = gql`
    query FetchReleasesRecentlyAdded {
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
 * __useFetchReleasesRecentlyAddedQuery__
 *
 * To run a query within a React component, call `useFetchReleasesRecentlyAddedQuery` and pass it any options that fit your needs.
 * When your component renders, `useFetchReleasesRecentlyAddedQuery` returns an object from Apollo Client that contains loading, error, and data properties
 * you can use to render your UI.
 *
 * @param baseOptions options that will be passed into the query, supported options are listed on: https://www.apollographql.com/docs/react/api/react-hooks/#options;
 *
 * @example
 * const { data, loading, error } = useFetchReleasesRecentlyAddedQuery({
 *   variables: {
 *   },
 * });
 */
export function useFetchReleasesRecentlyAddedQuery(baseOptions?: Apollo.QueryHookOptions<IFetchReleasesRecentlyAddedQuery, IFetchReleasesRecentlyAddedQueryVariables>) {
        return Apollo.useQuery<IFetchReleasesRecentlyAddedQuery, IFetchReleasesRecentlyAddedQueryVariables>(FetchReleasesRecentlyAddedDocument, baseOptions);
      }
export function useFetchReleasesRecentlyAddedLazyQuery(baseOptions?: Apollo.LazyQueryHookOptions<IFetchReleasesRecentlyAddedQuery, IFetchReleasesRecentlyAddedQueryVariables>) {
          return Apollo.useLazyQuery<IFetchReleasesRecentlyAddedQuery, IFetchReleasesRecentlyAddedQueryVariables>(FetchReleasesRecentlyAddedDocument, baseOptions);
        }
export type FetchReleasesRecentlyAddedQueryHookResult = ReturnType<typeof useFetchReleasesRecentlyAddedQuery>;
export type FetchReleasesRecentlyAddedLazyQueryHookResult = ReturnType<typeof useFetchReleasesRecentlyAddedLazyQuery>;
export type FetchReleasesRecentlyAddedQueryResult = Apollo.QueryResult<IFetchReleasesRecentlyAddedQuery, IFetchReleasesRecentlyAddedQueryVariables>;
export const FetchReleaseDocument = gql`
    query FetchRelease($id: Int!) {
  release(id: $id) {
    ...FullReleaseFields
  }
}
    ${FullReleaseFieldsFragmentDoc}`;

/**
 * __useFetchReleaseQuery__
 *
 * To run a query within a React component, call `useFetchReleaseQuery` and pass it any options that fit your needs.
 * When your component renders, `useFetchReleaseQuery` returns an object from Apollo Client that contains loading, error, and data properties
 * you can use to render your UI.
 *
 * @param baseOptions options that will be passed into the query, supported options are listed on: https://www.apollographql.com/docs/react/api/react-hooks/#options;
 *
 * @example
 * const { data, loading, error } = useFetchReleaseQuery({
 *   variables: {
 *      id: // value for 'id'
 *   },
 * });
 */
export function useFetchReleaseQuery(baseOptions: Apollo.QueryHookOptions<IFetchReleaseQuery, IFetchReleaseQueryVariables>) {
        return Apollo.useQuery<IFetchReleaseQuery, IFetchReleaseQueryVariables>(FetchReleaseDocument, baseOptions);
      }
export function useFetchReleaseLazyQuery(baseOptions?: Apollo.LazyQueryHookOptions<IFetchReleaseQuery, IFetchReleaseQueryVariables>) {
          return Apollo.useLazyQuery<IFetchReleaseQuery, IFetchReleaseQueryVariables>(FetchReleaseDocument, baseOptions);
        }
export type FetchReleaseQueryHookResult = ReturnType<typeof useFetchReleaseQuery>;
export type FetchReleaseLazyQueryHookResult = ReturnType<typeof useFetchReleaseLazyQuery>;
export type FetchReleaseQueryResult = Apollo.QueryResult<IFetchReleaseQuery, IFetchReleaseQueryVariables>;
export const FetchReleaseYearsDocument = gql`
    query FetchReleaseYears {
  releaseYears
}
    `;

/**
 * __useFetchReleaseYearsQuery__
 *
 * To run a query within a React component, call `useFetchReleaseYearsQuery` and pass it any options that fit your needs.
 * When your component renders, `useFetchReleaseYearsQuery` returns an object from Apollo Client that contains loading, error, and data properties
 * you can use to render your UI.
 *
 * @param baseOptions options that will be passed into the query, supported options are listed on: https://www.apollographql.com/docs/react/api/react-hooks/#options;
 *
 * @example
 * const { data, loading, error } = useFetchReleaseYearsQuery({
 *   variables: {
 *   },
 * });
 */
export function useFetchReleaseYearsQuery(baseOptions?: Apollo.QueryHookOptions<IFetchReleaseYearsQuery, IFetchReleaseYearsQueryVariables>) {
        return Apollo.useQuery<IFetchReleaseYearsQuery, IFetchReleaseYearsQueryVariables>(FetchReleaseYearsDocument, baseOptions);
      }
export function useFetchReleaseYearsLazyQuery(baseOptions?: Apollo.LazyQueryHookOptions<IFetchReleaseYearsQuery, IFetchReleaseYearsQueryVariables>) {
          return Apollo.useLazyQuery<IFetchReleaseYearsQuery, IFetchReleaseYearsQueryVariables>(FetchReleaseYearsDocument, baseOptions);
        }
export type FetchReleaseYearsQueryHookResult = ReturnType<typeof useFetchReleaseYearsQuery>;
export type FetchReleaseYearsLazyQueryHookResult = ReturnType<typeof useFetchReleaseYearsLazyQuery>;
export type FetchReleaseYearsQueryResult = Apollo.QueryResult<IFetchReleaseYearsQuery, IFetchReleaseYearsQueryVariables>;
export const UpdateReleaseDocument = gql`
    mutation UpdateRelease($id: Int!, $title: String, $releaseType: ReleaseType, $releaseYear: Int, $releaseDate: String, $rating: Int) {
  updateRelease(
    id: $id
    title: $title
    releaseType: $releaseType
    releaseYear: $releaseYear
    releaseDate: $releaseDate
    rating: $rating
  ) {
    id
    title
    releaseType
    releaseYear
    releaseDate
    rating
  }
}
    `;
export type IUpdateReleaseMutationFn = Apollo.MutationFunction<IUpdateReleaseMutation, IUpdateReleaseMutationVariables>;

/**
 * __useUpdateReleaseMutation__
 *
 * To run a mutation, you first call `useUpdateReleaseMutation` within a React component and pass it any options that fit your needs.
 * When your component renders, `useUpdateReleaseMutation` returns a tuple that includes:
 * - A mutate function that you can call at any time to execute the mutation
 * - An object with fields that represent the current status of the mutation's execution
 *
 * @param baseOptions options that will be passed into the mutation, supported options are listed on: https://www.apollographql.com/docs/react/api/react-hooks/#options-2;
 *
 * @example
 * const [updateReleaseMutation, { data, loading, error }] = useUpdateReleaseMutation({
 *   variables: {
 *      id: // value for 'id'
 *      title: // value for 'title'
 *      releaseType: // value for 'releaseType'
 *      releaseYear: // value for 'releaseYear'
 *      releaseDate: // value for 'releaseDate'
 *      rating: // value for 'rating'
 *   },
 * });
 */
export function useUpdateReleaseMutation(baseOptions?: Apollo.MutationHookOptions<IUpdateReleaseMutation, IUpdateReleaseMutationVariables>) {
        return Apollo.useMutation<IUpdateReleaseMutation, IUpdateReleaseMutationVariables>(UpdateReleaseDocument, baseOptions);
      }
export type UpdateReleaseMutationHookResult = ReturnType<typeof useUpdateReleaseMutation>;
export type UpdateReleaseMutationResult = Apollo.MutationResult<IUpdateReleaseMutation>;
export type UpdateReleaseMutationOptions = Apollo.BaseMutationOptions<IUpdateReleaseMutation, IUpdateReleaseMutationVariables>;
export const UpdateReleaseRatingDocument = gql`
    mutation UpdateReleaseRating($id: Int!, $rating: Int) {
  updateRelease(id: $id, rating: $rating) {
    id
    rating
  }
}
    `;
export type IUpdateReleaseRatingMutationFn = Apollo.MutationFunction<IUpdateReleaseRatingMutation, IUpdateReleaseRatingMutationVariables>;

/**
 * __useUpdateReleaseRatingMutation__
 *
 * To run a mutation, you first call `useUpdateReleaseRatingMutation` within a React component and pass it any options that fit your needs.
 * When your component renders, `useUpdateReleaseRatingMutation` returns a tuple that includes:
 * - A mutate function that you can call at any time to execute the mutation
 * - An object with fields that represent the current status of the mutation's execution
 *
 * @param baseOptions options that will be passed into the mutation, supported options are listed on: https://www.apollographql.com/docs/react/api/react-hooks/#options-2;
 *
 * @example
 * const [updateReleaseRatingMutation, { data, loading, error }] = useUpdateReleaseRatingMutation({
 *   variables: {
 *      id: // value for 'id'
 *      rating: // value for 'rating'
 *   },
 * });
 */
export function useUpdateReleaseRatingMutation(baseOptions?: Apollo.MutationHookOptions<IUpdateReleaseRatingMutation, IUpdateReleaseRatingMutationVariables>) {
        return Apollo.useMutation<IUpdateReleaseRatingMutation, IUpdateReleaseRatingMutationVariables>(UpdateReleaseRatingDocument, baseOptions);
      }
export type UpdateReleaseRatingMutationHookResult = ReturnType<typeof useUpdateReleaseRatingMutation>;
export type UpdateReleaseRatingMutationResult = Apollo.MutationResult<IUpdateReleaseRatingMutation>;
export type UpdateReleaseRatingMutationOptions = Apollo.BaseMutationOptions<IUpdateReleaseRatingMutation, IUpdateReleaseRatingMutationVariables>;
export const FetchUserDocument = gql`
    query FetchUser {
  user {
    ...UserFields
  }
}
    ${UserFieldsFragmentDoc}`;

/**
 * __useFetchUserQuery__
 *
 * To run a query within a React component, call `useFetchUserQuery` and pass it any options that fit your needs.
 * When your component renders, `useFetchUserQuery` returns an object from Apollo Client that contains loading, error, and data properties
 * you can use to render your UI.
 *
 * @param baseOptions options that will be passed into the query, supported options are listed on: https://www.apollographql.com/docs/react/api/react-hooks/#options;
 *
 * @example
 * const { data, loading, error } = useFetchUserQuery({
 *   variables: {
 *   },
 * });
 */
export function useFetchUserQuery(baseOptions?: Apollo.QueryHookOptions<IFetchUserQuery, IFetchUserQueryVariables>) {
        return Apollo.useQuery<IFetchUserQuery, IFetchUserQueryVariables>(FetchUserDocument, baseOptions);
      }
export function useFetchUserLazyQuery(baseOptions?: Apollo.LazyQueryHookOptions<IFetchUserQuery, IFetchUserQueryVariables>) {
          return Apollo.useLazyQuery<IFetchUserQuery, IFetchUserQueryVariables>(FetchUserDocument, baseOptions);
        }
export type FetchUserQueryHookResult = ReturnType<typeof useFetchUserQuery>;
export type FetchUserLazyQueryHookResult = ReturnType<typeof useFetchUserLazyQuery>;
export type FetchUserQueryResult = Apollo.QueryResult<IFetchUserQuery, IFetchUserQueryVariables>;
export const UpdateUserDocument = gql`
    mutation UpdateUser($nickname: String) {
  updateUser(nickname: $nickname) {
    id
    nickname
  }
}
    `;
export type IUpdateUserMutationFn = Apollo.MutationFunction<IUpdateUserMutation, IUpdateUserMutationVariables>;

/**
 * __useUpdateUserMutation__
 *
 * To run a mutation, you first call `useUpdateUserMutation` within a React component and pass it any options that fit your needs.
 * When your component renders, `useUpdateUserMutation` returns a tuple that includes:
 * - A mutate function that you can call at any time to execute the mutation
 * - An object with fields that represent the current status of the mutation's execution
 *
 * @param baseOptions options that will be passed into the mutation, supported options are listed on: https://www.apollographql.com/docs/react/api/react-hooks/#options-2;
 *
 * @example
 * const [updateUserMutation, { data, loading, error }] = useUpdateUserMutation({
 *   variables: {
 *      nickname: // value for 'nickname'
 *   },
 * });
 */
export function useUpdateUserMutation(baseOptions?: Apollo.MutationHookOptions<IUpdateUserMutation, IUpdateUserMutationVariables>) {
        return Apollo.useMutation<IUpdateUserMutation, IUpdateUserMutationVariables>(UpdateUserDocument, baseOptions);
      }
export type UpdateUserMutationHookResult = ReturnType<typeof useUpdateUserMutation>;
export type UpdateUserMutationResult = Apollo.MutationResult<IUpdateUserMutation>;
export type UpdateUserMutationOptions = Apollo.BaseMutationOptions<IUpdateUserMutation, IUpdateUserMutationVariables>;
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
export type MutationKeySpecifier = ('createArtist' | 'updateArtist' | 'createCollection' | 'updateCollection' | 'addReleaseToCollection' | 'delReleaseFromCollection' | 'createPlaylist' | 'updatePlaylist' | 'addTrackToPlaylist' | 'delTrackFromPlaylist' | 'createRelease' | 'updateRelease' | 'addArtistToRelease' | 'delArtistFromRelease' | 'updateTrack' | 'addArtistToTrack' | 'delArtistFromTrack' | 'updateUser' | 'newToken' | MutationKeySpecifier)[];
export type MutationFieldPolicy = {
	createArtist?: FieldPolicy<any> | FieldReadFunction<any>,
	updateArtist?: FieldPolicy<any> | FieldReadFunction<any>,
	createCollection?: FieldPolicy<any> | FieldReadFunction<any>,
	updateCollection?: FieldPolicy<any> | FieldReadFunction<any>,
	addReleaseToCollection?: FieldPolicy<any> | FieldReadFunction<any>,
	delReleaseFromCollection?: FieldPolicy<any> | FieldReadFunction<any>,
	createPlaylist?: FieldPolicy<any> | FieldReadFunction<any>,
	updatePlaylist?: FieldPolicy<any> | FieldReadFunction<any>,
	addTrackToPlaylist?: FieldPolicy<any> | FieldReadFunction<any>,
	delTrackFromPlaylist?: FieldPolicy<any> | FieldReadFunction<any>,
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
export type PlaylistKeySpecifier = ('id' | 'name' | 'starred' | 'type' | 'numTracks' | 'lastUpdatedOn' | 'imageId' | 'tracks' | 'topGenres' | PlaylistKeySpecifier)[];
export type PlaylistFieldPolicy = {
	id?: FieldPolicy<any> | FieldReadFunction<any>,
	name?: FieldPolicy<any> | FieldReadFunction<any>,
	starred?: FieldPolicy<any> | FieldReadFunction<any>,
	type?: FieldPolicy<any> | FieldReadFunction<any>,
	numTracks?: FieldPolicy<any> | FieldReadFunction<any>,
	lastUpdatedOn?: FieldPolicy<any> | FieldReadFunction<any>,
	imageId?: FieldPolicy<any> | FieldReadFunction<any>,
	tracks?: FieldPolicy<any> | FieldReadFunction<any>,
	topGenres?: FieldPolicy<any> | FieldReadFunction<any>
};
export type PlaylistsKeySpecifier = ('results' | PlaylistsKeySpecifier)[];
export type PlaylistsFieldPolicy = {
	results?: FieldPolicy<any> | FieldReadFunction<any>
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
export type PlaylistAndTrackKeySpecifier = ('playlist' | 'track' | PlaylistAndTrackKeySpecifier)[];
export type PlaylistAndTrackFieldPolicy = {
	playlist?: FieldPolicy<any> | FieldReadFunction<any>,
	track?: FieldPolicy<any> | FieldReadFunction<any>
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
	PlaylistAndTrack?: Omit<TypePolicy, "fields" | "keyFields"> & {
		keyFields?: false | PlaylistAndTrackKeySpecifier | (() => undefined | PlaylistAndTrackKeySpecifier),
		fields?: PlaylistAndTrackFieldPolicy,
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