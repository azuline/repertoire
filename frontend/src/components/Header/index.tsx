import clsx from 'clsx';
import * as React from 'react';
import { Icon, Link } from 'src/components/common';
import { SidebarContext } from 'src/contexts';

import { Searchbar } from './Searchbar';
import { User } from './User';

export const Header: React.FC<{ className?: string; searchbar?: boolean }> = ({
  className,
  searchbar = true,
}) => {
  const { isSidebarOpen, setSidebarOpen } = React.useContext(SidebarContext);

  const toggleOpen = React.useCallback(() => setSidebarOpen((o) => !o), [setSidebarOpen]);

  return (
    <div className={clsx(className, 'z-10 flex items-center flex-none w-full h-20 px-8')}>
      {isSidebarOpen || (
        <Icon
          className="hidden w-6 mr-4 cursor-pointer hover:text-primary-400 text-primary-500 sm:block"
          icon="hamburger"
          onClick={toggleOpen}
        />
      )}
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
