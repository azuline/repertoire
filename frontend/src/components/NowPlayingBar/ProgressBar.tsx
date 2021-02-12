import * as React from 'react';
import ReactSlider from 'react-slider';
import { TrackT } from '~/types';

export const ProgressBar: React.FC<{
  curTime: number;
  curTrack: TrackT | null;
  seek: (arg0: number) => void;
}> = ({ curTime, curTrack, seek }) => {
  const onSliderChange = (value: number | number[] | undefined | null): void =>
    seek(value as number);

  return (
    <div className="absolute left-0 w-full h-1 -top-1">
      <ReactSlider
        className="slider playbar-slider"
        disabled={!curTrack}
        max={curTrack ? curTrack.duration : undefined}
        thumbClassName={curTrack ? undefined : 'hidden'}
        value={curTrack ? curTime : 0}
        onAfterChange={onSliderChange}
      />
    </div>
  );
};
