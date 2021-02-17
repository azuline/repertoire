import 'twin.macro';

import * as React from 'react';

import { Icon, Link } from '~/components/common';

import { Searchbar } from './Searchbar';
import { User } from './User';

export { Searchbar } from './Searchbar';
export { User } from './User';

type IHeader = React.FC<{ className?: string; searchbar?: boolean }>;

export const Header: IHeader = ({ className, searchbar = true }) => {
  return (
    <div className={className} tw="flex items-center flex-none w-full h-20 mb-2">
      <Link href="/mobile" tw="block sm:hidden">
        <Icon
          icon="home-small"
          tw="w-6 mr-4 cursor-pointer hover:text-primary-400 text-primary-500"
        />
      </Link>
      {searchbar && <Searchbar />}
      <User tw="hidden pl-6 ml-auto sm:flex" />
    </div>
  );
};
