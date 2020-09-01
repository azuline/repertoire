import './index.scss';

import React, { useContext, useMemo, useState } from 'react';

import { Card } from '@blueprintjs/core';
import { CoverArt } from 'components/common/CoverArt';
import { PopoverTrackList } from '../TrackList/PopoverTrackList';
import { ReleaseArtists } from '../Artists';
import { ViewContext } from 'contexts';

export const ArtworkRelease = (release) => {
  const { id, title, artists, collections, tracks, hasImage } = release;

  const [displayTrackList, setDisplayTrackList] = useState(false);
  const { expandTrackLists } = useContext(ViewContext);

  const inInbox = useMemo(() => {
    return collections.some((collection) => collection.id === 1);
  }, [collections]);

  return (
    <PopoverTrackList release={release} tracks={tracks} className="ReleaseWrapper">
      <Card
        className="Release"
        interactive
        onClick={() => expandTrackLists || setDisplayTrackList(!displayTrackList)}
      >
        <CoverArt inInbox={inInbox} releaseId={id} hasImage={hasImage} />
        <div className="ReleaseInfo">
          <div className="Title">
            <h5 className="bp3-heading">{title}</h5>
          </div>
          <ReleaseArtists artists={artists} minimal />
        </div>
      </Card>
    </PopoverTrackList>
  );
};
