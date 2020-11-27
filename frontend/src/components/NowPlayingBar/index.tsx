import * as React from 'react';
import { PlayQueueContext } from 'src/contexts';
import { useAudio } from 'src/hooks';

import { ExpandPlaying } from './ExpandPlaying';
import { PlayButtons } from './PlayButtons';
import { Progress } from './Progress';
import { TrackInfo } from './TrackInfo';
import { VolumeControl } from './VolumeControl';

export const NowPlayingBar: React.FC = () => {
  const { playQueue, curIndex } = React.useContext(PlayQueueContext);
  const { isPlaying, setIsPlaying, curTime, seek } = useAudio();

  // prettier-ignore
  const curTrack = React.useMemo(
    () => (curIndex !== null ? playQueue[curIndex] : null),
    [playQueue, curIndex],
  );

  return (
    <div className="relative z-30 flex-none w-full h-16 border-t-2 border-gray-300 bg-background-alt2 dark:border-gray-700">
      <div className="flex items-center full">
        <Progress curTrack={curTrack} curTime={curTime} />
        <PlayButtons
          isPlaying={isPlaying}
          setIsPlaying={setIsPlaying}
          curTime={curTime}
          seek={seek}
        />
        <TrackInfo curTrack={curTrack} />
        <VolumeControl />
        <ExpandPlaying />
      </div>
    </div>
  );
};
