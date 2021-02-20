import * as React from 'react';
import { useHistory } from 'react-router-dom';

import { Icon, RouteList, Searchbar, User } from '~/components';

export const Mobile: React.FC = () => {
  const history = useHistory();

  const goHome = (): void => history.push('/');

  return (
    <div tw="flex flex-col flex-1 pb-6">
      <div tw="flex items-center mt-6 mb-4">
        <div tw="flex items-center pr-4 cursor-pointer" onClick={goHome}>
          <Icon icon="logo" tw="w-8 text-primary-500" />
          <div tw="ml-2 font-semibold">
            <span tw="text-primary-500">reper</span>toire
          </div>
        </div>
        <User tw="ml-auto" />
      </div>
      <Searchbar shrink={false} tw="flex-none block h-16 mb-4" />
      <RouteList />
    </div>
  );
};
