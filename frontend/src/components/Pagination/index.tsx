import * as React from 'react';
import { PaginationContext } from 'src/contexts';
import clsx from 'clsx';
import { Page } from './Page';
import { Skip } from './Skip';
import { PopoverPosition } from 'react-tiny-popover';

export const Pagination: React.FC<{
  position?: PopoverPosition;
  className?: string;
}> = ({ position = 'bottom', className = '' }) => {
  const { curPage, setCurPage, numPages } = React.useContext(PaginationContext);

  React.useEffect(() => {
    if (curPage > numPages) setCurPage(1);
  }, [curPage, numPages, setCurPage]);

  const bottom = React.useMemo(() => Math.max(curPage - 2, 2), [curPage]);
  const top = React.useMemo(() => Math.min(curPage + 3, numPages), [curPage]);

  if (numPages === 0) {
    return null;
  }

  return (
    <div className={clsx(className, 'flex')}>
      <Page page={1} />
      {bottom !== 2 && <Skip position={position} />}
      {Array.from({ length: top - bottom }).map((_, i) => (
        <Page key={bottom + i} page={bottom + i} />
      ))}
      {top !== numPages && <Skip position={position} />}
      {numPages > 1 && <Page page={numPages} />}
    </div>
  );
};
