import * as React from 'react';

import { Navbar } from './Navbar';
import { Searchbar } from './Searchbar';
import { User } from './User';

export const Header: React.FC = () => {
  return (
    <div>
      <div className="flex items-center w-full h-12 px-4 bg-bg border-highlight border-b-2">
        <Searchbar className="mr-4" />
        <User />
      </div>
      <Navbar />
    </div>
  );
};
