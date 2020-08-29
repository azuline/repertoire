import React, { useContext } from 'react';
import { PaginationContext } from 'contexts';
import { Page } from './Page';
import { DotDotDot } from './DotDotDot';
import './index.scss';

export const Pagination = () => {
  const { page, numPages } = useContext(PaginationContext);

  const bottom = Math.max(page - 2, 2);
  const top = Math.min(page + 2, numPages - 1);

  return (
    <div className="Pagination">
      <Page page={1} />
      {bottom !== 2 && <DotDotDot />}
      {Array.from({ length: top - bottom }).map((_, i) => (
        <Page page={bottom + i} />
      ))}
      {top + 1 !== numPages && <DotDotDot />}
      {numPages > 2 && <Page page={numPages} />}
    </div>
  );
};
