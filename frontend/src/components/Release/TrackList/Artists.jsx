import React, { useContext, useMemo } from 'react';

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
  const { runQuery } = useContext(SearchContext);

  // Return a map of artist roles to the artists in that role, filtering out
  // roles without any artists in them.
  const artistsByRoles = useMemo(() => {
    const roles = { 1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: [] };
    artists.map((artist) => roles[artist.role].push(artist));

    return Object.entries(roles).filter(([role, results]) => results.length !== 0);
  }, [artists]);

  // Very annoyed by React, this is a slight hack. We construct a list of divs
  // for the artist list, consisting of artists and divider words. We want this
  // to be flat, which doesn't work out with the typical map inside component
  // practice.
  const childDivList = useMemo(() => {
    const queryArtist = (artist) => (event) => {
      runQuery(`artist:"${escapeQuotes(artist)}"`);
      event.stopPropagation();
    };

    const childrenList = artistsByRoles.map(([role, artists]) => {
      const dividerDivs = dividerWords.hasOwnProperty(role)
        ? [<span className="DividerWord">{dividerWords[role]}</span>]
        : [];

      const artistDivs = artists.map((artist) => (
        <Link key={artist.id} to="/" onClick={queryArtist(artist.name)}>
          <Tag minimal={minimal} interactive className="TrackArtist">
            {artist.name}
          </Tag>
        </Link>
      ));

      return [...dividerDivs, ...artistDivs];
    });

    // Flatten the accumulated list of lists of divs.
    return [].concat.apply([], childrenList);
  }, [artistsByRoles, minimal, runQuery]);

  return <div className="TrackArtists">{childDivList.map((div) => div)}</div>;
};
