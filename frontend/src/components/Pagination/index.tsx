import clsx from 'clsx';
import * as React from 'react';

import { IPagination } from '~/hooks';

import { Arrow } from './Arrow';
import { Goto } from './Goto';
import { Page } from './Page';

export const Pagination: React.FC<{
  pagination: IPagination;
  className?: string;
}> = ({ pagination: { curPage, setCurPage, numPages }, className }) => {
  const bottom = Math.max(curPage - 2, 2);
  const top = Math.min(curPage + 3, numPages);

  const goBackOnePage = (): void => setCurPage((page) => Math.min(Math.max(1, page - 1), numPages));
  const goForwardOnePage = (): void =>
    setCurPage((page) => Math.min(Math.max(1, page + 1), numPages));

  // If there are no pages, don't render pagination.
  if (numPages <= 1) return null;

  return (
    <div className={clsx(className, 'flex items-center -ml-1')}>
      {numPages > 1 && <Arrow direction="left" onClick={goBackOnePage} />}
      <Page curPage={curPage} page={1} setCurPage={setCurPage} />
      {Array.from({ length: top - bottom }).map((_, i) => (
        <Page key={bottom + i} curPage={curPage} page={bottom + i} setCurPage={setCurPage} />
      ))}
      {numPages > 1 && <Page curPage={curPage} page={numPages} setCurPage={setCurPage} />}
      {numPages > 1 && <Arrow direction="right" onClick={goForwardOnePage} />}
      {numPages > 4 && <Goto numPages={numPages} setCurPage={setCurPage} />}
    </div>
  );
};
