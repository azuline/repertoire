import * as React from 'react';

import { Icon } from 'src/components/common/Icon';
import clsx from 'clsx';

// TODO: Implement a dropdown and stuff...

export const Searchbar: React.FC<{
  className?: string | undefined;
  shrink?: boolean;
}> = ({ className, shrink = true }) => {
  return (
    <div className={clsx(className, 'flex-1')}>
      <div className="flex items-center h-full">
        <div className="relative ml-auto">
          <input
            className={clsx('w-full pl-9', shrink && 'max-w-xs focus:max-w-none')}
            placeholder="Search"
          />
          <div className="h-full absolute top-0 left-0 flex items-center pl-2 pr-1 pointer-events-none">
            <Icon icon="search-medium" className="w-5 text-primary" />
          </div>
        </div>
      </div>
    </div>
  );
};
