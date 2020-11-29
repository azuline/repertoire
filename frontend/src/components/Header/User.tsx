import clsx from 'clsx';
import * as React from 'react';
import { useToasts } from 'react-toast-notifications';
import { Icon, Link } from 'src/components/common';
import { AuthorizationContext, SidebarContext } from 'src/contexts';
import { useRequest } from 'src/hooks';
import { useFetchUser } from 'src/lib';

export const User: React.FC<{ className?: string }> = ({ className }) => {
  const { setLoggedIn } = React.useContext(AuthorizationContext);
  const { setSidebarOpen } = React.useContext(SidebarContext);
  const { addToast } = useToasts();
  const { data } = useFetchUser();
  const request = useRequest();

  const closeSidebar = React.useCallback(() => setSidebarOpen(false), [setSidebarOpen]);

  const logout = React.useCallback(() => {
    (async (): Promise<void> => {
      await request('/session', { method: 'DELETE' });

      addToast('Logged out!', { appearance: 'success' });
      setLoggedIn(false);
    })();
  }, [request, setLoggedIn, addToast]);

  return (
    <div className={clsx(className, 'flex items-center h-full min-w-0')}>
      <Icon className="flex-none w-5 mr-1" icon="user-medium" />
      <div className="mr-3 truncate">{data?.user?.nickname || 'Loading...'}</div>
      <Link className="flex-none sm:hidden" href="/settings" onClick={closeSidebar}>
        <Icon
          className="w-5 mr-2 cursor-pointer hover:text-primary-400 text-primary-500"
          title="Settings"
          icon="cog-medium"
        />
      </Link>
      <Link className="flex-none hidden sm:block" href="/settings">
        <Icon
          className="w-5 mr-2 cursor-pointer hover:text-primary-400 text-primary-500"
          title="Settings"
          icon="cog-medium"
        />
      </Link>
      <Icon
        className="flex-none w-5 cursor-pointer hover:text-primary-400 text-primary-500"
        title="Logout"
        icon="logout-medium"
        onClick={logout}
      />
    </div>
  );
};
