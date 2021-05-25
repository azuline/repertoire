import * as React from 'react';
import tw from 'twin.macro';

import { Button } from '~/components/common';

type IPage = React.FC<{
  page: number;
  curPage: number;
  setCurPage: React.Dispatch<React.SetStateAction<number>>;
  className?: string;
}>;

export const Page: IPage = ({ page, curPage, setCurPage, className }) => (
  <Button
    text
    className={className}
    css={[
      page === curPage
        ? tw`font-bold text-primary-500`
        : tw`text-black dark:text-white`,
      tw`p-1 rounded-none`,
    ]}
    type="button"
    onClick={(): void => setCurPage(page)}
  >
    {page}
  </Button>
);
