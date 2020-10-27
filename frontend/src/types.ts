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

  artists?: ArtistT[];
  tracks?: TrackT[];
  genres?: CollectionT[];
  labels?: CollectionT[];
  collages?: CollectionT[];
};

export type ArtistT = {
  id: number;
  name: string;
  favorite: boolean;
  numReleases: number;

  releases?: ReleaseT[];
  topGenres?: TopGenre[];
};

export type CollectionT = {
  id: number;
  name: string;
  favorite: boolean;
  type: string;
  numReleases: number;
  lastUpdatedOn: number;

  releases?: ReleaseT[];
  topGenres?: TopGenre[];
};

export type TrackT = {
  id: number;
  title: string;
  duration: number;
  trackNumber: string;
  discNumber: string;

  release?: ReleaseT;
  artists?: TrackArtist[];
};

export type TrackArtist = {
  role: ArtistRole;
  artist: ArtistT;
};

export type TopGenre = {
  genre: CollectionT;
  numMatches: number;
};

export type ArtistRole =
  | 'MAIN'
  | 'FEATURE'
  | 'REMIXER'
  | 'PRODUCER'
  | 'COMPOSER'
  | 'CONDUCTOR'
  | 'DJMIXER';

export type ReleaseType =
  | 'ALBUM'
  | 'SINGLE'
  | 'EP'
  | 'COMPILATION'
  | 'SOUNDTRACK'
  | 'SPOKENWORD'
  | 'LIVE'
  | 'REMIX'
  | 'DJMIX'
  | 'MIXTAPE'
  | 'OTHER'
  | 'UNKNOWN';

export type CollectionType = 'SYSTEM' | 'COLLAGE' | 'LABEL' | 'GENRE' | 'RATING';

export type ReleaseSort = 'RECENTLY_ADDED' | 'TITLE' | 'YEAR' | 'RANDOM';
