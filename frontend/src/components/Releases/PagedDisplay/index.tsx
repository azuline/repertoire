import * as React from 'react';
import { Pagination } from 'src/components/Pagination';

export const PagedReleases: React.FC = () => {
  return (
    <div>
      <Pagination />
      <div />
      <Pagination position="top" />
    </div>
  );
};
