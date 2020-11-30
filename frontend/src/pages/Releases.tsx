import * as React from 'react';
import { Header, PagedReleases } from 'src/components';
import { usePagination, useViewOptions } from 'src/hooks';

const paginationOpts = { useUrl: true };

export const Releases: React.FC = (): React.ReactElement => {
  const viewOptions = useViewOptions();
  const pagination = usePagination(paginationOpts);

  return (
    <>
      <Header />
      <div className="px-8 pt-4">
        <PagedReleases pagination={pagination} viewOptions={viewOptions} />
      </div>
    </>
  );
};
