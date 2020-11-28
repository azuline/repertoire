import * as React from 'react';
import { Icon } from 'src/components';
import { PlayQueueContext } from 'src/contexts';
import { SetValue } from 'src/types';

export const PlayButtons: React.FC<{
  isPlaying: boolean;
  setIsPlaying: SetValue<boolean>;
  curTime: number;
  seek: SetValue<number>;
}> = ({ isPlaying, setIsPlaying, curTime, seek }) => {
  const { playQueue, curIndex, setCurIndex } = React.useContext(PlayQueueContext);

  const togglePlay = React.useCallback(() => {
    if (playQueue.length !== 0 && curIndex === null) {
      setCurIndex(0);
    } else {
      setIsPlaying((p: boolean) => !p);
    }
  }, [playQueue, curIndex, setCurIndex, setIsPlaying]);

  const fastForward = React.useCallback(
    () => setCurIndex((idx) => (idx !== null && idx !== playQueue.length - 1 ? idx + 1 : null)),
    [setCurIndex, playQueue],
  );

  const rewind = React.useCallback(() => {
    if (isPlaying && curTime > 10) {
      seek(0);
    } else {
      setCurIndex((idx) => (idx !== null && idx !== 0 ? idx - 1 : null));
    }
  }, [curTime, setCurIndex, isPlaying]);

  return (
    <div className="flex items-center justify-center flex-none mx-4 sm:mx-8 text-primary-alt">
      <Icon
        className="mr-1 cursor-pointer w-9 hover:text-primary"
        icon="rewind-small"
        onClick={rewind}
      />
      <Icon
        className="w-12 mr-1 cursor-pointer hover:text-primary"
        icon={isPlaying ? 'pause-small' : 'play-small'}
        onClick={togglePlay}
      />
      <Icon
        className="cursor-pointer w-9 hover:text-primary"
        icon="fast-forward-small"
        onClick={fastForward}
      />
    </div>
  );
};
