import * as React from 'react';
import clsx from 'clsx';

export const defaultTheme = 'bg-white';

export const Page: React.FC<{
  page: number;
  curPage: number;
  setCurPage: (arg0: number) => void;
  className?: string;
}> = ({ page, curPage, setCurPage, className = '' }) => {
  const onClick = React.useCallback(() => setCurPage(page), [page, setCurPage]);

  // prettier-ignore
  const theme = React.useMemo(
    () => (page === curPage ? 'bg-blue-400' : defaultTheme),
    [page, curPage],
  );

  return (
    <button
      className={clsx(className, theme, 'border-gray-400 square-btn p-2 border-2')}
      onClick={onClick}
    >
      {page}
    </button>
  );
};
