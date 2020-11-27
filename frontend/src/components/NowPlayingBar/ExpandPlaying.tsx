import * as React from 'react';
import { Icon, Link } from 'src/components';
import { SidebarContext } from 'src/contexts';

export const ExpandPlaying: React.FC = () => {
  const { setSidebarOpen } = React.useContext(SidebarContext);

  const closeSidebar = React.useCallback(() => setSidebarOpen(false), [setSidebarOpen]);

  return (
    <>
      <Link
        className="block p-2 pr-8 sm:hidden text-primary hover:text-primary-alt3"
        href="/playing"
        onClick={closeSidebar}
      >
        <Icon icon="chevron-up-medium" className="w-6" />
      </Link>
      <Link
        className="hidden p-2 pr-8 sm:block text-primary hover:text-primary-alt3"
        href="/playing"
      >
        <Icon icon="chevron-up-medium" className="w-6" />
      </Link>
    </>
  );
};
