import * as React from 'react';
import tw, { styled } from 'twin.macro';

import { Slider } from '~/components';
import { ITrack } from '~/graphql';

type IProgressBar = React.FC<{
  curTime: number;
  curTrack: ITrack | null;
  seek: (arg0: number) => void;
}>;

export const ProgressBar: IProgressBar = ({ curTime, curTrack, seek }) => {
  const onSliderChange = (value: number | readonly number[]): void =>
    seek(value as number);

  return (
    <ProgressSlider>
      <Slider
        disabled={!curTrack}
        max={curTrack ? curTrack.duration : undefined}
        thumbClassName={curTrack ? undefined : 'hidden'}
        value={curTrack ? curTime : 0}
        onAfterChange={onSliderChange}
      />
    </ProgressSlider>
  );
};

const ProgressSlider = styled.div`
  ${tw`absolute left-0 w-full h-1 -top-1`}

  .slider .track {
    ${tw`h-1`}
  }
`;
