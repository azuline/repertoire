export enum ArtistRole {
  MAIN = 'MAIN',
  FEATURE = 'FEATURE',
  REMIXER = 'REMIXER',
  PRODUCER = 'PRODUCER',
  COMPOSER = 'COMPOSER',
  CONDUCTOR = 'CONDUCTOR',
  DJMIXER = 'DJMIXER',
}

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

export enum CollectionType {
  SYSTEM = 'SYSTEM',
  COLLAGE = 'COLLAGE',
  LABEL = 'LABEL',
  GENRE = 'GENRE',
  RATING = 'RATING',
}

export enum ReleaseSort {
  RECENTLY_ADDED = 'RECENTLY_ADDED',
  TITLE = 'TITLE',
  YEAR = 'YEAR',
  RANDOM = 'RANDOM',
}

export enum ReleaseView {
  ARTWORK = 'ARTWORK',
  ROW = 'ROW',
}

export type ArtistRoleT = keyof typeof ArtistRole;
export type ReleaseTypeT = keyof typeof ReleaseType;
export type CollectionTypeT = keyof typeof CollectionType;
export type ReleaseSortT = keyof typeof ReleaseSort;
