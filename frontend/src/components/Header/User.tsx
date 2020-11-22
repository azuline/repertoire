import * as React from 'react';

import { AuthorizationContext } from 'src/contexts';
import { Icon } from 'src/components/common/Icon';
import clsx from 'clsx';
import { fetchUser } from 'src/lib';
import { useToasts } from 'react-toast-notifications';

export const User: React.FC<{ className?: string | undefined }> = ({ className }) => {
  const { status, data } = fetchUser();
  const { setToken } = React.useContext(AuthorizationContext);
  const { addToast } = useToasts();

  const logout = React.useCallback(() => {
    addToast('Logged out!', { appearance: 'success' });
    setToken(null);
  }, [setToken, addToast]);

  return (
    <div className={clsx(className, 'flex h-full items-center')}>
      <Icon className="w-5 mr-1" icon="user-medium" />
      <div className="mr-2">{status === 'success' && data ? data.user.username : 'Loading...'}</div>
      <Icon
        className="w-5 text-primary cursor-pointer"
        title="Logout"
        icon="logout-medium"
        onClick={logout}
      />
    </div>
  );
};
