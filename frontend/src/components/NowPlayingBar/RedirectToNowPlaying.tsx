import clsx from 'clsx';
import * as React from 'react';

import { Link } from '~/components';

export const RedirectToNowPlaying: React.FC<{ className?: string; children: React.ReactNode }> = ({
  className,
  children,
}) => {
  return (
    <Link className={clsx('flex', className)} href="/playing">
      {children}
    </Link>
  );
};
