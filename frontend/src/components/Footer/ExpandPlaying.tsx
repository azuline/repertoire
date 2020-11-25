import * as React from 'react';
import { Icon, Link } from 'src/components';
import { SidebarContext } from 'src/contexts';

export const ExpandPlaying: React.FC = () => {
  const { setSidebarOpen } = React.useContext(SidebarContext);

  const closeSidebar = React.useCallback(() => setSidebarOpen(false), [setSidebarOpen]);

  return (
    <>
      <Link
        className="flex sm:hidden h-full items-center pl-2 pr-8 text-primary hover:text-primary-alt3"
        href="/playing"
        onClick={closeSidebar}
      >
        <Icon icon="chevron-up-medium" className="w-6" />
      </Link>
      <Link
        className="hidden sm:flex h-full items-center pl-2 pr-8 text-primary hover:text-primary-alt3"
        href="/playing"
      >
        <Icon icon="chevron-up-medium" className="w-6" />
      </Link>
    </>
  );
};
