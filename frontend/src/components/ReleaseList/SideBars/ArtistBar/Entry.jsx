import React, { useCallback, useMemo, useContext } from 'react';
import { escapeQuotes } from 'common/queries';
import { SearchContext } from 'contexts';
import { Card } from '@blueprintjs/core';

export const Entry = ({ artist, activeArtists }) => {
  const { query, setActiveQuery } = useContext(SearchContext);

  const active = useMemo(() => activeArtists.includes(artist.id), [
    artist,
    activeArtists,
  ]);

  const queryString = useMemo(() => `artist:"${escapeQuotes(artist.name)}"`, [artist]);

  const toggleActive = useCallback(() => {
    if (query.search(queryString) === -1) {
      setActiveQuery(`${query} ${queryString}`);
    } else {
      setActiveQuery(query.replace(queryString, ''));
    }
  }, [query, queryString, setActiveQuery]);

  return (
    <Card className={'Entry' + (active ? ' Active' : '')} onClick={toggleActive}>
      {artist.name}
    </Card>
  );
};
