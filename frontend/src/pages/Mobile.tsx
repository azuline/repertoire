import * as React from 'react';
import { useHistory } from 'react-router-dom';
import { Icon } from '~/components/common';
import { Searchbar } from '~/components/Header/Searchbar';
import { User } from '~/components/Header/User';
import { RouteList } from '~/components/Routelist';

export const Mobile: React.FC = () => {
  const history = useHistory();

  const goHome = (): void => history.push('/');

  return (
    <div className="flex flex-col flex-1 pb-6">
      <div className="flex items-center mt-6 mb-4">
        <div className="flex items-center pr-4 cursor-pointer" onClick={goHome}>
          <Icon className="w-8 text-primary-500" icon="logo" />
          <div className="ml-2 font-semibold">
            <span className="text-primary-500">reper</span>toire
          </div>
        </div>
        <User className="ml-auto" />
      </div>
      <Searchbar className="flex-none block h-16 mb-4" shrink={false} />
      <RouteList />
    </div>
  );
};
