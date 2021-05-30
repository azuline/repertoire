import { makeList } from './makeList';

export { ArtistListWithRoles } from './ArtistListWithRoles';

export const ArtistList = makeList('/artists');
export const GenreList = makeList('/genres');
export const LabelList = makeList('/labels');
export const CollageList = makeList('/collages');
