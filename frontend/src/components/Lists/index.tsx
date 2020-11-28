import { makeList } from './makeList';

export { TrackArtistList } from './TrackArtistList';

export const ArtistList = makeList('/artists');
export const GenreList = makeList('/genres');
export const LabelList = makeList('/labels');
export const CollageList = makeList('/collages');
