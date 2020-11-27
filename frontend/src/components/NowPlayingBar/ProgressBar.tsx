import * as React from 'react';
import ReactSlider from 'react-slider';
import { SetValue, TrackT } from 'src/types';

export const ProgressBar: React.FC<{
  curTime: number;
  curTrack: TrackT | null;
  seek: SetValue<number>;
}> = ({ curTime, curTrack, seek }) => {
  const onSliderChange = React.useCallback((value) => seek(value), [seek]);

  return (
    <div className="absolute left-0 w-full h-1 -top-1">
      <ReactSlider
        className="slider playbar-slider"
        value={curTime}
        onAfterChange={onSliderChange}
        max={curTrack ? curTrack.duration : undefined}
        thumbClassName={curTrack ? undefined : 'hidden'}
        disabled={!curTrack}
      />
    </div>
  );
};
