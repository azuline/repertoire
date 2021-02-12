import * as React from 'react';

import { Header, PagedReleases } from '~/components';
import { usePagination, useViewOptions } from '~/hooks';

const paginationOpts = { useUrl: true };

export const Releases: React.FC = (): React.ReactElement => {
  const viewOptions = useViewOptions();
  const pagination = usePagination(paginationOpts);

  return (
    <>
      <Header />
      <div className="pt-4">
        <PagedReleases pagination={pagination} viewOptions={viewOptions} />
      </div>
    </>
  );
};
