import clsx from 'clsx';
import * as React from 'react';
import { Link } from 'src/components';
import { SidebarContext } from 'src/contexts';

export const RedirectToNowPlaying: React.FC<{ className?: string; children: React.ReactNode }> = ({
  className,
  children,
}) => {
  const { setSidebarOpen } = React.useContext(SidebarContext);
  const closeSidebar = React.useCallback(() => setSidebarOpen(false), [setSidebarOpen]);

  return (
    <>
      <Link className={clsx('sm:hidden', className)} href="/playing" onClick={closeSidebar}>
        {children}
      </Link>
      <Link className={clsx('hidden sm:flex', className)} href="/playing">
        {children}
      </Link>
    </>
  );
};
