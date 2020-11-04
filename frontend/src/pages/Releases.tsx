import * as React from 'react';

import { usePagination, useViewOptions } from 'src/hooks';

import { PagedReleases } from 'src/components/Releases';
import { Pagination } from 'src/components/Pagination';
import { SectionHeader } from 'src/components/common/SectionHeader';
import { ViewSettings } from 'src/components/ViewSettings';
import { fetchReleases } from 'src/lib';
import { useToasts } from 'react-toast-notifications';

export const Releases: React.FC = (): React.ReactElement => {
  const viewOptions = useViewOptions();
  const pagination = usePagination();
  const { addToast } = useToasts();

  const { status, data } = fetchReleases(viewOptions, pagination);

  React.useEffect(() => {
    if (status === 'loading') addToast('Loading releases...', { appearance: 'info' });
  }, [status]);

  const { total, results } = React.useMemo(
    () => (data && status === 'success' ? data.releases : { total: 0, results: [] }),
    [status, data],
  );

  React.useEffect(() => {
    if (total) pagination.setTotal(total);
  }, [pagination, total]);

  return (
    <>
      <SectionHeader>Releases</SectionHeader>
      <ViewSettings viewOptions={viewOptions} pagination={pagination} />
      <PagedReleases releases={results} />
      <Pagination className="my-4" pagination={pagination} />
    </>
  );
};
