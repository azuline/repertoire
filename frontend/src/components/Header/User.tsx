import 'twin.macro';

import { gql } from '@apollo/client';
import * as React from 'react';
import { useToasts } from 'react-toast-notifications';

import { Icon, Link } from '~/components/common';
import { AuthorizationContext } from '~/contexts';
import { useHeaderFetchUserQuery } from '~/graphql';
import { useRequest } from '~/hooks';

type IUser = React.FC<{ className?: string }>;

export const User: IUser = ({ className }) => {
  const { setLoggedIn } = React.useContext(AuthorizationContext);
  const { addToast } = useToasts();
  const { data } = useHeaderFetchUserQuery();
  const request = useRequest();

  const logout = (): void => {
    (async (): Promise<void> => {
      await request('/api/session', { method: 'DELETE' });

      addToast('Logged out!', { appearance: 'success' });
      setLoggedIn(false);
    })();
  };

  return (
    <div className={className} tw="flex items-center h-full min-w-0">
      <div tw="mr-2 truncate">{data?.user?.nickname || 'Loading...'}</div>
      <Link
        href="/settings"
        tw="flex-none px-1 py-2 cursor-pointer hover:text-primary-400 text-primary-500 sm:hidden"
      >
        <Icon icon="cog-medium" title="Settings" tw="w-6" />
      </Link>
      <Link
        href="/settings"
        tw="flex-none hidden px-1 py-2 cursor-pointer hover:text-primary-400 text-primary-500 sm:block"
      >
        <Icon icon="cog-medium" title="Settings" tw="w-6" />
      </Link>
      <div
        tw="flex-none px-2 py-1 -mr-2 cursor-pointer hover:text-primary-400 text-primary-500"
        onClick={logout}
      >
        <Icon icon="logout-medium" title="Logout" tw="w-6" />
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
