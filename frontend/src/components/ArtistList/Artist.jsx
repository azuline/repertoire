import { Card, Icon, Position, Tooltip } from '@blueprintjs/core';
import React, { useContext } from 'react';

import { CollectionTag } from 'components/common/CollectionTag';
import { SearchContext } from 'components/Contexts';
import { escapeQuotes } from 'common/queries';
import { useHistory } from 'react-router-dom';

export const Artist = ({ artist }) => {
  const { favorite, name, numReleases, topGenres } = artist;
  const { setQuery } = useContext(SearchContext);
  const history = useHistory();

  const queryArtist = () => {
    setQuery(`artist:"${escapeQuotes(name)}"`);
    history.push('/');
  };

  return (
    <Card className="Artist" interactive onClick={queryArtist}>
      <div className="Name">
        <span className="NameText">{name}</span>
        {favorite && (
          <div class="Favorite">
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
