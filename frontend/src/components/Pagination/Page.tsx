import * as React from 'react';
import tw from 'twin.macro';

import { TextButton } from '../common/Button';

export const Page: React.FC<{
  page: number;
  curPage: number;
  setCurPage: (arg0: number) => void;
  className?: string;
}> = ({ page, curPage, setCurPage, className }) => (
  <TextButton
    className={className}
    css={[
      page === curPage ? tw`font-bold text-primary-500` : tw`text-black dark:text-white`,
      tw`p-1 rounded-none`,
    ]}
    type="button"
    onClick={(): void => setCurPage(page)}
  >
    {page}
  </TextButton>
);
