import * as React from 'react';

import { usePagination, useViewOptions } from 'src/hooks';

import { Header } from 'src/components/Header';
import { PagedReleases } from 'src/components/Releases';

const paginationOpts = { useUrl: true };

export const Releases: React.FC = (): React.ReactElement => {
  const viewOptions = useViewOptions();
  const pagination = usePagination(paginationOpts);

  return (
    <div className="flex flex-col full">
      <Header />
      <div className="min-h-0 flex flex-col mt-4">
        <div className="overflow-y-auto">
          <PagedReleases className="px-8 pb-8" viewOptions={viewOptions} pagination={pagination} />
        </div>
      </div>
    </div>
  );
};
