import React, { useContext } from 'react';
import { Tag, Text } from '@blueprintjs/core';
import { collectionQueryFormats, escapeQuotes } from 'common/queries';

import { SearchContext } from 'contexts';

export const CollectionTag = ({ collection, minimal }) => {
  const { type, name } = collection;
  const { runQuery } = useContext(SearchContext);

  const queryCollection = (event) => {
    runQuery(collectionQueryFormats[type](escapeQuotes(name)));
    event.stopPropagation();
  };

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
