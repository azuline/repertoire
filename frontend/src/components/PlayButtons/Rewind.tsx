import React from 'react';

import { Icon } from '~/components';
import { PlayQueueContext } from '~/contexts';

type IRewind = React.FC<{
  className?: string;
  isPlaying: boolean;
  curTime: number;
  seek: (arg0: number) => void;
}>;

export const Rewind: IRewind = ({ className, isPlaying, curTime, seek }) => {
  const { setCurIndex } = React.useContext(PlayQueueContext);

  const rewind = (): void => {
    if (isPlaying && curTime > 10) {
      seek(0);
    } else {
      setCurIndex((idx) => (idx !== null && idx !== 0 ? idx - 1 : null));
    }
  };

  return (
    <Icon
      className={className}
      icon="rewind-small"
      tw="cursor-pointer mr-1 hover:text-primary-400 w-9"
      onClick={rewind}
    />
  );
};
