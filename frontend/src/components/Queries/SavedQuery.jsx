import { Card, Tag } from '@blueprintjs/core';
import React, { useContext } from 'react';

import { SearchContext } from 'contexts';
import { useHistory } from 'react-router-dom';

export const SavedQuery = (props) => {
  const { name, id, query } = props.query;
  const { setQuery } = useContext(SearchContext);
  const history = useHistory();

  const restoreQuery = () => {
    setQuery(query);
    history.push('/');
  };

  return (
    <Card className="SavedQuery" interactive onClick={restoreQuery} title={query}>
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
