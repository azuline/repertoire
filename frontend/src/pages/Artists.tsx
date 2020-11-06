import * as React from 'react';
import clsx from 'clsx';

import { usePagination, useViewOptions } from 'src/hooks';

import { PagedReleases } from 'src/components/Releases';
import { Pagination } from 'src/components/Pagination';
import { ReleaseView } from 'src/types';
import { ViewSettings } from 'src/components/ViewSettings';
import { fetchReleases } from 'src/lib';
import { useToasts } from 'react-toast-notifications';
import { ChooseArtist } from 'src/components/ChooseArtist';

const chooseStyle = { maxHeight: 'calc(100vh - 4rem)' };

export const Artists: React.FC = (): React.ReactElement => {
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
    <div className="flex-1 bg-bg w-full border-t-2 border-bg-embellish flex">
      <ChooseArtist
        className="rpr--chooser sticky mt-4 pt-4 top-0 w-48 flex-none overflow-y-auto"
        style={chooseStyle}
        viewOptions={viewOptions}
      />
      <div
        className={clsx(
          'py-4 px-1/24 flex-1',
          viewOptions.releaseView === ReleaseView.ROW ? 'max-w-6xl' : '',
        )}
      >
        <ViewSettings className="my-4" viewOptions={viewOptions} pagination={pagination} partial />
        <PagedReleases view={viewOptions.releaseView} releases={results} partial />
        <Pagination className="my-4" pagination={pagination} />
      </div>
    </div>
  );
};
