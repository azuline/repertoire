import * as React from 'react';
import { TrackT } from '~/types';
import { secondsToLength } from '~/util';

export const Progress: React.FC<{
  curTrack: TrackT | null;
  curTime: number;
}> = ({ curTrack, curTime }) => (
  <div className="flex-none hidden ml-4 text-center w-24 md:block">
    {curTrack ? (
      <>
        {secondsToLength(curTime)}
        {' / '}
        {secondsToLength(curTrack.duration)}
      </>
    ) : (
      <span>-:-- / -:--</span>
    )}
  </div>
);
