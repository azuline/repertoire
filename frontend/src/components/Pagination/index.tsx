import * as React from 'react';
import { PaginationContext } from 'src/contexts';
import clsx from 'clsx';
import { Page } from './Page';
import { Skip } from './Skip';
import { Placement } from '@popperjs/core';

export const Pagination: React.FC<{
  popperPlacement?: Placement;
  className?: string;
}> = ({ popperPlacement = 'bottom', className = '' }) => {
  const { curPage, setCurPage, numPages } = React.useContext(PaginationContext);

  React.useEffect(() => {
    if (curPage > numPages) setCurPage(1);
  }, [curPage, numPages, setCurPage]);

  const bottom = React.useMemo(() => Math.max(curPage - 2, 2), [curPage]);
  const top = React.useMemo(() => Math.min(curPage + 3, numPages), [curPage, numPages]);

  if (numPages === 0) {
    return null;
  }

  return (
    <div className={clsx(className, 'flex btn-group')}>
      <Page page={1} />
      {bottom !== 2 && <Skip popperPlacement={popperPlacement} />}
      {Array.from({ length: top - bottom }).map((_, i) => (
        <Page key={bottom + i} page={bottom + i} />
      ))}
      {top !== numPages && <Skip popperPlacement={popperPlacement} />}
      {numPages > 1 && <Page page={numPages} />}
    </div>
  );
};
