import { Card, Tag } from '@blueprintjs/core';
import React, { useContext } from 'react';

import { SearchContext } from 'contexts';

export const SavedQuery = (props) => {
  const { name, id, query } = props.query;
  const { runQuery } = useContext(SearchContext);

  return (
    <Card
      className="SavedQuery"
      interactive
      onClick={() => runQuery(query)}
      title={query}
    >
      <div className="MetaInfo">
        <div className="Id">{id}</div>
        <div className="Name">{name}</div>
      </div>
      <Tag className="Query" large minimal>
        {query}
      </Tag>
    </Card>
  );
};
