import * as React from 'react';
import clsx from 'clsx';
import { Page } from './Page';
import { Skip } from './Skip';
import { PCType } from 'src/hooks';

export const Pagination: React.FC<{
  pagination: PCType;
  popperPlacement?: string;
  className?: string;
}> = ({
  pagination: { curPage, setCurPage, numPages },
  popperPlacement = 'bottom-center',
  className = '',
}) => {
  React.useEffect(() => {
    if (curPage > numPages) setCurPage(1);
  }, [curPage, numPages, setCurPage]);

  const bottom = React.useMemo(() => Math.max(curPage - 2, 2), [curPage]);
  const top = React.useMemo(() => Math.min(curPage + 3, numPages), [curPage, numPages]);

  // If there are no pages, don't render pagination.
  if (numPages === 0) return null;

  return (
    <div className={clsx(className, 'flex btn-group justify-center mx-auto my-4')}>
      <Page page={1} curPage={curPage} setCurPage={setCurPage} />
      {bottom !== 2 && (
        <Skip popperPlacement={popperPlacement} setCurPage={setCurPage} numPages={numPages} />
      )}
      {Array.from({ length: top - bottom }).map((_, i) => (
        <Page key={bottom + i} page={bottom + i} curPage={curPage} setCurPage={setCurPage} />
      ))}
      {top !== numPages && (
        <Skip popperPlacement={popperPlacement} setCurPage={setCurPage} numPages={numPages} />
      )}
      {numPages > 1 && <Page page={numPages} curPage={curPage} setCurPage={setCurPage} />}
    </div>
  );
};
