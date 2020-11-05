import * as React from 'react';

import { PCType, RVOCType } from 'src/hooks';

import { Order } from './Order';
import { Pagination } from 'src/components/Pagination';
import { PerPage } from './PerPage';
import { Sort } from './Sort';
import { View } from './View';
import clsx from 'clsx';

// TODO: At a certain breakpoint, turn the selects into an "Options <chevron>" popover.

export const ViewSettings: React.FC<{
  viewOptions: RVOCType;
  pagination: PCType;
  className?: string;
}> = ({ viewOptions, pagination, className = '' }) => {
  return (
    <div className={clsx('flex my-4', className)}>
      <Pagination pagination={pagination} />
      <div className="flex ml-auto">
        <View viewOptions={viewOptions} />
        <Sort className="ml-2" viewOptions={viewOptions} />
        <Order className="ml-2" viewOptions={viewOptions} />
        <PerPage className="ml-2" pagination={pagination} />
      </div>
    </div>
  );
};
