import clsx from 'clsx';
import * as React from 'react';
import { Icon } from 'src/components';
import { PlayQueueContext } from 'src/contexts';

export const Rewind: React.FC<{
  className?: string;
  isPlaying: boolean;
  curTime: number;
  seek: (arg0: number) => void;
}> = ({ className, isPlaying, curTime, seek }) => {
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
      className={clsx(className, 'cursor-pointer mr-1 hover:text-primary-400')}
      icon="rewind-small"
      onClick={rewind}
    />
  );
};
