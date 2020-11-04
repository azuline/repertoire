import * as React from 'react';

import clsx from 'clsx';

export const Card: React.FC<{ children: React.ReactNode; className?: string }> = ({
  children,
  className = '',
}) => {
  return <div className={clsx(className, 'bg-background-alt rounded p-2')}>{children}</div>;
};
