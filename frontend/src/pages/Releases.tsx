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
      <div className="flex flex-col min-h-0">
        <div className="px-8 pt-4 overflow-y-auto">
          <div className="pb-8">
            <PagedReleases pagination={pagination} viewOptions={viewOptions} />
          </div>
        </div>
      </div>
    </div>
  );
};
