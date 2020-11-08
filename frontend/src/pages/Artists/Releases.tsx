import * as React from 'react';

import { usePagination, useViewOptions } from 'src/hooks';

import { PagedReleases } from 'src/components/Releases';
import { Pagination } from 'src/components/Pagination';
import { ViewSettings } from 'src/components/ViewSettings';
import { fetchReleases } from 'src/lib';

export const ArtistReleases: React.FC<{ active: number }> = ({ active }) => {
  const viewOptionsSeed = React.useMemo(() => {
    return { artistIds: [active] };
  }, [active]);

  const viewOptions = useViewOptions(viewOptionsSeed);
  const pagination = usePagination();

  const { status, data } = fetchReleases(viewOptions, pagination);
  const { total, results } = React.useMemo(
    () => (data && status === 'success' ? data.releases : { total: 0, results: [] }),
    [status, data],
  );

  React.useEffect(() => {
    if (total) pagination.setTotal(total);
  }, [pagination, total]);

  if (total === 0) return null;

  return (
    <div>
      <ViewSettings className="my-4" viewOptions={viewOptions} pagination={pagination} partial />
      <PagedReleases view={viewOptions.releaseView} releases={results} partial />
      <Pagination className="my-4" pagination={pagination} />
    </div>
  );
};
