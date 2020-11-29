import * as React from 'react';
import { Icon } from 'src/components';
import { PlayQueueContext } from 'src/contexts';
import { SetValue } from 'src/types';

export const Rewind: React.FC<{
  className?: string;
  isPlaying: boolean;
  setIsPlaying: SetValue<boolean>;
  curTime: number;
  seek: SetValue<number>;
}> = ({ className, isPlaying, setIsPlaying, curTime, seek }) => {
  const { setCurIndex } = React.useContext(PlayQueueContext);

  const rewind = React.useCallback(() => {
    if (isPlaying && curTime > 10) {
      seek(0);
    } else {
      setCurIndex((idx) => (idx !== null && idx !== 0 ? idx - 1 : null));
    }
  }, [curTime, setCurIndex, isPlaying, seek]);

  return (
    <Icon
      className="mr-1 cursor-pointer w-9 hover:text-primary"
      icon="rewind-small"
      onClick={rewind}
    />
  );
};
