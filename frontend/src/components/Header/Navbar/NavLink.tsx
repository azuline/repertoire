import * as React from 'react';

import { Link } from 'src/components/common/Link';

export const NavLink: React.FC<{
  children: React.ReactNode;
  url: string;
  activeRoute?: string | undefined;
}> = ({ children, url, activeRoute }) => {
  const active = React.useMemo(() => activeRoute && url === activeRoute, [activeRoute, url]);

  return (
    <Link href={url} className="flex items-center justify-center hover:text-bold px-2 lg:px-5">
      <div className={active ? 'border-bold border-b-2' : ''}>
        <div className="py-2 text-sm uppercase font-semibold">{children}</div>
      </div>
    </Link>
  );
};
