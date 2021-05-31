import * as React from 'react';

import { PagedReleases } from '~/components';
import { usePagination, useViewOptions } from '~/hooks';

const paginationOpts = { useUrl: true };

export const Releases: React.FC = () => {
  const viewOptions = useViewOptions();
  const pagination = usePagination(paginationOpts);

  return (
    <div tw="pt-4">
      <PagedReleases pagination={pagination} viewOptions={viewOptions} />
    </div>
  );
};
