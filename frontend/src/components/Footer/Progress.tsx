import clsx from 'clsx';
import * as React from 'react';
import { TrackT } from 'src/types';
import { secondsToLength } from 'src/util';

export const Progress: React.FC<{
  className?: string;
  curTrack: TrackT | null;
  curTime: number;
}> = ({ className, curTrack, curTime }) => (
  <div className={clsx(className, 'w-28 text-center')}>
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
