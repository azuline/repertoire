import clsx from 'clsx';
import * as React from 'react';

import { Icon } from '~/components';
import { PlayQueueContext } from '~/contexts';
import { ISetValue } from '~/types';

export const PlayPause: React.FC<{
  className?: string;
  isPlaying: boolean;
  setIsPlaying: ISetValue<boolean>;
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
