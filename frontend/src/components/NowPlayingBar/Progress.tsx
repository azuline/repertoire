import * as React from 'react';

import { ITrack } from '~/graphql';
import { secondsToLength } from '~/util';

type IProgress = React.FC<{
  curTrack: ITrack | null;
  curTime: number;
}>;

export const Progress: IProgress = ({ curTrack, curTime }) => (
  <div tw="flex-none hidden ml-4 text-center w-24 md:block">
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
