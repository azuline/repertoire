import * as React from 'react';
import { Story } from '@storybook/react/types-6-0';

import { Pagination } from '.';
import { PaginationContext, PaginationProvider } from 'src/contexts';
import { Placement } from '@popperjs/core';

export default {
  title: 'Pagination',
  component: Pagination,
};

type Args = {
  curPage: number;
  perPage: number;
  total: number;
  props: React.ComponentProps<typeof Pagination>;
};

const Template: Story<Args> = (args) => (
  <PaginationProvider>
    <Wrapper {...args} />
  </PaginationProvider>
);

const Wrapper: React.FC<Args> = ({ curPage, perPage, total, props }) => {
  const { setCurPage, setPerPage, setTotal } = React.useContext(PaginationContext);

  setCurPage(curPage);
  setPerPage(perPage);
  setTotal(total);

  return <Pagination {...props} />;
};

const generate = (
  curPage: number,
  total: number,
  popperPlacement: Placement = 'bottom',
): React.ReactNode => {
  const idk = Template.bind({});
  idk.args = { curPage, total, perPage: 10, props: { popperPlacement } };
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
