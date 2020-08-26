import './index.scss';

import { Card, Divider } from '@blueprintjs/core';
import React, { useContext, useMemo, useState } from 'react';

import { CoverArt } from '../CoverArt';
import { FlatTrackList } from '../TrackList/FlatTrackList';
import { ReleaseArtists } from '../Artists';
import { ReleaseCollections } from '../Collections';
import { ViewContext } from 'contexts';

export const DetailedRelease = ({
  title,
  year,
  releaseType,
  artists,
  collections,
  tracks,
}) => {
  const [displayTrackList, setDisplayTrackList] = useState(false);
  const { expandTrackLists } = useContext(ViewContext);

  const inInbox = useMemo(() => {
    return collections.some((collection) => collection.id === 1);
  }, [collections]);

  return (
    <div className="ReleaseWrapper">
      <Card
        className="Release"
        interactive
        onClick={() => expandTrackLists || setDisplayTrackList(!displayTrackList)}
      >
        <div className="ReleaseInfo">
          <CoverArt inInbox={inInbox} />
          <div className="Metadata">
            <div className="SimpleData">
              <div className="Title">
                <h4 className="bp3-heading">{title}</h4>
              </div>
              <div className="Classifiers">
                <div className="Year">
                  <h5 className="bp3-heading">{year}</h5>
                </div>
                <Divider />
                <div className="Type">
                  <h5 className="bp3-heading">{releaseType}</h5>
                </div>
              </div>
            </div>
            <ReleaseArtists artists={artists} large minimal />
          </div>
        </div>
        <ReleaseCollections collections={collections} />
      </Card>
      {(displayTrackList || expandTrackLists) && <FlatTrackList tracks={tracks} />}
    </div>
  );
};
