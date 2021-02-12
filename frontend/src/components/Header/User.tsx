import clsx from 'clsx';
import * as React from 'react';
import { useToasts } from 'react-toast-notifications';
import { Icon, Link } from '~/components/common';
import { AuthorizationContext } from '~/contexts';
import { useRequest } from '~/hooks';
import { useFetchUser } from '~/lib';

export const User: React.FC<{ className?: string }> = ({ className }) => {
  const { setLoggedIn } = React.useContext(AuthorizationContext);
  const { addToast } = useToasts();
  const { data } = useFetchUser();
  const request = useRequest();

  const logout = (): void => {
    (async (): Promise<void> => {
      await request('/api/session', { method: 'DELETE' });

      addToast('Logged out!', { appearance: 'success' });
      setLoggedIn(false);
    })();
  };

  return (
    <div className={clsx(className, 'flex items-center h-full min-w-0')}>
      <div className="mr-2 truncate">{data?.user?.nickname || 'Loading...'}</div>
      <Link
        className="flex-none px-1 py-2 cursor-pointer hover:text-primary-400 text-primary-500 sm:hidden"
        href="/settings"
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
        className="flex-none px-2 py-1 -mr-2 cursor-pointer hover:text-primary-400 text-primary-500"
        onClick={logout}
      >
        <Icon className="w-6" icon="logout-medium" title="Logout" />
      </div>
    </div>
  );
};
