import React, { useContext } from 'react';
import { Tag, Text } from '@blueprintjs/core';
import { collectionQueryFormats, escapeQuotes } from 'common/queries';

import { Link } from 'react-router-dom';
import { SearchContext } from 'contexts';

export const CollectionTag = ({ collection, minimal }) => {
  const { type, name } = collection;
  const { setQuery } = useContext(SearchContext);

  const queryCollection = (event) => {
    setQuery(collectionQueryFormats[type](escapeQuotes(name)));
    event.stopPropagation();
  };

  return (
    <Link to="/" onClick={queryCollection}>
      <Tag className="CollectionTag" minimal={minimal} interactive>
        <Text ellipsize>{name}</Text>
      </Tag>
    </Link>
  );
};
