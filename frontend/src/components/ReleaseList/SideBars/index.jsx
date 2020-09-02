import React from 'react';
import { Icon, Card, Button } from '@blueprintjs/core';
import { usePersistentState } from 'hooks';
import './index.scss';
import { ArtistBar } from './ArtistBar';
import { CollectionBar } from './CollectionBar';

export const SideBars = () => {
  const [hideCollection, setHideCollection] = usePersistentState(
    'sidebar--hide-collection',
    true
  );
  const [hideArtist, setHideArtist] = usePersistentState('sidebar--hide-artist', true);

  return (
    <div className="SideBars">
      <CollectionBar hidden={hideCollection} />
      <ArtistBar hidden={hideArtist} />
      <div className="HideBars">
        <div className="Vertical">
          <Card className="HideBar" onClick={() => setHideCollection(!hideCollection)}>
            <Icon icon={hideCollection ? 'chevron-up' : 'chevron-down'} />
            Collections
          </Card>
          <Card className="HideBar" onClick={() => setHideArtist(!hideArtist)}>
            <Icon icon={hideArtist ? 'chevron-up' : 'chevron-down'} />
            Artists
          </Card>
        </div>
      </div>
    </div>
  );
};
