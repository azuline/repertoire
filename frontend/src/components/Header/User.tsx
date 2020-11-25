import * as React from 'react';

import { AuthorizationContext, SidebarContext } from 'src/contexts';

import { Icon, Link } from 'src/components/common';
import clsx from 'clsx';
import { fetchUser } from 'src/lib';
import { useRequest } from 'src/hooks';
import { useToasts } from 'react-toast-notifications';

export const User: React.FC<{ className?: string }> = ({ className }) => {
  const { setLoggedIn } = React.useContext(AuthorizationContext);
  const { setSidebarOpen } = React.useContext(SidebarContext);
  const { addToast } = useToasts();
  const { status, data } = fetchUser();
  const request = useRequest();

  const closeSidebar = React.useCallback(() => setSidebarOpen(false), [setSidebarOpen]);

  const logout = React.useCallback(() => {
    (async (): Promise<void> => {
      await request('/session', {
        method: 'DELETE',
      });

      addToast('Logged out!', { appearance: 'success' });
      setLoggedIn(false);
    })();
  }, [request, setLoggedIn, addToast]);

  return (
    <div className={clsx(className, 'flex h-full items-center')}>
      <Icon className="w-5 mr-1" icon="user-medium" />
      <div className="mr-3">{status === 'success' && data ? data.user.username : 'Loading...'}</div>
      <Link className="sm:hidden" href="/settings" onClick={closeSidebar}>
        <Icon className="w-5 mr-2 text-primary cursor-pointer" title="Settings" icon="cog-medium" />
      </Link>
      <Link className="hidden sm:block" href="/settings">
        <Icon className="w-5 mr-2 text-primary cursor-pointer" title="Settings" icon="cog-medium" />
      </Link>
      <Icon
        className="w-5 text-primary cursor-pointer"
        title="Logout"
        icon="logout-medium"
        onClick={logout}
      />
    </div>
  );
};
