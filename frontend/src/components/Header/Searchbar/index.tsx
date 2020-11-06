import * as React from 'react';

import { Icon } from 'src/components/common/Icon';
import clsx from 'clsx';

// TODO: Implement a dropdown and stuff...

export const Searchbar: React.FC<{
  className?: string;
}> = ({ className = '' }) => {
  return (
    <div className={clsx(className, 'flex-1 relative')}>
      <div className="flex items-center h-full">
        <input className="w-full max-w-xs focus:max-w-none pl-8" placeholder="Search" />
        <div className="h-full absolute top-0 left-0 flex items-center pl-2 pr-1 pointer-events-none">
          <Icon icon="search-medium" className="w-5 text-bold" />
        </div>
      </div>
    </div>
  );
};
