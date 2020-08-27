import { Card, Icon, Position, Tooltip } from '@blueprintjs/core';
import React, { useContext } from 'react';

import { CollectionTag } from 'components/common/CollectionTag';
import { SearchContext } from 'contexts';
import { escapeQuotes } from 'common/queries';

export const Artist = ({ artist }) => {
  const { favorite, name, numReleases, topGenres } = artist;
  const { runQuery } = useContext(SearchContext);

  const queryArtist = () => runQuery(`artist:"${escapeQuotes(name)}"`);

  return (
    <Card className="Artist" interactive onClick={queryArtist}>
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
