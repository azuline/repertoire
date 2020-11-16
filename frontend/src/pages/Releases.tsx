import * as React from 'react';

import { usePagination, useViewOptions } from 'src/hooks';

import { PagedReleases } from 'src/components/Releases';
import { Pagination } from 'src/components/Pagination';
import { ViewSettings } from 'src/components/ViewSettings';
import { fetchReleases } from 'src/lib';

export const Releases: React.FC = (): React.ReactElement => {
  const viewOptions = useViewOptions();
  const pagination = usePagination({ useUrl: true });

  const { status, data } = fetchReleases(viewOptions, pagination);

  const { total, results } = React.useMemo(
    () => (data && status === 'success' ? data.releases : { total: 0, results: [] }),
    [status, data],
  );

  React.useEffect(() => {
    if (total) pagination.setTotal(total);
  }, [total]);

  return (
    <div className="py-4 full flex-1">
      <div className="mx-auto px-8 lg:px-12">
        <ViewSettings className="my-4" viewOptions={viewOptions} pagination={pagination} />
        <PagedReleases view={viewOptions.releaseView} releases={results} />
        <Pagination className="my-4" pagination={pagination} />
      </div>
    </div>
  );
};
