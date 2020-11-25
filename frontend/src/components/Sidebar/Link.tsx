import clsx from 'clsx';
import * as React from 'react';
import { Link } from 'src/components/common';
import { SidebarContext } from 'src/contexts';

export const NavLink: React.FC<{
  url: string;
  label: string;
  activeRoute?: string | null;
  className?: string;
}> = ({ url, label, activeRoute, className }) => {
  const active = React.useMemo(() => url === activeRoute, [activeRoute, url]);
  const { setSidebarOpen } = React.useContext(SidebarContext);

  const closeSidebar = React.useCallback(() => setSidebarOpen(false), [setSidebarOpen]);

  return (
    <>
      <Link className="hidden sm:block" href={url}>
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
      <Link className="block sm:hidden" href={url} onClick={closeSidebar}>
        <div
          className={clsx(
            className,
            active && 'sm:bg-primary-alt',
            'text-foreground cursor-pointer hover:bg-gray-200 hover:bg-opacity-5',
          )}
        >
          {label}
        </div>
      </Link>
    </>
  );
};
