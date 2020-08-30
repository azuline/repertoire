import { Card, Icon, Position, Tag, Tooltip } from '@blueprintjs/core';
import React, { useCallback, useContext } from 'react';
import { collectionQueryFormats, escapeQuotes } from 'common/queries';

import { CollectionTag } from 'components/common/CollectionTag';
import { SearchContext } from 'contexts';
import { collectionTypeIdsToNames } from 'common/collections';

export const Collection = ({ collection }) => {
  const { favorite, name, numReleases, topGenres, type } = collection;
  const { setActiveQuery } = useContext(SearchContext);

  const queryCollection = useCallback(() => {
    setActiveQuery(collectionQueryFormats[type](escapeQuotes(name)));
  }, [setActiveQuery, type, name]);

  return (
    <Card className="Collection" interactive onClick={queryCollection}>
      <div className="TypeAndName">
        <div className="Type">
          <Tag minimal large>
            {collectionTypeIdsToNames[type]}
          </Tag>
        </div>
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
      </div>
      <div className="GenresAndNumReleases">
        <div className="TopGenres">
          {topGenres.map((genre) => (
            <CollectionTag key={genre.id} collection={{ ...genre, type: 4 }} />
          ))}
        </div>
        <div className="NumReleases">
          {numReleases} <Icon className="MusicIcon" icon="music" />
        </div>
      </div>
    </Card>
  );
};
