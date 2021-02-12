import clsx from 'clsx';
import * as React from 'react';

import { Icon, Popover } from '~/components/common';
import { Pagination } from '~/components/Pagination';
import { IPagination, IViewOptions } from '~/hooks';

import { Order } from './Order';
import { PerPage } from './PerPage';
import { Sort } from './Sort';
import { View } from './View';

export const ViewSettings: React.FC<{
  viewOptions: IViewOptions;
  pagination: IPagination;
  className?: string;
  partial?: boolean;
}> = ({ viewOptions, pagination, className, partial = false }) => {
  const responsiveFlex = partial ? '2xl:flex' : 'xl:flex';
  const responsiveHide = partial ? '2xl:hidden' : 'xl:hidden';

  return (
    <div className={clsx('flex', className)}>
      <Pagination pagination={pagination} />
      <div className={clsx('hidden ml-auto', responsiveFlex)}>
        <View viewOptions={viewOptions} />
        <Sort className="ml-2" viewOptions={viewOptions} />
        <Order className="ml-2" viewOptions={viewOptions} />
        <PerPage className="ml-2" pagination={pagination} />
      </div>
      <Popover click className={clsx('ml-auto -mr-2', responsiveHide)}>
        <button className="flex items-center small-btn text-btn" type="button">
          <div>Options</div>
          <Icon className="w-4 ml-1 -mr-0.5" icon="chevron-down-small" />
        </button>
        <div>
          <View viewOptions={viewOptions} />
          <Sort viewOptions={viewOptions} />
          <Order viewOptions={viewOptions} />
          <PerPage pagination={pagination} />
        </div>
      </Popover>
    </div>
  );
};
