import * as React from 'react';
import { useHistory } from 'react-router-dom';
import { Icon } from '~/components/common';
import { RouteList } from '~/components/Routelist';

export const Sidebar: React.FC = () => {
  const history = useHistory();

  return (
    <div
      className="sticky top-0 flex-col flex-none hidden w-52 bg-background-900 sm:flex"
      style={{ height: 'calc(100vh - 4rem)' }}
    >
      <div className="mt-6 mb-4">
        <div className="flex items-center pl-6 pr-4">
          <div
            className="flex items-center pr-4 cursor-pointer"
            onClick={(): void => history.push('/')}
          >
            <Icon className="w-8 text-primary-500" icon="logo" />
            <div className="ml-2 font-semibold">
              <span className="text-primary-500">reper</span>toire
            </div>
          </div>
        </div>
      </div>
      <div className="px-6 overflow-y-auto md:px-8">
        <RouteList />
      </div>
    </div>
  );
};
