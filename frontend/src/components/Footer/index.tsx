import * as React from 'react';
import { PlayQueueContext } from 'src/contexts';
import { useAudio } from 'src/hooks';

import { ExpandPlaying } from './ExpandPlaying';
import { PlayButtons } from './PlayButtons';
import { Progress } from './Progress';
import { TrackInfo } from './TrackInfo';

export const Footer: React.FC = () => {
  const { playQueue, curIndex } = React.useContext(PlayQueueContext);
  const { isPlaying, setIsPlaying, curTime, seek } = useAudio();

  // prettier-ignore
  const curTrack = React.useMemo(
    () => (curIndex !== null ? playQueue[curIndex] : null),
    [playQueue, curIndex],
  );

  return (
    <div className="relative z-30 flex-none w-full h-16 bg-background-alt2 border-t-2 border-gray-300 dark:border-gray-700">
      <div className="full flex items-center">
        <Progress
          className="ml-4 hidden md:block flex-none"
          curTrack={curTrack}
          curTime={curTime}
        />
        <PlayButtons
          className="flex-none mx-8"
          isPlaying={isPlaying}
          setIsPlaying={setIsPlaying}
          curTime={curTime}
          seek={seek}
        />
        <TrackInfo curTrack={curTrack} />
        <ExpandPlaying />
      </div>
    </div>
  );
};
