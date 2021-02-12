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

export type FetchArtistsQueryVariables = Exact<{ [key: string]: never; }>;


export type FetchArtistsQuery = (
  { __typename?: 'Query' }
  & { artists?: Maybe<(
    { __typename?: 'Artists' }
    & { results: Array<Maybe<(
      { __typename?: 'Artist' }
      & ArtistFieldsFragment
    )>> }
  )> }
);

export type FetchArtistQueryVariables = Exact<{
  id: Scalars['Int'];
}>;


export type FetchArtistQuery = (
  { __typename?: 'Query' }
  & { artist?: Maybe<(
    { __typename?: 'Artist' }
    & ArtistFieldsFragment
  )> }
);

export type UpdateArtistMutationVariables = Exact<{
  id: Scalars['Int'];
  name?: Maybe<Scalars['String']>;
  starred?: Maybe<Scalars['Boolean']>;
}>;


export type UpdateArtistMutation = (
  { __typename?: 'Mutation' }
  & { updateArtist?: Maybe<(
    { __typename?: 'Artist' }
    & ArtistFieldsFragment
  )> }
);

export type FetchCollectionsQueryVariables = Exact<{
  types?: Maybe<Array<Maybe<CollectionType>> | Maybe<CollectionType>>;
}>;


export type FetchCollectionsQuery = (
  { __typename?: 'Query' }
  & { collections?: Maybe<(
    { __typename?: 'Collections' }
    & { results: Array<Maybe<(
      { __typename?: 'Collection' }
      & CollectionFieldsFragment
    )>> }
  )> }
);

export type FetchCollectionQueryVariables = Exact<{
  id: Scalars['Int'];
}>;


export type FetchCollectionQuery = (
  { __typename?: 'Query' }
  & { collection?: Maybe<(
    { __typename?: 'Collection' }
    & CollectionFieldsFragment
  )> }
);

export type UpdateCollectionMutationVariables = Exact<{
  id: Scalars['Int'];
  name?: Maybe<Scalars['String']>;
  starred?: Maybe<Scalars['Boolean']>;
}>;


export type UpdateCollectionMutation = (
  { __typename?: 'Mutation' }
  & { updateCollection?: Maybe<(
    { __typename?: 'Collection' }
    & CollectionFieldsFragment
  )> }
);

export type AddReleaseToCollectionMutationVariables = Exact<{
  collectionId: Scalars['Int'];
  releaseId: Scalars['Int'];
}>;


export type AddReleaseToCollectionMutation = (
  { __typename?: 'Mutation' }
  & { addReleaseToCollection?: Maybe<(
    { __typename?: 'CollectionAndRelease' }
    & { collection: (
      { __typename?: 'Collection' }
      & CollectionFieldsFragment
    ), release: (
      { __typename?: 'Release' }
      & ReleaseFieldsFragment
    ) }
  )> }
);

export type DelReleaseFromCollectionMutationVariables = Exact<{
  collectionId: Scalars['Int'];
  releaseId: Scalars['Int'];
}>;


export type DelReleaseFromCollectionMutation = (
  { __typename?: 'Mutation' }
  & { delReleaseFromCollection?: Maybe<(
    { __typename?: 'CollectionAndRelease' }
    & { collection: (
      { __typename?: 'Collection' }
      & CollectionFieldsFragment
    ), release: (
      { __typename?: 'Release' }
      & ReleaseFieldsFragment
    ) }
  )> }
);

export type UserFieldsFragment = (
  { __typename?: 'User' }
  & Pick<User, 'id' | 'nickname'>
);

export type ReleaseFieldsFragment = (
  { __typename?: 'Release' }
  & Pick<Release, 'id' | 'title' | 'releaseType' | 'addedOn' | 'inInbox' | 'inFavorites' | 'releaseYear' | 'releaseDate' | 'rating' | 'numTracks' | 'runtime' | 'imageId'>
);

export type ArtistFieldsFragment = (
  { __typename?: 'Artist' }
  & Pick<Artist, 'id' | 'name' | 'starred' | 'numReleases' | 'imageId'>
);

export type CollectionFieldsFragment = (
  { __typename?: 'Collection' }
  & Pick<Collection, 'id' | 'name' | 'starred' | 'type' | 'numReleases' | 'lastUpdatedOn' | 'imageId'>
);

export type TrackFieldsFragment = (
  { __typename?: 'Track' }
  & Pick<Track, 'id' | 'title' | 'duration' | 'trackNumber' | 'discNumber'>
);

export type FullReleaseFieldsFragment = (
  { __typename?: 'Release' }
  & { artists: Array<Maybe<(
    { __typename?: 'Artist' }
    & Pick<Artist, 'id' | 'name'>
  )>>, collages: Array<Maybe<(
    { __typename?: 'Collection' }
    & Pick<Collection, 'id' | 'name'>
  )>>, labels: Array<Maybe<(
    { __typename?: 'Collection' }
    & Pick<Collection, 'id' | 'name'>
  )>>, genres: Array<Maybe<(
    { __typename?: 'Collection' }
    & Pick<Collection, 'id' | 'name'>
  )>>, tracks: Array<Maybe<(
    { __typename?: 'Track' }
    & { release: (
      { __typename?: 'Release' }
      & Pick<Release, 'id' | 'imageId'>
    ), artists: Array<Maybe<(
      { __typename?: 'TrackArtist' }
      & Pick<TrackArtist, 'role'>
      & { artist: (
        { __typename?: 'Artist' }
        & Pick<Artist, 'id' | 'name'>
      ) }
    )>> }
    & TrackFieldsFragment
  )>> }
  & ReleaseFieldsFragment
);

export type FetchReleasesQueryVariables = Exact<{
  search?: Maybe<Scalars['String']>;
  collectionIds?: Maybe<Array<Maybe<Scalars['Int']>> | Maybe<Scalars['Int']>>;
  artistIds?: Maybe<Array<Maybe<Scalars['Int']>> | Maybe<Scalars['Int']>>;
  releaseTypes?: Maybe<Array<Maybe<ReleaseType>> | Maybe<ReleaseType>>;
  years?: Maybe<Array<Maybe<Scalars['Int']>> | Maybe<Scalars['Int']>>;
  ratings?: Maybe<Array<Maybe<Scalars['Int']>> | Maybe<Scalars['Int']>>;
  page?: Maybe<Scalars['Int']>;
  perPage?: Maybe<Scalars['Int']>;
  sort?: Maybe<ReleaseSort>;
  asc?: Maybe<Scalars['Boolean']>;
}>;


export type FetchReleasesQuery = (
  { __typename?: 'Query' }
  & { releases?: Maybe<(
    { __typename?: 'Releases' }
    & Pick<Releases, 'total'>
    & { results: Array<Maybe<(
      { __typename?: 'Release' }
      & { artists: Array<Maybe<(
        { __typename?: 'Artist' }
        & Pick<Artist, 'id' | 'name'>
      )>>, genres: Array<Maybe<(
        { __typename?: 'Collection' }
        & Pick<Collection, 'id' | 'name'>
      )>> }
      & ReleaseFieldsFragment
    )>> }
  )> }
);

export type FetchReleasesRecentlyAddedQueryVariables = Exact<{ [key: string]: never; }>;


export type FetchReleasesRecentlyAddedQuery = (
  { __typename?: 'Query' }
  & { releases?: Maybe<(
    { __typename?: 'Releases' }
    & { results: Array<Maybe<(
      { __typename?: 'Release' }
      & { artists: Array<Maybe<(
        { __typename?: 'Artist' }
        & Pick<Artist, 'id' | 'name'>
      )>>, genres: Array<Maybe<(
        { __typename?: 'Collection' }
        & Pick<Collection, 'id' | 'name'>
      )>> }
      & ReleaseFieldsFragment
    )>> }
  )> }
);

export type FetchReleaseQueryVariables = Exact<{
  id: Scalars['Int'];
}>;


export type FetchReleaseQuery = (
  { __typename?: 'Query' }
  & { release?: Maybe<(
    { __typename?: 'Release' }
    & FullReleaseFieldsFragment
  )> }
);

export type FetchReleaseYearsQueryVariables = Exact<{ [key: string]: never; }>;


export type FetchReleaseYearsQuery = (
  { __typename?: 'Query' }
  & Pick<Query, 'releaseYears'>
);

export type UpdateReleaseMutationVariables = Exact<{
  id: Scalars['Int'];
  title?: Maybe<Scalars['String']>;
  releaseType?: Maybe<ReleaseType>;
  releaseYear?: Maybe<Scalars['Int']>;
  releaseDate?: Maybe<Scalars['String']>;
  rating?: Maybe<Scalars['Int']>;
}>;


export type UpdateReleaseMutation = (
  { __typename?: 'Mutation' }
  & { updateRelease?: Maybe<(
    { __typename?: 'Release' }
    & FullReleaseFieldsFragment
  )> }
);

export type FetchUserQueryVariables = Exact<{ [key: string]: never; }>;


export type FetchUserQuery = (
  { __typename?: 'Query' }
  & { user?: Maybe<(
    { __typename?: 'User' }
    & UserFieldsFragment
  )> }
);

export type UpdateUserMutationVariables = Exact<{
  nickname?: Maybe<Scalars['String']>;
}>;


export type UpdateUserMutation = (
  { __typename?: 'Mutation' }
  & { updateUser?: Maybe<(
    { __typename?: 'User' }
    & UserFieldsFragment
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
export function useFetchArtistsQuery(baseOptions?: Apollo.QueryHookOptions<FetchArtistsQuery, FetchArtistsQueryVariables>) {
        return Apollo.useQuery<FetchArtistsQuery, FetchArtistsQueryVariables>(FetchArtistsDocument, baseOptions);
      }
export function useFetchArtistsLazyQuery(baseOptions?: Apollo.LazyQueryHookOptions<FetchArtistsQuery, FetchArtistsQueryVariables>) {
          return Apollo.useLazyQuery<FetchArtistsQuery, FetchArtistsQueryVariables>(FetchArtistsDocument, baseOptions);
        }
export type FetchArtistsQueryHookResult = ReturnType<typeof useFetchArtistsQuery>;
export type FetchArtistsLazyQueryHookResult = ReturnType<typeof useFetchArtistsLazyQuery>;
export type FetchArtistsQueryResult = Apollo.QueryResult<FetchArtistsQuery, FetchArtistsQueryVariables>;
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
export function useFetchArtistQuery(baseOptions: Apollo.QueryHookOptions<FetchArtistQuery, FetchArtistQueryVariables>) {
        return Apollo.useQuery<FetchArtistQuery, FetchArtistQueryVariables>(FetchArtistDocument, baseOptions);
      }
export function useFetchArtistLazyQuery(baseOptions?: Apollo.LazyQueryHookOptions<FetchArtistQuery, FetchArtistQueryVariables>) {
          return Apollo.useLazyQuery<FetchArtistQuery, FetchArtistQueryVariables>(FetchArtistDocument, baseOptions);
        }
export type FetchArtistQueryHookResult = ReturnType<typeof useFetchArtistQuery>;
export type FetchArtistLazyQueryHookResult = ReturnType<typeof useFetchArtistLazyQuery>;
export type FetchArtistQueryResult = Apollo.QueryResult<FetchArtistQuery, FetchArtistQueryVariables>;
export const UpdateArtistDocument = gql`
    mutation UpdateArtist($id: Int!, $name: String, $starred: Boolean) {
  updateArtist(id: $id, name: $name, starred: $starred) {
    ...ArtistFields
  }
}
    ${ArtistFieldsFragmentDoc}`;
export type UpdateArtistMutationFn = Apollo.MutationFunction<UpdateArtistMutation, UpdateArtistMutationVariables>;

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
export function useUpdateArtistMutation(baseOptions?: Apollo.MutationHookOptions<UpdateArtistMutation, UpdateArtistMutationVariables>) {
        return Apollo.useMutation<UpdateArtistMutation, UpdateArtistMutationVariables>(UpdateArtistDocument, baseOptions);
      }
export type UpdateArtistMutationHookResult = ReturnType<typeof useUpdateArtistMutation>;
export type UpdateArtistMutationResult = Apollo.MutationResult<UpdateArtistMutation>;
export type UpdateArtistMutationOptions = Apollo.BaseMutationOptions<UpdateArtistMutation, UpdateArtistMutationVariables>;
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
export function useFetchCollectionsQuery(baseOptions?: Apollo.QueryHookOptions<FetchCollectionsQuery, FetchCollectionsQueryVariables>) {
        return Apollo.useQuery<FetchCollectionsQuery, FetchCollectionsQueryVariables>(FetchCollectionsDocument, baseOptions);
      }
export function useFetchCollectionsLazyQuery(baseOptions?: Apollo.LazyQueryHookOptions<FetchCollectionsQuery, FetchCollectionsQueryVariables>) {
          return Apollo.useLazyQuery<FetchCollectionsQuery, FetchCollectionsQueryVariables>(FetchCollectionsDocument, baseOptions);
        }
export type FetchCollectionsQueryHookResult = ReturnType<typeof useFetchCollectionsQuery>;
export type FetchCollectionsLazyQueryHookResult = ReturnType<typeof useFetchCollectionsLazyQuery>;
export type FetchCollectionsQueryResult = Apollo.QueryResult<FetchCollectionsQuery, FetchCollectionsQueryVariables>;
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
export function useFetchCollectionQuery(baseOptions: Apollo.QueryHookOptions<FetchCollectionQuery, FetchCollectionQueryVariables>) {
        return Apollo.useQuery<FetchCollectionQuery, FetchCollectionQueryVariables>(FetchCollectionDocument, baseOptions);
      }
export function useFetchCollectionLazyQuery(baseOptions?: Apollo.LazyQueryHookOptions<FetchCollectionQuery, FetchCollectionQueryVariables>) {
          return Apollo.useLazyQuery<FetchCollectionQuery, FetchCollectionQueryVariables>(FetchCollectionDocument, baseOptions);
        }
export type FetchCollectionQueryHookResult = ReturnType<typeof useFetchCollectionQuery>;
export type FetchCollectionLazyQueryHookResult = ReturnType<typeof useFetchCollectionLazyQuery>;
export type FetchCollectionQueryResult = Apollo.QueryResult<FetchCollectionQuery, FetchCollectionQueryVariables>;
export const UpdateCollectionDocument = gql`
    mutation UpdateCollection($id: Int!, $name: String, $starred: Boolean) {
  updateCollection(id: $id, name: $name, starred: $starred) {
    ...CollectionFields
  }
}
    ${CollectionFieldsFragmentDoc}`;
export type UpdateCollectionMutationFn = Apollo.MutationFunction<UpdateCollectionMutation, UpdateCollectionMutationVariables>;

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
export function useUpdateCollectionMutation(baseOptions?: Apollo.MutationHookOptions<UpdateCollectionMutation, UpdateCollectionMutationVariables>) {
        return Apollo.useMutation<UpdateCollectionMutation, UpdateCollectionMutationVariables>(UpdateCollectionDocument, baseOptions);
      }
export type UpdateCollectionMutationHookResult = ReturnType<typeof useUpdateCollectionMutation>;
export type UpdateCollectionMutationResult = Apollo.MutationResult<UpdateCollectionMutation>;
export type UpdateCollectionMutationOptions = Apollo.BaseMutationOptions<UpdateCollectionMutation, UpdateCollectionMutationVariables>;
export const AddReleaseToCollectionDocument = gql`
    mutation AddReleaseToCollection($collectionId: Int!, $releaseId: Int!) {
  addReleaseToCollection(collectionId: $collectionId, releaseId: $releaseId) {
    collection {
      ...CollectionFields
    }
    release {
      ...ReleaseFields
    }
  }
}
    ${CollectionFieldsFragmentDoc}
${ReleaseFieldsFragmentDoc}`;
export type AddReleaseToCollectionMutationFn = Apollo.MutationFunction<AddReleaseToCollectionMutation, AddReleaseToCollectionMutationVariables>;

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
export function useAddReleaseToCollectionMutation(baseOptions?: Apollo.MutationHookOptions<AddReleaseToCollectionMutation, AddReleaseToCollectionMutationVariables>) {
        return Apollo.useMutation<AddReleaseToCollectionMutation, AddReleaseToCollectionMutationVariables>(AddReleaseToCollectionDocument, baseOptions);
      }
export type AddReleaseToCollectionMutationHookResult = ReturnType<typeof useAddReleaseToCollectionMutation>;
export type AddReleaseToCollectionMutationResult = Apollo.MutationResult<AddReleaseToCollectionMutation>;
export type AddReleaseToCollectionMutationOptions = Apollo.BaseMutationOptions<AddReleaseToCollectionMutation, AddReleaseToCollectionMutationVariables>;
export const DelReleaseFromCollectionDocument = gql`
    mutation DelReleaseFromCollection($collectionId: Int!, $releaseId: Int!) {
  delReleaseFromCollection(collectionId: $collectionId, releaseId: $releaseId) {
    collection {
      ...CollectionFields
    }
    release {
      ...ReleaseFields
    }
  }
}
    ${CollectionFieldsFragmentDoc}
${ReleaseFieldsFragmentDoc}`;
export type DelReleaseFromCollectionMutationFn = Apollo.MutationFunction<DelReleaseFromCollectionMutation, DelReleaseFromCollectionMutationVariables>;

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
export function useDelReleaseFromCollectionMutation(baseOptions?: Apollo.MutationHookOptions<DelReleaseFromCollectionMutation, DelReleaseFromCollectionMutationVariables>) {
        return Apollo.useMutation<DelReleaseFromCollectionMutation, DelReleaseFromCollectionMutationVariables>(DelReleaseFromCollectionDocument, baseOptions);
      }
export type DelReleaseFromCollectionMutationHookResult = ReturnType<typeof useDelReleaseFromCollectionMutation>;
export type DelReleaseFromCollectionMutationResult = Apollo.MutationResult<DelReleaseFromCollectionMutation>;
export type DelReleaseFromCollectionMutationOptions = Apollo.BaseMutationOptions<DelReleaseFromCollectionMutation, DelReleaseFromCollectionMutationVariables>;
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
export function useFetchReleasesQuery(baseOptions?: Apollo.QueryHookOptions<FetchReleasesQuery, FetchReleasesQueryVariables>) {
        return Apollo.useQuery<FetchReleasesQuery, FetchReleasesQueryVariables>(FetchReleasesDocument, baseOptions);
      }
export function useFetchReleasesLazyQuery(baseOptions?: Apollo.LazyQueryHookOptions<FetchReleasesQuery, FetchReleasesQueryVariables>) {
          return Apollo.useLazyQuery<FetchReleasesQuery, FetchReleasesQueryVariables>(FetchReleasesDocument, baseOptions);
        }
export type FetchReleasesQueryHookResult = ReturnType<typeof useFetchReleasesQuery>;
export type FetchReleasesLazyQueryHookResult = ReturnType<typeof useFetchReleasesLazyQuery>;
export type FetchReleasesQueryResult = Apollo.QueryResult<FetchReleasesQuery, FetchReleasesQueryVariables>;
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
export function useFetchReleasesRecentlyAddedQuery(baseOptions?: Apollo.QueryHookOptions<FetchReleasesRecentlyAddedQuery, FetchReleasesRecentlyAddedQueryVariables>) {
        return Apollo.useQuery<FetchReleasesRecentlyAddedQuery, FetchReleasesRecentlyAddedQueryVariables>(FetchReleasesRecentlyAddedDocument, baseOptions);
      }
export function useFetchReleasesRecentlyAddedLazyQuery(baseOptions?: Apollo.LazyQueryHookOptions<FetchReleasesRecentlyAddedQuery, FetchReleasesRecentlyAddedQueryVariables>) {
          return Apollo.useLazyQuery<FetchReleasesRecentlyAddedQuery, FetchReleasesRecentlyAddedQueryVariables>(FetchReleasesRecentlyAddedDocument, baseOptions);
        }
export type FetchReleasesRecentlyAddedQueryHookResult = ReturnType<typeof useFetchReleasesRecentlyAddedQuery>;
export type FetchReleasesRecentlyAddedLazyQueryHookResult = ReturnType<typeof useFetchReleasesRecentlyAddedLazyQuery>;
export type FetchReleasesRecentlyAddedQueryResult = Apollo.QueryResult<FetchReleasesRecentlyAddedQuery, FetchReleasesRecentlyAddedQueryVariables>;
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
export function useFetchReleaseQuery(baseOptions: Apollo.QueryHookOptions<FetchReleaseQuery, FetchReleaseQueryVariables>) {
        return Apollo.useQuery<FetchReleaseQuery, FetchReleaseQueryVariables>(FetchReleaseDocument, baseOptions);
      }
export function useFetchReleaseLazyQuery(baseOptions?: Apollo.LazyQueryHookOptions<FetchReleaseQuery, FetchReleaseQueryVariables>) {
          return Apollo.useLazyQuery<FetchReleaseQuery, FetchReleaseQueryVariables>(FetchReleaseDocument, baseOptions);
        }
export type FetchReleaseQueryHookResult = ReturnType<typeof useFetchReleaseQuery>;
export type FetchReleaseLazyQueryHookResult = ReturnType<typeof useFetchReleaseLazyQuery>;
export type FetchReleaseQueryResult = Apollo.QueryResult<FetchReleaseQuery, FetchReleaseQueryVariables>;
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
export function useFetchReleaseYearsQuery(baseOptions?: Apollo.QueryHookOptions<FetchReleaseYearsQuery, FetchReleaseYearsQueryVariables>) {
        return Apollo.useQuery<FetchReleaseYearsQuery, FetchReleaseYearsQueryVariables>(FetchReleaseYearsDocument, baseOptions);
      }
export function useFetchReleaseYearsLazyQuery(baseOptions?: Apollo.LazyQueryHookOptions<FetchReleaseYearsQuery, FetchReleaseYearsQueryVariables>) {
          return Apollo.useLazyQuery<FetchReleaseYearsQuery, FetchReleaseYearsQueryVariables>(FetchReleaseYearsDocument, baseOptions);
        }
export type FetchReleaseYearsQueryHookResult = ReturnType<typeof useFetchReleaseYearsQuery>;
export type FetchReleaseYearsLazyQueryHookResult = ReturnType<typeof useFetchReleaseYearsLazyQuery>;
export type FetchReleaseYearsQueryResult = Apollo.QueryResult<FetchReleaseYearsQuery, FetchReleaseYearsQueryVariables>;
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
    ...FullReleaseFields
  }
}
    ${FullReleaseFieldsFragmentDoc}`;
export type UpdateReleaseMutationFn = Apollo.MutationFunction<UpdateReleaseMutation, UpdateReleaseMutationVariables>;

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
export function useUpdateReleaseMutation(baseOptions?: Apollo.MutationHookOptions<UpdateReleaseMutation, UpdateReleaseMutationVariables>) {
        return Apollo.useMutation<UpdateReleaseMutation, UpdateReleaseMutationVariables>(UpdateReleaseDocument, baseOptions);
      }
export type UpdateReleaseMutationHookResult = ReturnType<typeof useUpdateReleaseMutation>;
export type UpdateReleaseMutationResult = Apollo.MutationResult<UpdateReleaseMutation>;
export type UpdateReleaseMutationOptions = Apollo.BaseMutationOptions<UpdateReleaseMutation, UpdateReleaseMutationVariables>;
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
export function useFetchUserQuery(baseOptions?: Apollo.QueryHookOptions<FetchUserQuery, FetchUserQueryVariables>) {
        return Apollo.useQuery<FetchUserQuery, FetchUserQueryVariables>(FetchUserDocument, baseOptions);
      }
export function useFetchUserLazyQuery(baseOptions?: Apollo.LazyQueryHookOptions<FetchUserQuery, FetchUserQueryVariables>) {
          return Apollo.useLazyQuery<FetchUserQuery, FetchUserQueryVariables>(FetchUserDocument, baseOptions);
        }
export type FetchUserQueryHookResult = ReturnType<typeof useFetchUserQuery>;
export type FetchUserLazyQueryHookResult = ReturnType<typeof useFetchUserLazyQuery>;
export type FetchUserQueryResult = Apollo.QueryResult<FetchUserQuery, FetchUserQueryVariables>;
export const UpdateUserDocument = gql`
    mutation UpdateUser($nickname: String) {
  updateUser(nickname: $nickname) {
    ...UserFields
  }
}
    ${UserFieldsFragmentDoc}`;
export type UpdateUserMutationFn = Apollo.MutationFunction<UpdateUserMutation, UpdateUserMutationVariables>;

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
export function useUpdateUserMutation(baseOptions?: Apollo.MutationHookOptions<UpdateUserMutation, UpdateUserMutationVariables>) {
        return Apollo.useMutation<UpdateUserMutation, UpdateUserMutationVariables>(UpdateUserDocument, baseOptions);
      }
export type UpdateUserMutationHookResult = ReturnType<typeof useUpdateUserMutation>;
export type UpdateUserMutationResult = Apollo.MutationResult<UpdateUserMutation>;
export type UpdateUserMutationOptions = Apollo.BaseMutationOptions<UpdateUserMutation, UpdateUserMutationVariables>;
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