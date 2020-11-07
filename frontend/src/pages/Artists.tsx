import * as React from 'react';

import { Icon } from 'src/components/common/Icon';
import { ArtistChooser } from 'src/components/Chooser';
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
  const [active, setActive] = React.useState<number | null>(null);

  const { status, data } = fetchReleases(viewOptions, pagination);
  const { total, results } = React.useMemo(
    () => (data && status === 'success' ? data.releases : { total: 0, results: [] }),
    [status, data],
  );

  React.useEffect(() => viewOptions.setArtistIds(active ? [active] : []), [active]);
  React.useEffect(() => {
    if (active && status === 'loading') addToast('Loading releases...', { appearance: 'info' });
  }, [active, status]);
  React.useEffect(() => {
    if (total) pagination.setTotal(total);
  }, [pagination, total]);

  const bp = React.useMemo(() => (openBar ? 'lg' : 'md'), [openBar]);
  const setInactive = React.useCallback(
    (e) => {
      e.preventDefault();
      setActive(null);
    },
    [setActive],
  );

  return (
    <div className="flex-1 w-full pr-8 flex">
      <ArtistChooser active={active} setActive={setActive} />
      {active && (
        <div className="pl-8 py-4 flex-1 overflow-x-hidden">
          <button className={`${bp}:hidden flex items-center`} onClick={setInactive}>
            <Icon className="w-5 text-bold mr-1" icon="chevron-left-small" />
            <div className="flex-shrink">Back</div>
          </button>
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
