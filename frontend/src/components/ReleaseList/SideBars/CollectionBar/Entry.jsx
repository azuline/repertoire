import React, { useCallback, useMemo, useContext } from 'react';
import { collectionQueryFormats, escapeQuotes } from 'common/queries';
import { SearchContext } from 'contexts';
import { Card } from '@blueprintjs/core';

export const Entry = ({ collection, activeCollections }) => {
  const { query, setActiveQuery } = useContext(SearchContext);

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
      setActiveQuery(`${query} ${queryString}`);
    } else {
      setActiveQuery(query.replace(queryString, ''));
    }
  }, [query, queryString, setActiveQuery]);

  return (
    <Card className={'Entry' + (active ? ' Active' : '')} onClick={toggleActive}>
      {collection.name}
    </Card>
  );
};
