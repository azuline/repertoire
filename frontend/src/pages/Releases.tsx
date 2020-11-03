import * as React from 'react';
import { PagedReleases } from 'src/components/Releases';
import { Pagination } from 'src/components/Pagination';
import { ViewSettings } from 'src/components/ViewSettings';
import { fetchReleases } from 'src/lib';
import { useViewOptions, usePagination } from 'src/hooks';
import { SectionHeader } from 'src/components/common/SectionHeader';
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
      <Pagination pagination={pagination} />
      <PagedReleases releases={results} />
      <Pagination pagination={pagination} popperPlacement="top" />
    </>
  );
};
