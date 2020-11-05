import * as React from 'react';

import { Navbar } from './Navbar';
import { Searchbar } from './Searchbar';
import { User } from './User';
import { Title } from './Title';

export const Header: React.FC = () => {
  const [searchFocused, setSearchFocused] = React.useState<boolean>(false);
  return (
    <div>
      <div className="flex items-center w-full h-12 px-4 bg-bg border-highlight border-b-2">
        {!searchFocused && <Title className="mr-auto" />}
        <Searchbar className="mr-4" focus={searchFocused} setFocus={setSearchFocused} />
        <User />
      </div>
      <Navbar />
    </div>
  );
};
