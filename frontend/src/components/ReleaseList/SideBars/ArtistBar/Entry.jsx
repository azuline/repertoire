import React, { useCallback, useContext, useMemo } from 'react';

import { Card } from '@blueprintjs/core';
import { SearchContext } from 'contexts';
import { escapeQuotes } from 'common/queries';

export const Entry = ({ artist, activeArtists }) => {
  const { query, setQuery } = useContext(SearchContext);

  const active = useMemo(() => activeArtists.includes(artist.id), [
    artist,
    activeArtists,
  ]);

  const queryString = useMemo(() => `artist:"${escapeQuotes(artist.name)}"`, [artist]);

  const toggleActive = useCallback(() => {
    if (query.search(queryString) === -1) {
      setQuery(`${query} ${queryString}`);
    } else {
      setQuery(query.replace(queryString, ''));
    }
  }, [query, queryString, setQuery]);

  return (
    <Card className={'Entry' + (active ? ' Active' : '')} onClick={toggleActive}>
      {artist.name}
    </Card>
  );
};
