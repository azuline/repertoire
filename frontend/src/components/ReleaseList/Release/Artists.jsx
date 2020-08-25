import React, { useContext } from 'react';

import { Link } from 'react-router-dom';
import { SearchContext } from 'components/Contexts';
import { Tag } from '@blueprintjs/core';
import { escapeQuotes } from 'common/queries';

export const ReleaseArtists = ({ artists, minimal, large }) => {
  const { setQuery } = useContext(SearchContext);

  const queryArtist = (artist) => (event) => {
    setQuery(`artist:"${escapeQuotes(artist)}"`);
    event.stopPropagation();
  };

  return (
    <div className="ReleaseArtists">
      {artists.map((artist) => {
        return (
          <Link key={artist.id} to="/" onClick={queryArtist(artist.name)}>
            <Tag className="ReleaseArtist" interactive large={large} minimal={minimal}>
              {artist.name}
            </Tag>
          </Link>
        );
      })}
    </div>
  );
};
