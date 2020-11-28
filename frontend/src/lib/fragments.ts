/**
 * This module contains GraphQL query fragments.
 *
 * Currently, there are only fragments for the fields of each type.
 */

export const USER_FIELDS = `
  id
  nickname
`;

export const RELEASE_FIELDS = `
  id
  title
  releaseType
  addedOn
  inInbox
  inFavorites
  releaseYear
  releaseDate
  numTracks
  runtime
  imageId
`;

export const ARTIST_FIELDS = `
  id
  name
  starred
  numReleases
  imageId
`;

export const COLLECTION_FIELDS = `
  id
  name
  starred
  type
  numReleases
  lastUpdatedOn
  imageId
`;

export const TRACK_FIELDS = `
  id
  title
  duration
  trackNumber
  discNumber
`;

export const FULL_RELEASE_FIELDS = `
  ${RELEASE_FIELDS}
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
    ${TRACK_FIELDS}
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
