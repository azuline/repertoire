import * as React from 'react';

import { Link } from '~/components/common';
import { ArtistT, TrackArtistT } from '~/types';

type ListT = React.FC<{
  artists?: TrackArtistT[];
  className?: string;
  elementClassName?: string;
  delimiter?: string;
  link?: boolean;
}>;

type RolesArtistsMap = { [k in string]: ArtistT[] };
type RolesArtistsMapEntries = [string, ArtistT[]][];
type DividerWords = { [k in string]: string };

// Role rankings for sorting their order of apperance.
const ROLE_RANKINGS: string[] = [
  'CONDUCTOR',
  'COMPOSER',
  'DJMIXER',
  'MAIN',
  'PRODUCER',
  'FEATURE',
  'REMIXER',
];

const DIVIDER_WORDS_RAW: { [k in string]: string } = {
  DJMIXER: ' mixed by ',
  FEATURE: ' feat. ',
  PRODUCER: ' produced by ',
  REMIXER: ' remixed by ',
};

export const TrackArtistList: ListT = ({
  artists,
  className,
  elementClassName,
  delimiter = ', ',
  link = false,
}) => {
  const rolesToArtists = React.useMemo(() => mapRolesToArtists(artists), [artists]);
  const dividerWords = React.useMemo(() => determineDividerWords(rolesToArtists), [rolesToArtists]);

  if (!artists || artists.length === 0) return <div> </div>;

  return (
    <div className={className}>
      {rolesToArtists.map(([role, arts], i) => (
        <React.Fragment key={role}>
          {(i > 0 && dividerWords[role]) ?? delimiter}
          {arts.map((art, j) => (
            <React.Fragment key={j}>
              {j > 0 && delimiter}
              {link ? (
                <Link className={elementClassName} href={`artists/${art.id}`}>
                  {art.name}
                </Link>
              ) : (
                <span className={elementClassName}>{art.name}</span>
              )}
            </React.Fragment>
          ))}
        </React.Fragment>
      ))}
    </div>
  );
};

export const mapRolesToArtists = (artists?: TrackArtistT[]): RolesArtistsMapEntries => {
  if (!artists) return [];

  // Get a map of artist roles to the artists in that role, filtering out
  // roles without any artists in them.
  const rolesToArtists = Object.entries(
    artists.reduce<RolesArtistsMap>((accumulator, artist) => {
      const { role } = artist;

      accumulator[role] = accumulator[role] ?? [];
      accumulator[role].push(artist.artist);

      return accumulator;
    }, {}),
  );

  rolesToArtists.sort(sortRoles);

  return rolesToArtists;
};

const sortRoles = ([a]: [string, ArtistT[]], [b]: [string, ArtistT[]]): number =>
  ROLE_RANKINGS.indexOf(a) - ROLE_RANKINGS.indexOf(b);

// Determine the final list of divider words.
// If we have a composer or a conductor, switch to "classical mode" and turn
// main artists into performers.
const determineDividerWords = (rolesToArtists: RolesArtistsMapEntries): DividerWords =>
  rolesToArtists.some(([role]) => role === 'PRODUCER' || role === 'FEATURE')
    ? { MAIN: ' performed by ', ...DIVIDER_WORDS_RAW }
    : DIVIDER_WORDS_RAW;
