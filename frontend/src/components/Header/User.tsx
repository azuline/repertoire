import { gql } from '@apollo/client';
import * as React from 'react';
import { useHistory } from 'react-router';
import { useToasts } from 'react-toast-notifications';

import { Icon } from '~/components/common';
import { AuthorizationContext } from '~/contexts';
import { useHeaderFetchUserQuery } from '~/graphql';
import { useRequest } from '~/hooks';

type IUserComponent = React.FC<{ className?: string }>;

export const User: IUserComponent = ({ className }) => {
  const { setLoggedIn } = React.useContext(AuthorizationContext);
  const { addToast } = useToasts();
  const { data } = useHeaderFetchUserQuery();
  const request = useRequest();
  const history = useHistory();

  const logout = async (): Promise<void> => {
    await request('/api/session', { method: 'DELETE' });

    addToast('Logged out!', { appearance: 'success' });
    setLoggedIn(false);
    history.push('/');
  };

  return (
    <div className={className} tw="flex items-center h-full min-w-0">
      <div className="header--username" tw="mr-2 truncate">
        {data?.user?.nickname ?? 'Loading...'}
      </div>
      <div tw="flex-none px-2 py-1 -mr-2">
        <div
          tw="cursor-pointer hover:text-primary-400 text-primary-500 flex items-center"
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
