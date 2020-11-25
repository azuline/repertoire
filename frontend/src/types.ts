export type SetBoolean = (arg0: boolean | ((arg0: boolean) => boolean)) => void;
export type SetNumber = (arg0: number | ((arg0: number) => number)) => void;

export class RequestError<T> extends Error {
  errors: T[];

  constructor(message = 'uwu request error', errors: T[] = []) {
    super(message);
    this.errors = errors;
  }
}

export type GraphQLError = {
  type: string;
  message: string;
  locations: { line: number; column: number }[];
  path: string[];
};

export type UserT = { id: number; username: string };

export type ReleaseT = {
  id: number;
  title: string;
  releaseType: string;
  addedOn: number;
  inInbox: boolean;
  releaseYear: number;
  numTracks: number;
  releaseDate: string;
  hasCover: boolean;
  runtime: number;

  artists?: ArtistT[];
  tracks?: TrackT[];
  genres?: CollectionT[];
  labels?: CollectionT[];
  collages?: CollectionT[];
};

export type ArtistT = {
  id: number;
  name: string;
  starred: boolean;
  numReleases: number;

  releases?: ReleaseT[];
  topGenres?: TopGenreT[];
};

export type CollectionT = {
  id: number;
  name: string;
  starred: boolean;
  type: string;
  numReleases: number;
  lastUpdatedOn: number;

  releases?: ReleaseT[];
  topGenres?: TopGenreT[];
};

export type TrackT = {
  id: number;
  title: string;
  duration: number;
  trackNumber: string;
  discNumber: string;

  release?: ReleaseT;
  artists?: TrackArtistT[];
};

export type TrackArtistT = {
  role: ArtistRole;
  artist: ArtistT;
};

export type TopGenreT = {
  genre: CollectionT;
  numMatches: number;
};

export enum ArtistRole {
  MAIN = 'MAIN',
  FEATURE = 'FEATURE',
  REMIXER = 'REMIXER',
  PRODUCER = 'PRODUCER',
  COMPOSER = 'COMPOSER',
  CONDUCTOR = 'CONDUCTOR',
  DJMIXER = 'DJMIXER',
}

export type ArtistRoleT = keyof typeof ArtistRole;

export enum ReleaseType {
  ALBUM = 'ALBUM',
  SINGLE = 'SINGLE',
  EP = 'EP',
  COMPILATION = 'COMPILATION',
  SOUNDTRACK = 'SOUNDTRACK',
  SPOKENWORD = 'SPOKENWORD',
  LIVE = 'LIVE',
  REMIX = 'REMIX',
  DJMIX = 'DJMIX',
  MIXTAPE = 'MIXTAPE',
  OTHER = 'OTHER',
  UNKNOWN = 'UNKNOWN',
}

export type ReleaseTypeT = keyof typeof ReleaseType;

export enum CollectionType {
  SYSTEM = 'SYSTEM',
  COLLAGE = 'COLLAGE',
  LABEL = 'LABEL',
  GENRE = 'GENRE',
  RATING = 'RATING',
}

export type CollectionTypeT = keyof typeof CollectionType;

export enum ReleaseSort {
  RECENTLY_ADDED = 'RECENTLY_ADDED',
  TITLE = 'TITLE',
  YEAR = 'YEAR',
  RANDOM = 'RANDOM',
}

export type ReleaseSortT = keyof typeof ReleaseSort;

export enum ReleaseView {
  ARTWORK = 'ARTWORK',
  ROW = 'ROW',
}
