import clsx from 'clsx';
import * as React from 'react';
import { Pagination } from 'src/components/Pagination';
import { ArtRelease, RowRelease } from 'src/components/Release';
import { ViewSettings } from 'src/components/ViewSettings';
import { SidebarContext } from 'src/contexts';
import { PaginationT, ViewOptionsT } from 'src/hooks';
import { useSearchReleases } from 'src/lib';
import { ReleaseView } from 'src/types';

// Partial here means that we have an artist/collection selector open.

export const PagedReleases: React.FC<{
  viewOptions: ViewOptionsT;
  pagination: PaginationT;
  partial?: boolean;
}> = ({ viewOptions, pagination, partial = false }) => {
  const { isSidebarOpen } = React.useContext(SidebarContext);
  const { data } = useSearchReleases(viewOptions, pagination);

  // prettier-ignore
  const { total, results } = data?.releases || { results: [], total: 0 };

  React.useEffect(() => {
    if (total) pagination.setTotal(total);
  }, [total, pagination]);

  let releasesDiv = null;

  switch (viewOptions.releaseView) {
    case ReleaseView.ROW:
      releasesDiv = (
        <div className="flex flex-col">
          {results.map((rls) => (
            <div key={rls.id}>
              <RowRelease className="-mx-3 rounded-lg" release={rls} />
            </div>
          ))}
        </div>
      );
      break;
    case ReleaseView.ARTWORK:
      releasesDiv = (
        <div className={clsx('grid gap-4 md:gap-6', calculateGridCss(isSidebarOpen, partial))}>
          {results.map((rls) => (
            <ArtRelease key={rls.id} release={rls} />
          ))}
        </div>
      );
      break;
    default:
  }

  return (
    <div className="pb-8">
      <ViewSettings
        className="mb-6"
        pagination={pagination}
        partial={partial}
        viewOptions={viewOptions}
      />
      {releasesDiv}
      <Pagination className="mt-6" pagination={pagination} />
    </div>
  );
};

const calculateGridCss = (isSidebarOpen: boolean, partial: boolean): string => {
  if (isSidebarOpen && partial) {
    return 'grid-cols-2 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 xl:grid-cols-4 2xl:grid-cols-5';
  }
  if (isSidebarOpen) {
    return 'grid-cols-2 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 xl:grid-cols-5 2xl:grid-cols-6';
  }
  if (partial) {
    return 'grid-cols-2 sm:grid-cols-3 md:grid-cols-4 lg:grid-cols-4 xl:grid-cols-5 2xl:grid-cols-6';
  }
  return 'grid-cols-2 sm:grid-cols-3 md:grid-cols-4 lg:grid-cols-5 xl:grid-cols-6 2xl:grid-cols-7';
};
