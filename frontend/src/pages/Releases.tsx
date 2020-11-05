import * as React from 'react';
import { TitleContext } from 'src/contexts';

import { usePagination, useViewOptions } from 'src/hooks';

import { PagedReleases } from 'src/components/Releases';
import { Pagination } from 'src/components/Pagination';
import { ViewSettings } from 'src/components/ViewSettings';
import { fetchReleases } from 'src/lib';
import { useToasts } from 'react-toast-notifications';

export const Releases: React.FC = (): React.ReactElement => {
  const viewOptions = useViewOptions();
  const pagination = usePagination();
  const { addToast } = useToasts();
  const { setTitles } = React.useContext(TitleContext);

  React.useEffect(() => setTitles([{ label: 'Releases', url: '/releases' }]), [setTitles]);

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
      <ViewSettings viewOptions={viewOptions} pagination={pagination} />
      <PagedReleases view={viewOptions.releaseView} releases={results} />
      <Pagination className="my-4" pagination={pagination} />
    </>
  );
};
