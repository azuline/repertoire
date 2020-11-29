import clsx from 'clsx';
import * as React from 'react';
import { Icon } from 'src/components';
import { PlayQueueContext } from 'src/contexts';

export const FastForward: React.FC<{
  className?: string;
}> = ({ className }) => {
  const { playQueue, setCurIndex } = React.useContext(PlayQueueContext);

  const fastForward = React.useCallback(
    () => setCurIndex((idx) => (idx !== null && idx !== playQueue.length - 1 ? idx + 1 : null)),
    [setCurIndex, playQueue],
  );

  return (
    <Icon
      className={clsx(className, 'cursor-pointer hover:text-primary-400')}
      icon="fast-forward-small"
      onClick={fastForward}
    />
  );
};
