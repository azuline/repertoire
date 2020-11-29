/**
 * In reality, a lot of these object attributes are "optional", in that we can
 * have objects of the type without them. However, if we mark them as optional,
 * then we end up with a lot of type casting to not-undefined in our code.
 *
 * Furthermore, this all describes data received from the backend during
 * runtime, and I'm too lazy to explicitly type every detail from the output of
 * the GraphQL queries.
 *
 * Rather than deal with that, I think it better to just eat the cost of less
 * type safety.
 */

import { ArtistRole } from './enums';

export type UserT = { id: number; nickname: string };

export type ReleaseT = {
  id: number;
  title: string;
  releaseType: string;
  addedOn: number;
  inInbox: boolean;
  inFavorites: boolean;
  releaseYear: number;
  releaseDate: string | null;
  rating: number | null;
  numTracks: number;
  imageId: number | null;
  runtime: number;

  artists: ArtistT[];
  tracks: TrackT[];
  genres: CollectionT[];
  labels: CollectionT[];
  collages: CollectionT[];
};

export type ElementT = {
  id: number;
  name: string;
};

export type ArtistT = {
  id: number;
  name: string;
  starred: boolean;
  numReleases: number;
  imageId: number | null;

  releases: ReleaseT[];
  topGenres: TopGenreT[];
};

export type CollectionT = {
  id: number;
  name: string;
  starred: boolean;
  type: string;
  numReleases: number;
  lastUpdatedOn: number;
  imageId: number | null;

  releases: ReleaseT[];
  topGenres: TopGenreT[];
};

export type TrackT = {
  id: number;
  title: string;
  duration: number;
  trackNumber: string;
  discNumber: string;

  release: ReleaseT;
  artists: TrackArtistT[];
};

export type TrackArtistT = {
  role: ArtistRole;
  artist: ArtistT;
};

export type TopGenreT = {
  genre: CollectionT;
  numMatches: number;
};
