import * as React from 'react';

import { usePagination, useViewOptions } from 'src/hooks';

import { PagedReleases } from 'src/components/Releases';
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
    <div className="min-h-0 flex flex-col">
      <ViewSettings className="px-8 my-4" viewOptions={viewOptions} pagination={pagination} />
      <div className="overflow-y-auto">
        <PagedReleases className="px-8 pb-8" view={viewOptions.releaseView} releases={results} />
      </div>
    </div>
  );
};
