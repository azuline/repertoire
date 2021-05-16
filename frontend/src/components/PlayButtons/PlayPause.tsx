import React from 'react';

import { Icon } from '~/components';
import { PlayQueueContext } from '~/contexts';
import { ISetValue } from '~/types';

type IPlayPause = React.FC<{
  className?: string;
  isPlaying: boolean;
  setIsPlaying: ISetValue<boolean>;
}>;

export const PlayPause: IPlayPause = ({ className, isPlaying, setIsPlaying }) => {
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
      className={className}
      icon={isPlaying ? 'pause-small' : 'play-small'}
      tw="mr-1 cursor-pointer hover:text-primary-400 w-12"
      onClick={togglePlay}
    />
  );
};
