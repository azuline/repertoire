import * as React from 'react';

import { Icon } from 'src/components/common/Icon';
import { Searchbar } from './Searchbar';
import { User } from './User';
import { SidebarContext } from 'src/contexts';
import clsx from 'clsx';

export const Header: React.FC<{ className?: string | undefined; searchbar?: boolean }> = ({
  className,
  searchbar = true,
}) => {
  const { openBar, setOpenBar } = React.useContext(SidebarContext);

  const toggleOpen = React.useCallback(() => setOpenBar((o) => !o), [setOpenBar]);

  return (
    <div className={clsx(className, 'relative z-10 flex-none flex items-center w-full h-20 px-8')}>
      {!openBar && (
        <>
          <Icon
            className="hidden sm:block -ml-2 w-6 mr-4 cursor-pointer"
            icon="hamburger"
            onClick={toggleOpen}
          />
          <Icon
            className="block sm:hidden -ml-2 w-6 mr-4 cursor-pointer"
            icon="chevron-double-left-medium"
            onClick={toggleOpen}
          />
        </>
      )}
      {searchbar && <Searchbar className="mr-4" />}
      <User />
    </div>
  );
};
