import * as React from 'react';
import tw from 'twin.macro';

import { Icon, Popover, TextButton } from '~/components/common';
import { Pagination } from '~/components/Pagination';
import { IPagination, IViewOptions } from '~/hooks';

import { Order } from './Order';
import { PerPage } from './PerPage';
import { Sort } from './Sort';
import { View } from './View';

type IViewSettings = React.FC<{
  viewOptions: IViewOptions;
  pagination: IPagination;
  className?: string;
  partial?: boolean;
}>;

export const ViewSettings: IViewSettings = ({
  viewOptions,
  pagination,
  className,
  partial = false,
}) => {
  const responsiveFlex = partial ? tw`2xl:flex` : tw`xl:flex`;
  const responsiveHide = partial ? tw`2xl:hidden` : tw`xl:hidden`;

  return (
    <div className={className} tw="flex">
      <Pagination pagination={pagination} />
      <div css={[tw`hidden ml-auto`, responsiveFlex]}>
        <View viewOptions={viewOptions} />
        <Sort tw="ml-2" viewOptions={viewOptions} />
        <Order tw="ml-2" viewOptions={viewOptions} />
        <PerPage pagination={pagination} tw="ml-2" />
      </div>
      <div css={[tw`ml-auto -mr-2`, responsiveHide]}>
        <Popover>
          <TextButton tw="flex items-center px-2 py-1" type="button">
            <div>Options</div>
            <Icon icon="chevron-down-small" tw="w-4 ml-1 -mr-0.5" />
          </TextButton>
          <div>
            <View tw="mb-1" viewOptions={viewOptions} />
            <Sort tw="mb-1" viewOptions={viewOptions} />
            <Order tw="mb-1" viewOptions={viewOptions} />
            <PerPage pagination={pagination} />
          </div>
        </Popover>
      </div>
    </div>
  );
};
