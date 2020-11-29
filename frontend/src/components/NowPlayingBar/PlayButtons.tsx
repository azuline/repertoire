import * as React from 'react';
import { FastForward, PlayPause, Rewind } from 'src/components/PlayButtons';
import { SetValue } from 'src/types';

export const PlayButtons: React.FC<{
  isPlaying: boolean;
  setIsPlaying: SetValue<boolean>;
  curTime: number;
  seek: SetValue<number>;
}> = ({ isPlaying, setIsPlaying, curTime, seek }) => (
  <div className="flex items-center justify-center flex-none mx-4 sm:mx-8 text-primary-600">
    <Rewind
      className="mr-1 cursor-pointer w-9 hover:text-primary-400"
      isPlaying={isPlaying}
      setIsPlaying={setIsPlaying}
      curTime={curTime}
      seek={seek}
    />
    <PlayPause
      className="w-12 mr-1 cursor-pointer hover:text-primary-400"
      isPlaying={isPlaying}
      setIsPlaying={setIsPlaying}
    />
    <FastForward className="cursor-pointer w-9 hover:text-primary-400" />
  </div>
);
