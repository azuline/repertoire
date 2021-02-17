import 'twin.macro';

import * as React from 'react';

import { Link } from '~/components';

export const RedirectToNowPlaying: React.FC<{ className?: string; children: React.ReactNode }> = ({
  className,
  children,
}) => {
  return (
    <Link className={className} href="/playing" tw="flex">
      {children}
    </Link>
  );
};
