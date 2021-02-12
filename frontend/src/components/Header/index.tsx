import clsx from 'clsx';
import * as React from 'react';
import { Icon, Link } from '~/components/common';

import { Searchbar } from './Searchbar';
import { User } from './User';

export const Header: React.FC<{ className?: string; searchbar?: boolean }> = ({
  className,
  searchbar = true,
}) => {
  return (
    <div className={clsx(className, 'flex items-center flex-none w-full h-20 mb-2')}>
      <Link className="block sm:hidden" href="/mobile">
        <Icon
          className="w-6 mr-4 cursor-pointer hover:text-primary-400 text-primary-500"
          icon="home-small"
        />
      </Link>
      {searchbar && <Searchbar />}
      <User className="hidden pl-6 ml-auto sm:flex" />
    </div>
  );
};
