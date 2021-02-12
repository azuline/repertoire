import clsx from 'clsx';
import * as React from 'react';

import { Icon } from '~/components';
import { PlayQueueContext } from '~/contexts';

export const FastForward: React.FC<{
  className?: string;
}> = ({ className }) => {
  const { playQueue, setCurIndex } = React.useContext(PlayQueueContext);

  const fastForward = (): void =>
    setCurIndex((idx) => (idx !== null && idx !== playQueue.length - 1 ? idx + 1 : null));

  return (
    <Icon
      className={clsx(className, 'cursor-pointer hover:text-primary-400')}
      icon="fast-forward-small"
      onClick={fastForward}
    />
  );
};
