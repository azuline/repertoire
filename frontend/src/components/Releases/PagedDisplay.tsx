import clsx from 'clsx';
import * as React from 'react';
import { Pagination } from 'src/components/Pagination';
import { ArtRelease, RowRelease } from 'src/components/Release';
import { ViewSettings } from 'src/components/ViewSettings';
import { SidebarContext } from 'src/contexts';
import { PaginationT, ViewOptionsT } from 'src/hooks';
import { searchReleases } from 'src/lib';
import { ReleaseView } from 'src/types';

// Partial here means that we have an artist/collection selector open.

// prettier-ignore
const gridFullCss = 'grid-cols-2 sm:grid-cols-3 md:grid-cols-4 lg:grid-cols-5 xl:grid-cols-6 2xl:grid-cols-7';
// prettier-ignore
const gridOneCssSidebar = 'grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 xl:grid-cols-5 2xl:grid-cols-6';
// prettier-ignore
const gridOneCssPartial = 'grid-cols-2 sm:grid-cols-3 md:grid-cols-4 lg:grid-cols-4 xl:grid-cols-5 2xl:grid-cols-6';
// prettier-ignore
const gridTwoCss = 'grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 xl:grid-cols-4 2xl:grid-cols-5';

export const PagedReleases: React.FC<{
  viewOptions: ViewOptionsT;
  pagination: PaginationT;
  partial?: boolean;
}> = ({ viewOptions, pagination, partial = false }) => {
  const { isSidebarOpen } = React.useContext(SidebarContext);

  const { status, data } = searchReleases(viewOptions, pagination);

  const { total, results } = React.useMemo(
    () => (data && status === 'success' ? data.releases : { total: 0, results: [] }),
    [status, data],
  );

  React.useEffect(() => {
    if (total) pagination.setTotal(total);
  }, [total]);

  const gridCss = React.useMemo(() => {
    if (isSidebarOpen && partial) {
      return gridTwoCss;
    }
    if (isSidebarOpen) {
      return gridOneCssSidebar;
    }
    if (partial) {
      return gridOneCssPartial;
    }
    return gridFullCss;
  }, [isSidebarOpen, partial]);

  let releasesDiv = null;

  switch (viewOptions.releaseView) {
    case ReleaseView.ROW:
      releasesDiv = (
        <div className="flex flex-col divide-y-2 divide-primary-alt2 bg-background">
          {results.map((rls) => (
            <div key={rls.id}>
              <RowRelease release={rls} className="px-4 py-4 rounded" />
            </div>
          ))}
        </div>
      );
      break;
    case ReleaseView.ARTWORK:
    default:
      releasesDiv = (
        <div className={clsx('grid gap-6', gridCss)}>
          {results.map((rls) => (
            <ArtRelease key={rls.id} release={rls} />
          ))}
        </div>
      );
  }

  return (
    <>
      <ViewSettings className="mb-4" viewOptions={viewOptions} pagination={pagination} />
      {releasesDiv}
      <Pagination className="mt-4" pagination={pagination} />
    </>
  );
};
