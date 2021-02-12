import clsx from 'clsx';
import * as React from 'react';

import { Icon } from '~/components/common';

// TODO: Implement a dropdown and stuff... get a way to monitor searchbar focus in react
// and use that for width/whatnot.

export const Searchbar: React.FC<{
  className?: string;
  shrink?: boolean;
}> = ({ className, shrink = true }) => (
  <div className={clsx(className, 'flex-1')}>
    <div className="relative flex items-center h-full">
      <input
        className={clsx('w-full pl-9 searchbar', shrink && 'max-w-xs focus:max-w-none')}
        placeholder="Search"
      />
      <div className="absolute top-0 left-0 flex items-center h-full pl-2 pr-1 pointer-events-none">
        <Icon className="w-5 text-primary-400" icon="search-medium" />
      </div>
    </div>
  </div>
);
