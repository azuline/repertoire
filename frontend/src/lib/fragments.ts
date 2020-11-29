/**
 * This module contains GraphQL query fragments.
 *
 * Currently, there are only fragments for the fields of each type.
 */

import { gql } from '@apollo/client';

export const USER_FIELDS = gql`
  fragment UserFields on User {
    id
    nickname
  }
`;

export const RELEASE_FIELDS = gql`
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

export const ARTIST_FIELDS = gql`
  fragment ArtistFields on Artist {
    id
    name
    starred
    numReleases
    imageId
  }
`;

export const COLLECTION_FIELDS = gql`
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

export const TRACK_FIELDS = gql`
  fragment TrackFields on Track {
    id
    title
    duration
    trackNumber
    discNumber
  }
`;

export const FULL_RELEASE_FIELDS = gql`
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
  ${RELEASE_FIELDS}
  ${TRACK_FIELDS}
`;
