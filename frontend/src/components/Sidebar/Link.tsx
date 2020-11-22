import * as React from 'react';

import clsx from 'clsx';
import { Link } from 'src/components/common/Link';

export const NavLink: React.FC<{
  url: string;
  label: string;
  activeRoute?: string | undefined | null;
  className?: string | undefined;
}> = ({ url, label, activeRoute, className }) => {
  const active = React.useMemo(() => url === activeRoute, [activeRoute, url]);

  return (
    <Link href={url}>
      <div
        className={clsx(
          className,
          active ? 'bg-primary-alt' : 'hover:bg-gray-200 hover:bg-opacity-5',
          'text-foreground cursor-pointer',
        )}
      >
        {label}
      </div>
    </Link>
  );
};
