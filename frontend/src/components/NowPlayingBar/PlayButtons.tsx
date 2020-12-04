import * as React from 'react';
import { FastForward, PlayPause, Rewind } from 'src/components/PlayButtons';
import { SetValue } from 'src/types';

export const PlayButtons: React.FC<{
  isPlaying: boolean;
  setIsPlaying: SetValue<boolean>;
  curTime: number;
  seek: (arg0: number) => void;
}> = ({ isPlaying, setIsPlaying, curTime, seek }) => (
  <div className="flex items-center justify-center flex-none mx-2 text-primary-500 sm:mx-8">
    <Rewind
      className="mr-1 cursor-pointer hover:text-primary-400 w-9"
      curTime={curTime}
      isPlaying={isPlaying}
      seek={seek}
    />
    <PlayPause
      className="w-12 mr-1 cursor-pointer hover:text-primary-400"
      isPlaying={isPlaying}
      setIsPlaying={setIsPlaying}
    />
    <FastForward className="cursor-pointer hover:text-primary-400 w-9" />
  </div>
);
