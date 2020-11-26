import clsx from 'clsx';
import * as React from 'react';
import { Icon } from 'src/components/common';
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
    <div className={clsx(className, 'relative z-10 flex-none flex items-center w-full h-20 px-8')}>
      {!isSidebarOpen && (
        <>
          <Icon
            className="hidden w-6 mr-4 -ml-2 cursor-pointer sm:block"
            icon="hamburger"
            onClick={toggleOpen}
          />
          <Icon
            className="block w-6 mr-4 -ml-2 cursor-pointer sm:hidden"
            icon="chevron-double-left-medium"
            onClick={toggleOpen}
          />
        </>
      )}
      {searchbar && <Searchbar className="mr-4" />}
      <User className="hidden ml-auto sm:flex" />
    </div>
  );
};
