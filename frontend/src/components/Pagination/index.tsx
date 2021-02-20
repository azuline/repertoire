import * as React from 'react';

import { IPagination } from '~/hooks';

import { Arrow } from './Arrow';
import { Goto } from './Goto';
import { Page } from './Page';

type IPaginationComponent = React.FC<{
  pagination: IPagination;
  className?: string;
}>;

export const Pagination: IPaginationComponent = ({
  pagination: { page, setPage, numPages },
  className,
}) => {
  const bottom = Math.max(page - 2, 2);
  const top = Math.min(page + 3, numPages);

  const goBackOnePage = (): void => setPage((p) => Math.min(Math.max(1, p - 1), numPages));
  const goForwardOnePage = (): void => setPage((p) => Math.min(Math.max(1, p + 1), numPages));

  // If there are no pages, don't render pagination.
  if (numPages <= 1) {
    return null;
  }

  return (
    <div className={className} tw="flex items-center -ml-1">
      {numPages > 1 && <Arrow direction="left" onClick={goBackOnePage} />}
      <Page curPage={page} page={1} setCurPage={setPage} />
      {Array.from({ length: top - bottom }).map((_, i) => (
        <Page key={bottom + i} curPage={page} page={bottom + i} setCurPage={setPage} />
      ))}
      {numPages > 1 && <Page curPage={page} page={numPages} setCurPage={setPage} />}
      {numPages > 1 && <Arrow direction="right" onClick={goForwardOnePage} />}
      {numPages > 4 && <Goto numPages={numPages} setCurPage={setPage} />}
    </div>
  );
};
