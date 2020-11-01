import * as React from 'react';
import clsx from 'clsx';
import { PaginationContext } from 'src/contexts';

export const defaultTheme = 'bg-gray-300 border-gray-400';

export const Page: React.FC<{ page: number; className?: string }> = ({ page, className = '' }) => {
  const { curPage, setCurPage } = React.useContext(PaginationContext);

  const onClick = React.useCallback(() => setCurPage(page), [page, setCurPage]);

  const theme = React.useMemo(
    () => (page === curPage ? 'bg-blue-500 border-blue-600' : defaultTheme),
    [page, curPage],
  );

  return (
    <button className={clsx(className, theme, 'square-btn p-2 border-1')} onClick={onClick}>
      {page}
    </button>
  );
};
