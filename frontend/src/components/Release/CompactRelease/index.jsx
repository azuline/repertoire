import './index.scss';

import { Card, Divider, Icon, Position, Tooltip } from '@blueprintjs/core';
import React, { useContext, useMemo, useState } from 'react';

import { CoverArt } from '../CoverArt';
import { FlatTrackList } from '../TrackList/FlatTrackList';
import { ReleaseArtists } from '../Artists';
import { ReleaseCollections } from '../Collections';
import { ViewContext } from 'contexts';

const genreAndLabelCollectionTypes = [3, 4];

export const CompactRelease = ({
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

  // In the compact release, only display genres and labels.
  const filteredCollections = collections.filter(({ type }) => {
    return genreAndLabelCollectionTypes.includes(type);
  });

  return (
    <div className="ReleaseWrapper">
      <Card
        className="Release"
        interactive
        onClick={() => expandTrackLists || setDisplayTrackList(!displayTrackList)}
      >
        <div className="ReleaseInfo">
          <div className="SimpleData">
            <div className="Title">
              {inInbox && (
                <Tooltip content="In Inbox!" position={Position.TOP}>
                  <Icon
                    className="InInboxIcon"
                    icon="inbox-update"
                    intent="danger"
                    htmlTitle="In Inbox"
                  />
                </Tooltip>
              )}
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
          <div className="ArtAndTags">
            <CoverArt />
            <div className="Tags">
              <ReleaseArtists artists={artists} minimal />
              <ReleaseCollections collections={filteredCollections} />
            </div>
          </div>
        </div>
      </Card>
      {(displayTrackList || expandTrackLists) && <FlatTrackList tracks={tracks} />}
    </div>
  );
};
