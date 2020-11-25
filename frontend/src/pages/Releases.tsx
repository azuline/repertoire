import * as React from 'react';

import { Header, PagedReleases } from 'src/components';
import { usePagination, useViewOptions } from 'src/hooks';

const paginationOpts = { useUrl: true };

export const Releases: React.FC = (): React.ReactElement => {
  const viewOptions = useViewOptions();
  const pagination = usePagination(paginationOpts);

  return (
    <div className="flex flex-col full">
      <Header />
      <div className="min-h-0 flex flex-col mt-4">
        <div className="px-8 overflow-y-auto">
          <div className="pb-8">
            <PagedReleases viewOptions={viewOptions} pagination={pagination} />
          </div>
        </div>
      </div>
    </div>
  );
};
