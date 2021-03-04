import { gql } from '@apollo/client';
import * as React from 'react';
import { useToasts } from 'react-toast-notifications';

import { Icon, Link } from '~/components/common';
import { AuthorizationContext } from '~/contexts';
import { useHeaderFetchUserQuery } from '~/graphql';
import { useRequest } from '~/hooks';

type IUserComponent = React.FC<{ className?: string }>;

export const User: IUserComponent = ({ className }) => {
  const { setLoggedIn } = React.useContext(AuthorizationContext);
  const { addToast } = useToasts();
  const { data } = useHeaderFetchUserQuery();
  const request = useRequest();

  const logout = async (): Promise<void> => {
    await request('/api/session', { method: 'DELETE' });

    addToast('Logged out!', { appearance: 'success' });
    setLoggedIn(false);
  };

  return (
    <div className={className} tw="flex items-center h-full min-w-0">
      <div tw="mr-2 truncate">{data?.user?.nickname ?? 'Loading...'}</div>
      <div tw="flex-none px-1 py-2 sm:hidden">
        <Link
          href="/settings"
          tw="cursor-pointer hover:text-primary-400 text-primary-500"
        >
          <Icon icon="cog-medium" title="Settings" tw="w-6" />
        </Link>
      </div>
      <div tw="flex-none px-1 py-2 hidden sm:block">
        <Link
          href="/settings"
          tw="cursor-pointer hover:text-primary-400 text-primary-500"
        >
          <Icon icon="cog-medium" title="Settings" tw="w-6" />
        </Link>
      </div>
      <div tw="flex-none px-2 py-1 -mr-2">
        <div
          tw="cursor-pointer hover:text-primary-400 text-primary-500"
          onClick={logout}
        >
          <Icon icon="logout-medium" title="Logout" tw="w-6" />
        </div>
      </div>
    </div>
  );
};

/* eslint-disable */
gql`
  query HeaderFetchUser {
    user {
      ...UserFields
    }
  }
`;
