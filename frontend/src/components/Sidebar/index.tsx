import 'twin.macro';

import * as React from 'react';
import { useHistory } from 'react-router-dom';

import { Icon } from '~/components/common';
import { RouteList } from '~/components/Routelist';

export const Sidebar: React.FC = () => {
  const history = useHistory();

  return (
    <div
      style={{ height: 'calc(100vh - 4rem)' }}
      tw="sticky top-0 flex-col flex-none hidden w-52 bg-background-900 sm:flex"
    >
      <div tw="mt-6 mb-4">
        <div tw="flex items-center pl-6 pr-4">
          <div tw="flex items-center pr-4 cursor-pointer" onClick={(): void => history.push('/')}>
            <Icon icon="logo" tw="w-8 text-primary-500" />
            <div tw="ml-2 font-semibold">
              <span tw="text-primary-500">reper</span>toire
            </div>
          </div>
        </div>
      </div>
      <div tw="px-6 overflow-y-auto md:px-8">
        <div tw="pb-4">
          <RouteList />
        </div>
      </div>
    </div>
  );
};
