import React, { useCallback, useContext } from 'react';
import { Tag, Text } from '@blueprintjs/core';
import { collectionQueryFormats, escapeQuotes } from 'common/queries';

import { SearchContext } from 'contexts';

export const CollectionTag = ({ collection, minimal }) => {
  const { type, name } = collection;
  const { setQuery } = useContext(SearchContext);

  const queryCollection = useCallback(
    (event) => {
      setQuery(collectionQueryFormats[type](escapeQuotes(name)));
      event.stopPropagation();
    },
    [setQuery, name, type]
  );

  return (
    <Tag
      onClick={queryCollection}
      className="CollectionTag"
      minimal={minimal}
      interactive
    >
      <Text ellipsize>{name}</Text>
    </Tag>
  );
};
