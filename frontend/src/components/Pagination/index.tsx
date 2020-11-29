import clsx from 'clsx';
import * as React from 'react';
import { PaginationT } from 'src/hooks';

import { Arrow } from './Arrow';
import { Goto } from './Goto';
import { Page } from './Page';

export const Pagination: React.FC<{
  pagination: PaginationT;
  className?: string;
}> = ({ pagination: { curPage, setCurPage, numPages }, className }) => {
  const bottom = React.useMemo(() => Math.max(curPage - 2, 2), [curPage]);
  const top = React.useMemo(() => Math.min(curPage + 3, numPages), [curPage, numPages]);

  const goBackOnePage = React.useCallback(
    () => setCurPage((page) => Math.min(Math.max(1, page - 1), numPages)),
    [numPages, setCurPage],
  );
  const goForwardOnePage = React.useCallback(
    () => setCurPage((page) => Math.min(Math.max(1, page + 1), numPages)),
    [numPages, setCurPage],
  );

  // If there are no pages, don't render pagination.
  if (numPages <= 1) return null;

  return (
    <div className={clsx(className, 'flex items-center')}>
      {numPages > 1 && <Arrow direction="left" onClick={goBackOnePage} />}
      <Page page={1} curPage={curPage} setCurPage={setCurPage} />
      {Array.from({ length: top - bottom }).map((_, i) => (
        <Page key={bottom + i} page={bottom + i} curPage={curPage} setCurPage={setCurPage} />
      ))}
      {numPages > 1 && <Page page={numPages} curPage={curPage} setCurPage={setCurPage} />}
      {numPages > 1 && <Arrow direction="right" onClick={goForwardOnePage} />}
      {numPages > 4 && <Goto setCurPage={setCurPage} numPages={numPages} />}
    </div>
  );
};
