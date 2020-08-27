import React, { useContext } from 'react';

import { SearchContext } from 'contexts';
import { Tag } from '@blueprintjs/core';
import { escapeQuotes } from 'common/queries';

export const ReleaseArtists = ({ artists, minimal, large }) => {
  const { runQuery } = useContext(SearchContext);

  const queryArtist = (artist) => (event) => {
    runQuery(`artist:"${escapeQuotes(artist)}"`);
    event.stopPropagation();
  };

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
