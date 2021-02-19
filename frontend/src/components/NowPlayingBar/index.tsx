import 'twin.macro';

import * as React from 'react';

import { PlayQueueContext } from '~/contexts';
import { useAudio } from '~/hooks';

import { ExpandPlaying } from './ExpandPlaying';
import { PlayButtons } from './PlayButtons';
import { Progress } from './Progress';
import { ProgressBar } from './ProgressBar';
import { TrackInfo } from './TrackInfo';
import { VolumeControl } from './VolumeControl';

export const NowPlayingBar: React.FC = () => {
  const { playQueue, curIndex } = React.useContext(PlayQueueContext);
  const { isPlaying, setIsPlaying, curTime, seek } = useAudio();

  const curTrack = curIndex !== null ? playQueue[curIndex] : null;

  return (
    <div tw="relative flex-none w-full h-16 bg-background-900 z-10">
      <ProgressBar curTime={curTime} curTrack={curTrack} seek={seek} />
      <div tw="flex items-center full">
        <PlayButtons
          curTime={curTime}
          isPlaying={isPlaying}
          seek={seek}
          setIsPlaying={setIsPlaying}
        />
        {curTrack ? <TrackInfo curTrack={curTrack} /> : <div tw="flex-1" />}
        <Progress curTime={curTime} curTrack={curTrack} />
        <VolumeControl />
        <ExpandPlaying />
      </div>
    </div>
  );
};
