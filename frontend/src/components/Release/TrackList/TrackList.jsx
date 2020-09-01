import './index.scss';

import React, { useCallback, useContext, useMemo } from 'react';

import { NowPlayingContext } from 'contexts';
import { Card } from '@blueprintjs/core';
import { TrackArtists } from './Artists';
import { secondsToLength } from 'common/tracks';
import { TopToaster } from 'components/Toaster';

export const TrackList = ({ release, tracks }) => {
  const { setPlayQueue, setCurrentQueueIndex } = useContext(NowPlayingContext);

  const enQueue = useCallback(
    (track_id) => {
      const flattenedTracks = Object.values(tracks).reduce(
        (accumulator, disctracks) => [
          ...accumulator,
          ...Object.values(disctracks).map((track) => ({ ...track, release: release })),
        ],
        []
      );
      setPlayQueue(flattenedTracks);
      setCurrentQueueIndex(flattenedTracks.findIndex((track) => track.id === track_id));
      TopToaster.show({ icon: 'music', message: 'Loading track...', timeout: 1000 });
    },
    [release, tracks, setPlayQueue, setCurrentQueueIndex]
  );

  const multiDisc = useMemo(() => Object.keys(tracks).length !== 1, [tracks]);

  return (
    <Card className="TrackList">
      <h2>Tracks</h2>
      {Object.entries(tracks).map(([discno, disctracks]) => {
        return (
          <div key={discno} className="Disc">
            {multiDisc && (
              <div className="DiscNumber">
                <h3>Disc {discno}</h3>
              </div>
            )}
            <div className="TrackListTracks">
              {Object.entries(disctracks).map(([trackno, track]) => {
                return (
                  <Card
                    key={track.id}
                    className="Track"
                    onClick={() => enQueue(track.id)}
                  >
                    <div className="TrackSimpleInfo">
                      <div className="TrackNumber">{trackno}</div>
                      <div className="TrackTitle">{track.title}</div>
                      <div className="TrackLength">
                        {secondsToLength(track.duration)}
                      </div>
                    </div>
                    <TrackArtists artists={track.artists} minimal />
                  </Card>
                );
              })}
            </div>
          </div>
        );
      })}
    </Card>
  );
};
