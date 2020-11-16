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
	hasCover
`;

export const ARTIST_FIELDS = `
	id
	name
	starred
	numReleases
`;

export const COLLECTION_FIELDS = `
	id
	name
	starred
	type
	numReleases
	lastUpdatedOn
`;

export const TRACK_FIELDS = `
	id
	title
	duration
	trackNumber
	discNumber
`;
