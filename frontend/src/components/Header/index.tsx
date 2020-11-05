import * as React from 'react';

import { Navbar } from './Navbar';
import { Searchbar } from './Searchbar';
import { User } from './User';
import { Title } from './Title';

export const Header: React.FC = () => {
  return (
    <div>
      <div className="flex items-center w-full h-12 py-2 px-4 bg-bg border-highlight border-b-2">
        <Title className="mr-auto" />
        <Searchbar className="mr-4 cursor-pointer" />
        <User />
      </div>
      <Navbar />
    </div>
  );
};
