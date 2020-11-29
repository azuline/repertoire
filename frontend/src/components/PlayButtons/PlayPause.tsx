import clsx from 'clsx';
import * as React from 'react';
import { Icon } from 'src/components';
import { PlayQueueContext } from 'src/contexts';
import { SetValue } from 'src/types';

export const PlayPause: React.FC<{
  className?: string;
  isPlaying: boolean;
  setIsPlaying: SetValue<boolean>;
}> = ({ className, isPlaying, setIsPlaying }) => {
  const { playQueue, curIndex, setCurIndex } = React.useContext(PlayQueueContext);

  const togglePlay = React.useCallback(() => {
    if (playQueue.length !== 0 && curIndex === null) {
      setCurIndex(0);
    } else {
      setIsPlaying((p: boolean) => !p);
    }
  }, [playQueue, curIndex, setCurIndex, setIsPlaying]);

  return (
    <Icon
      className={clsx(className, 'mr-1 cursor-pointer hover:text-primary')}
      icon={isPlaying ? 'pause-small' : 'play-small'}
      onClick={togglePlay}
    />
  );
};
