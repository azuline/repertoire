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
