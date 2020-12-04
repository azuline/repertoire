import clsx from 'clsx';
import * as React from 'react';
import { Link } from 'src/components/common';
import { SidebarContext } from 'src/contexts';

export const NavLink: React.FC<{
  url: string;
  label: string;
  activeRoute?: string | null;
}> = ({ url, label, activeRoute }) => {
  const active = React.useMemo(() => url === activeRoute, [activeRoute, url]);
  const { setSidebarOpen } = React.useContext(SidebarContext);

  const closeSidebar = React.useCallback(() => setSidebarOpen(false), [setSidebarOpen]);

  return (
    <>
      <Link className="hidden sm:block" href={url}>
        <div
          className={clsx(
            active
              ? 'border-l-4 border-primary-500 bg-white bg-opacity-10'
              : 'border-transparent hover-emph-bg',
            'cursor-pointer text-foreground border-l-4 pl-7 pr-8 py-2',
          )}
        >
          {label}
        </div>
      </Link>
      <Link className="block sm:hidden" href={url} onClick={closeSidebar}>
        <div className="px-8 py-2 cursor-pointer text-foreground hover-emph-bg">{label}</div>
      </Link>
    </>
  );
};
