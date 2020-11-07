import * as React from 'react';

import { Icon } from 'src/components/common/Icon';
import { Searchbar } from './Searchbar';
import { SidebarContext } from 'src/contexts';
import { User } from './User';
import clsx from 'clsx';

export const Header: React.FC<{ className?: string | undefined }> = ({ className }) => {
  const { openBar, setOpenBar } = React.useContext(SidebarContext);

  const toggleOpen = React.useCallback(() => setOpenBar((o) => !o), [setOpenBar]);

  return (
    <div className={clsx(className, 'flex items-center w-full h-20 px-8')}>
      {!openBar && (
        <Icon className="w-6 mr-4 cursor-pointer" icon="hamburger" onClick={toggleOpen} />
      )}
      <Searchbar className="mr-6" />
      <User />
    </div>
  );
};
