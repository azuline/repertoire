import * as React from 'react';
import clsx from 'clsx';
import { RVOCType, PCType } from 'src/hooks';
import { Sort } from './Sort';
import { Order } from './Order';
import { PerPage } from './PerPage';

export const ViewSettings: React.FC<{
  viewOptions: RVOCType;
  pagination: PCType;
  className?: string;
}> = ({ viewOptions, pagination, className = '' }) => {
  return (
    <div className={clsx('flex justify-center', className)}>
      <Sort viewOptions={viewOptions} />
      <Order className="ml-4" viewOptions={viewOptions} />
      <PerPage className="ml-4" pagination={pagination} />
    </div>
  );
};
