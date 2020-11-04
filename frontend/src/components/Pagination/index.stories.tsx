import * as React from 'react';

import { Pagination } from '.';
import { Story } from '@storybook/react/types-6-0';
import { usePagination } from 'src/hooks';

export default {
  title: 'Pagination',
  component: Pagination,
};

type Args = {
  curPage: number;
  perPage: number;
  total: number;
  popperPlacement: string;
};

const Template: Story<Args> = ({ curPage, perPage, total, popperPlacement }) => {
  const pagination = usePagination();

  pagination.setCurPage(curPage);
  pagination.setPerPage(perPage);
  pagination.setTotal(total);

  return <Pagination pagination={pagination} popperPlacement={popperPlacement} />;
};

const generate = (
  curPage: number,
  total: number,
  popperPlacement = 'bottom-center',
): React.ReactNode => {
  const idk = Template.bind({});
  idk.args = { curPage, total, perPage: 10, popperPlacement };
  return idk;
};

export const NoPages = generate(1, 0);
export const OnePage = generate(1, 5);
export const TwoPages = generate(1, 15);
export const ThreePages = generate(1, 25);
export const FourPages = generate(1, 35);
export const FivePages = generate(1, 45);
export const SevenPages = generate(1, 65);
export const TenPages = generate(1, 95);
