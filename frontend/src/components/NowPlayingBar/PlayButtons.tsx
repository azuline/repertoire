import * as React from 'react';
import tw from 'twin.macro';

import { FastForward, PlayPause, Rewind } from '~/components/PlayButtons';

type IPlayButtons = React.FC<{
  isPlaying: boolean;
  setIsPlaying: React.Dispatch<React.SetStateAction<boolean>>;
  curTime: number;
  seek: (arg0: number) => void;
}>;

export const PlayButtons: IPlayButtons = ({
  isPlaying,
  setIsPlaying,
  curTime,
  seek,
}) => (
  <div tw="flex items-center justify-center flex-none text-primary-500">
    <Rewind curTime={curTime} isPlaying={isPlaying} seek={seek} />
    <PlayPause isPlaying={isPlaying} setIsPlaying={setIsPlaying} />
    <FastForward />
  </div>
);
