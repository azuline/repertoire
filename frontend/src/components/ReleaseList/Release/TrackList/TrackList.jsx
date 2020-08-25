import './index.scss';

import React, { useMemo } from 'react';

import { Card } from '@blueprintjs/core';
import { TrackArtists } from './Artists';

const secondsToLength = (totalSeconds) => {
  const minutes = Math.floor(totalSeconds / 60);
  const seconds = totalSeconds % 60;
  return `${minutes}:${seconds}`;
};

export const TrackList = ({ tracks }) => {
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
            <div className="Tracks">
              {Object.entries(disctracks).map(([trackno, track]) => {
                return (
                  <Card key={trackno} className="Track" interactive>
                    <div className="TrackSimpleInfo">
                      <div className="TrackTitle">{track.title}</div>
                      <div className="TrackLength">{secondsToLength(track.length)}</div>
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
