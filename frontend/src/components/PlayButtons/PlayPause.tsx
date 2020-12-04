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

  const togglePlay = (): void => {
    if (playQueue.length !== 0 && curIndex === null) {
      setCurIndex(0);
    } else {
      setIsPlaying((p: boolean) => !p);
    }
  };

  return (
    <Icon
      className={clsx(className, 'mr-1 cursor-pointer hover:text-primary-400')}
      icon={isPlaying ? 'pause-small' : 'play-small'}
      onClick={togglePlay}
    />
  );
};
