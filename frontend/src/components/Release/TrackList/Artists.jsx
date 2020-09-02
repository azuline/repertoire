import React, { Fragment, useCallback, useContext, useMemo } from 'react';

import { Link } from 'react-router-dom';
import { SearchContext } from 'contexts';
import { Tag } from '@blueprintjs/core';
import { escapeQuotes } from 'common/queries';

const dividerWordsRaw = {
  2: 'feat.',
  3: 'remixed by',
  4: 'produced by',
  7: 'mixed by',
};

// Role rankings for sorting their order of apperance.
const roleRankings = ['6', '5', '7', '1', '4', '2', '3'];

const sortRoles = ([a], [b]) => roleRankings.indexOf(a) - roleRankings.indexOf(b);

export const TrackArtists = ({ artists, minimal }) => {
  const { setActiveQuery } = useContext(SearchContext);

  // Return a map of artist roles to the artists in that role, filtering out
  // roles without any artists in them.
  const artistsByRoles = useMemo(() => {
    const roles = artists.reduce((accumulator, artist) => {
      accumulator[artist.role] = accumulator[artist.role] ?? [];
      accumulator[artist.role].push(artist);
      return accumulator;
    }, {});

    const entries = Object.entries(roles);
    entries.sort(sortRoles);
    return entries;
  }, [artists]);

  // Determine the final list of divider words.
  // If we have a composer or a conductor, switch to "classical mode" and turn
  // main artists into performers.
  const dividerWords = useMemo(() => {
    if (artistsByRoles.some(([role]) => role === '5' || role === '6')) {
      return { 1: 'performed by', ...dividerWordsRaw };
    }
    return dividerWordsRaw;
  }, [artistsByRoles]);

  console.log(artistsByRoles);

  const queryArtist = useCallback(
    (artist) => (event) => {
      setActiveQuery(`artist:"${escapeQuotes(artist)}"`);
      event.stopPropagation();
    },
    [setActiveQuery]
  );

  return (
    <div className="TrackArtists">
      {artistsByRoles.map(([role, artists]) => (
        <Fragment key={role}>
          {role in dividerWords && (
            <span className="DividerWord">{dividerWords[role]}</span>
          )}
          {artists.map((artist) => (
            <Link key={artist.id} to="/" onClick={queryArtist(artist.name)}>
              <Tag minimal={minimal} interactive className="TrackArtist">
                {artist.name}
              </Tag>
            </Link>
          ))}
        </Fragment>
      ))}
    </div>
  );
};
