import * as React from 'react';

import { Link } from '~/components';

type IRedirectToNowPlaying = React.FC<{
  className?: string;
  children: React.ReactNode;
}>;
export const RedirectToNowPlaying: IRedirectToNowPlaying = ({
  className,
  children,
}) => {
  return (
    <Link className={className} href="/playing" tw="flex">
      {children}
    </Link>
  );
};
