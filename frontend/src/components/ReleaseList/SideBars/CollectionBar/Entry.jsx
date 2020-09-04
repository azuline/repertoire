import React, { useCallback, useContext, useMemo } from 'react';
import { collectionQueryFormats, escapeQuotes } from 'common/queries';

import { Card } from '@blueprintjs/core';
import { SearchContext } from 'contexts';

export const Entry = ({ collection, activeCollections }) => {
  const { query, setQuery } = useContext(SearchContext);

  const active = useMemo(() => activeCollections.includes(collection.id), [
    collection,
    activeCollections,
  ]);

  const queryString = useMemo(
    () => collectionQueryFormats[collection.type](escapeQuotes(collection.name)),
    [collection]
  );

  const toggleActive = useCallback(() => {
    if (query.search(queryString) === -1) {
      setQuery(`${query} ${queryString}`);
    } else {
      setQuery(query.replace(queryString, ''));
    }
  }, [query, queryString, setQuery]);

  return (
    <Card className={'Entry' + (active ? ' Active' : '')} onClick={toggleActive}>
      {collection.name}
    </Card>
  );
};
