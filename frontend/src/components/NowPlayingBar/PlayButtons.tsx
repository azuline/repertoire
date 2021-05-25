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
  <div
    css={[
      tw`flex items-center justify-center flex-none mx-2 sm:mx-6 lg:mx-10`,
      tw`text-primary-500`,
    ]}
  >
    <Rewind curTime={curTime} isPlaying={isPlaying} seek={seek} />
    <PlayPause isPlaying={isPlaying} setIsPlaying={setIsPlaying} />
    <FastForward />
  </div>
);
