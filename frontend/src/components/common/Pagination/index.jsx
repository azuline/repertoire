import './index.scss';

import React, { useContext } from 'react';

import { ControlGroup } from '@blueprintjs/core';
import { DotDotDot } from './DotDotDot';
import { Page } from './Page';
import { PaginationContext } from 'contexts';

export const Pagination = () => {
  const { page, numPages } = useContext(PaginationContext);

  const bottom = Math.max(page - 2, 2);
  const top = Math.min(page + 3, numPages);

  if (numPages === 0) {
    return null;
  }

  return (
    <ControlGroup className="Pagination">
      <Page page={1} />
      {bottom !== 2 && <DotDotDot />}
      {Array.from({ length: top - bottom }).map((_, i) => (
        <Page key={bottom + i} page={bottom + i} />
      ))}
      {top !== numPages && <DotDotDot />}
      {numPages > 2 && <Page page={numPages} />}
    </ControlGroup>
  );
};
