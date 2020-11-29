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
  const { total, results } = React.useMemo(
    () => (data?.releases || { total: 0, results: [] }),
    [data],
  );

  React.useEffect(() => {
    if (total) pagination.setTotal(total);
  }, [total]);

  const releasesDiv = React.useMemo(() => {
    switch (viewOptions.releaseView) {
      case ReleaseView.ROW:
        return (
          <div className="flex flex-col divide-y-2 divide-primary-alt23">
            {results.map((rls) => (
              <div key={rls.id}>
                <RowRelease release={rls} className="px-4 py-4 rounded" />
              </div>
            ))}
          </div>
        );
      case ReleaseView.ARTWORK:
      default:
        return (
          <div className={clsx('grid gap-6', calculateGridCss(isSidebarOpen, partial))}>
            {results.map((rls) => (
              <ArtRelease key={rls.id} release={rls} />
            ))}
          </div>
        );
    }
  }, [viewOptions, results, isSidebarOpen, partial]);

  return (
    <>
      <ViewSettings
        className="mb-4"
        viewOptions={viewOptions}
        pagination={pagination}
        partial={partial}
      />
      {releasesDiv}
      <Pagination className="mt-4" pagination={pagination} />
    </>
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
