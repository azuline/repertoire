import clsx from 'clsx';
import * as React from 'react';
import { TrackT } from 'src/types';
import { secondsToLength } from 'src/util';

export const Progress: React.FC<{
  className?: string;
  curTrack: TrackT | null;
  curTime: number;
}> = ({ className, curTrack, curTime }) => (
  <div className={clsx(className, 'text-center w-28')}>
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
