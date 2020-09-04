import { Card, Icon, Position, Tag, Tooltip } from '@blueprintjs/core';
import React, { useContext } from 'react';

import { SearchContext } from 'contexts';

export const Query = ({ query: { query, id, name, favorite } }) => {
  const { setQuery } = useContext(SearchContext);

  return (
    <Card
      className="SavedQuery"
      interactive
      onClick={() => setQuery(query)}
      title={query}
    >
      <div className="Name">
        <span className="NameText">{name}</span>
        {favorite && (
          <div className="Favorite">
            <Tooltip content="Favorite!" position={Position.TOP}>
              <Icon className="FavoriteIcon" icon="heart" intent="primary" />
            </Tooltip>
          </div>
        )}
      </div>
      <Tag className="Query" large minimal>
        {query}
      </Tag>
    </Card>
  );
};
