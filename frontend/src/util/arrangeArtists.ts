import { ArtistT, TrackArtistT } from 'src/types';

type ElementT = { id: number; name: string };

const dividerWordsRaw: { [k in string]: string } = {
  FEATURE: 'feat.',
  REMIXER: 'remixed by',
  PRODUCER: 'produced by',
  DJMIXER: 'mixed by',
};

// Role rankings for sorting their order of apperance.
const roleRankings: string[] = [
  'CONDUCTOR',
  'COMPOSER',
  'DJMIXER',
  'MAIN',
  'PRODUCER',
  'FEATURE',
  'REMIXER',
];

const sortRoles = ([a]: [string, ArtistT[]], [b]: [string, ArtistT[]]): number =>
  roleRankings.indexOf(a) - roleRankings.indexOf(b);

export const arrangeArtists = (artists: TrackArtistT[]): ElementT[] => {
  // Get a map of artist roles to the artists in that role, filtering out
  // roles without any artists in them.
  const artistRoles = Object.entries(
    artists.reduce<{ [k in string]: ArtistT[] }>((accumulator, artist) => {
      const { role } = artist;

      accumulator[role] = accumulator[role] ?? [];
      accumulator[role].push(artist.artist);

      return accumulator;
    }, {}),
  );

  artistRoles.sort(sortRoles);

  // Determine the final list of divider words.
  // If we have a composer or a conductor, switch to "classical mode" and turn
  // main artists into performers.
  const dividerWords = artistRoles.some(
    ([role]: [string, ArtistT[]]) => role === 'PRODUCER' || role === 'FEATURE',
  )
    ? { MAIN: 'performed by', ...dividerWordsRaw }
    : dividerWordsRaw;

  return artistRoles.reduce<ElementT[]>((acc, [role, innerArtists]) => {
    if (dividerWords[role]) {
      acc.push({ id: 0, name: dividerWords[role] });
    }

    acc.push(...innerArtists);

    return acc;
  }, []);
};
