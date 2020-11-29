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
      <div className="mr-2 truncate">{data?.user?.nickname || 'Loading...'}</div>
      <Link
        className="flex-none px-1 py-2 cursor-pointer hover:text-primary-400 text-primary-500 sm:hidden"
        href="/settings"
        onClick={closeSidebar}
      >
        <Icon className="w-6" icon="cog-medium" title="Settings" />
      </Link>
      <Link
        className="flex-none hidden px-1 py-2 cursor-pointer hover:text-primary-400 text-primary-500 sm:block"
        href="/settings"
      >
        <Icon className="w-6" icon="cog-medium" title="Settings" />
      </Link>
      <div
        className="flex-none px-2 py-1 cursor-pointer hover:text-primary-400 text-primary-500"
        onClick={logout}
      >
        <Icon className="w-6" icon="logout-medium" title="Logout" />
      </div>
    </div>
  );
};
