import React, { useCallback, useContext } from 'react';

import { SearchContext } from 'contexts';
import { Tag } from '@blueprintjs/core';
import { escapeQuotes } from 'common/queries';

export const ReleaseArtists = ({ artists, minimal, large }) => {
  const { setQuery } = useContext(SearchContext);

  const queryArtist = useCallback(
    (artist) => (event) => {
      setQuery(`artist:"${escapeQuotes(artist)}"`);
      event.stopPropagation();
    },
    [setQuery]
  );

  return (
    <div className="ReleaseArtists">
      {artists.map((artist) => {
        return (
          <Tag
            key={artist.id}
            className="ReleaseArtist"
            onClick={queryArtist(artist.name)}
            interactive
            large={large}
            minimal={minimal}
          >
            {artist.name}
          </Tag>
        );
      })}
    </div>
  );
};
