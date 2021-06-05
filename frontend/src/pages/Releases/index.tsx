import * as React from 'react';

import { PagedReleases } from '~/components';
import { usePagination, useViewOptions } from '~/hooks';
import { Layout } from '~/layout';

const paginationOpts = { useUrl: true };

export const Releases: React.FC = () => {
  const viewOptions = useViewOptions();
  const pagination = usePagination(paginationOpts);

  return (
    <Layout padX padY scroll>
      <PagedReleases pagination={pagination} viewOptions={viewOptions} />
    </Layout>
  );
};
