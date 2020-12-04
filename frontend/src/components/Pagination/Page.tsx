import clsx from 'clsx';
import * as React from 'react';

export const Page: React.FC<{
  page: number;
  curPage: number;
  setCurPage: (arg0: number) => void;
  className?: string;
}> = ({ page, curPage, setCurPage, className }) => (
  <button
    className={clsx(
      className,
      page === curPage ? 'font-bold text-primary-500' : 'text-black dark:text-white',
      'p-1 text-btn rounded-none',
    )}
    type="button"
    onClick={(): void => setCurPage(page)}
  >
    {page}
  </button>
);
