import 'twin.macro';

import * as React from 'react';

import { FastForward, PlayPause, Rewind } from '~/components/PlayButtons';
import { ISetValue } from '~/types';

type IPlayButtons = React.FC<{
  isPlaying: boolean;
  setIsPlaying: ISetValue<boolean>;
  curTime: number;
  seek: (arg0: number) => void;
}>;

export const PlayButtons: IPlayButtons = ({ isPlaying, setIsPlaying, curTime, seek }) => (
  <div tw="flex items-center justify-center flex-none mx-2 text-primary-500 sm:mx-6 lg:mx-10">
    <Rewind
      curTime={curTime}
      isPlaying={isPlaying}
      seek={seek}
      tw="mr-1 cursor-pointer hover:text-primary-400 w-9"
    />
    <PlayPause
      isPlaying={isPlaying}
      setIsPlaying={setIsPlaying}
      tw="w-12 mr-1 cursor-pointer hover:text-primary-400"
    />
    <FastForward tw="cursor-pointer hover:text-primary-400 w-9" />
  </div>
);
