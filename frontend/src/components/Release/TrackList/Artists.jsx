import React, { Fragment, useCallback, useContext, useMemo } from 'react';

import { Link } from 'react-router-dom';
import { SearchContext } from 'contexts';
import { Tag } from '@blueprintjs/core';
import { escapeQuotes } from 'common/queries';

const dividerWords = {
  2: 'feat.',
  3: 'remixed by',
  4: 'produced by',
  7: 'mixed by',
};

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

    return Object.entries(roles);
  }, [artists]);

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
