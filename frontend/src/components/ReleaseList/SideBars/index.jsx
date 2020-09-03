import React, { useContext } from 'react';
import { Icon, Card } from '@blueprintjs/core';
import { SideBarContext } from 'contexts';
import './index.scss';
import { ArtistBar } from './ArtistBar';
import { CollectionBar } from './CollectionBar';

export const SideBars = () => {
  const { hideCollection, setHideCollection, hideArtist, setHideArtist } = useContext(
    SideBarContext
  );

  return (
    <>
      <div className="SideBars">
        <CollectionBar hidden={hideCollection} />
        <ArtistBar hidden={hideArtist} />
      </div>
      <div className="HideBars">
        <div className="Vertical">
          <Card
            className="HideBar HideCollections"
            onClick={() => setHideCollection(!hideCollection)}
          >
            <Icon icon={hideCollection ? 'chevron-up' : 'chevron-down'} />
            <div className="HideName">
              <span>Collections</span>
            </div>
          </Card>
          <Card
            className="HideBar HideArtists"
            onClick={() => setHideArtist(!hideArtist)}
          >
            <Icon icon={hideArtist ? 'chevron-up' : 'chevron-down'} />
            <div className="HideName">
              <span>Artists</span>
            </div>
          </Card>
        </div>
      </div>
    </>
  );
};
