import * as React from 'react';

import { ArtistChooser, ArtistSelector } from 'src/components/Picker';
import { usePagination, useViewOptions } from 'src/hooks';

import { PagedReleases } from 'src/components/Releases';
import { Pagination } from 'src/components/Pagination';
import { SidebarContext } from 'src/contexts';
import { ViewSettings } from 'src/components/ViewSettings';
import { fetchReleases } from 'src/lib';
import { useToasts } from 'react-toast-notifications';

export const Artists: React.FC = () => {
  const viewOptions = useViewOptions();
  const pagination = usePagination();
  const { addToast } = useToasts();
  const { openBar } = React.useContext(SidebarContext);

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

  const bp = React.useMemo(() => (openBar ? 'lg' : 'md'), [openBar]);

  return (
    <div className={`flex-1 w-full px-8 flex flex-col ${bp}:flex-row`}>
      <ArtistChooser className={`flex-none mr-4 hidden ${bp}:block`} viewOptions={viewOptions} />
      <ArtistSelector className={`flex-none ${bp}:hidden`} viewOptions={viewOptions} />
      {viewOptions.artistIds.length !== 0 && (
        <div className="py-4 flex-1 overflow-x-hidden">
          <ViewSettings
            className="my-4"
            viewOptions={viewOptions}
            pagination={pagination}
            partial
          />
          <PagedReleases view={viewOptions.releaseView} releases={results} partial />
          <Pagination className="my-4" pagination={pagination} />
        </div>
      )}
    </div>
  );
};
