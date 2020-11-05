import * as React from 'react';

import { Goto } from './Goto';
import { PCType } from 'src/hooks';
import { Page } from './Page';
import clsx from 'clsx';

export const Pagination: React.FC<{
  pagination: PCType;
  className?: string;
}> = ({ pagination: { curPage, setCurPage, numPages }, className = '' }) => {
  React.useEffect(() => {
    if (curPage > numPages) setCurPage(1);
  }, [curPage, numPages, setCurPage]);

  const bottom = React.useMemo(() => Math.max(curPage - 2, 2), [curPage]);
  const top = React.useMemo(() => Math.min(curPage + 3, numPages), [curPage, numPages]);

  // If there are no pages, don't render pagination.
  if (numPages === 0) return null;

  return (
    <div className={clsx(className, 'flex')}>
      <Page page={1} curPage={curPage} setCurPage={setCurPage} />
      {Array.from({ length: top - bottom }).map((_, i) => (
        <Page key={bottom + i} page={bottom + i} curPage={curPage} setCurPage={setCurPage} />
      ))}
      {numPages > 1 && <Page page={numPages} curPage={curPage} setCurPage={setCurPage} />}
      {numPages > 4 && <Goto setCurPage={setCurPage} numPages={numPages} />}
    </div>
  );
};
