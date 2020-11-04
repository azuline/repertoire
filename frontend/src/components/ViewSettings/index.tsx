import * as React from 'react';

import { PCType, RVOCType } from 'src/hooks';

import { Order } from './Order';
import { Pagination } from 'src/components/Pagination';
import { PerPage } from './PerPage';
import { Sort } from './Sort';
import clsx from 'clsx';

export const ViewSettings: React.FC<{
  viewOptions: RVOCType;
  pagination: PCType;
  className?: string;
}> = ({ viewOptions, pagination, className = '' }) => {
  return (
    <div className={clsx('flex my-4', className)}>
      <Pagination pagination={pagination} />
      <div className="flex ml-auto">
        <Sort viewOptions={viewOptions} />
        <Order className="ml-2" viewOptions={viewOptions} />
        <PerPage className="ml-2" pagination={pagination} />
      </div>
    </div>
  );
};
