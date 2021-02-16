import clsx from 'clsx';
import * as React from 'react';

import { Link } from '~/components/common';

export const NavLink: React.FC<{
  url: string;
  label: string;
  activeRoute?: string | null;
}> = ({ url, label, activeRoute }) => {
  const active = url === activeRoute;

  return (
    <>
      <Link className="hidden sm:block" href={url}>
        <div
          className={clsx(
            active
              ? 'border-l-4 border-primary-500 bg-white bg-opacity-7'
              : 'border-transparent hover-bg',
            'text-sm cursor-pointer text-foreground border-l-4 pl-7 pr-8 py-2',
          )}
        >
          {label}
        </div>
      </Link>
      <Link className="block sm:hidden" href={url}>
        <div className="px-6 py-2 cursor-pointer md:px-8 text-foreground hover-bg">
          {label}
        </div>
      </Link>
    </>
  );
};
