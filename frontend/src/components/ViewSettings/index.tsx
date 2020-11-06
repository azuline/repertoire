import * as React from 'react';

import { PCType, RVOCType } from 'src/hooks';

import { Popover } from 'src/components/common/Popover';
import { Icon } from 'src/components/common/Icon';
import { Order } from './Order';
import { Pagination } from 'src/components/Pagination';
import { PerPage } from './PerPage';
import { Sort } from './Sort';
import { View } from './View';
import clsx from 'clsx';

export const ViewSettings: React.FC<{
  viewOptions: RVOCType;
  pagination: PCType;
  className?: string;
  partial?: boolean;
}> = ({ viewOptions, pagination, className = '', partial = false }) => {
  return (
    <div className={clsx('flex', className)}>
      <Pagination pagination={pagination} />
      <div className={clsx('hidden ml-auto', partial ? 'lg:flex' : 'md:flex')}>
        <View viewOptions={viewOptions} />
        <Sort className="ml-2" viewOptions={viewOptions} />
        <Order className="ml-2" viewOptions={viewOptions} />
        <PerPage className="ml-2" pagination={pagination} />
      </div>
      <Popover
        click
        className={clsx('ml-auto cursor-pointer', partial ? 'lg:hidden' : 'md:hidden')}
      >
        <div className="flex items-center">
          <div>Options</div>
          <Icon className="text-bold w-4 ml-1" icon="chevron-down-small" />
        </div>
        <div className="px-4 py-2 bg-bg-alt border-highlight border-2 rounded">
          <View viewOptions={viewOptions} />
          <Sort viewOptions={viewOptions} />
          <Order viewOptions={viewOptions} />
          <PerPage pagination={pagination} />
        </div>
      </Popover>
    </div>
  );
};
