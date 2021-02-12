import clsx from 'clsx';
import * as React from 'react';

import { Pagination } from '~/components/Pagination';
import { ArtRelease, RowRelease } from '~/components/Release';
import { ViewSettings } from '~/components/ViewSettings';
import { PaginationT, ViewOptionsT } from '~/hooks';
import { useSearchReleases } from '~/lib';
import { ReleaseView } from '~/types';

// Partial here means that we have an artist/collection selector open.

export const PagedReleases: React.FC<{
  viewOptions: ViewOptionsT;
  pagination: PaginationT;
  partial?: boolean;
}> = ({ viewOptions, pagination, partial = false }) => {
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
        <div className={clsx('grid gap-4 md:gap-6', calculateGridCss(partial))}>
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

const calculateGridCss = (partial: boolean): string => {
  if (partial) {
    return 'grid-cols-2 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 xl:grid-cols-4 2xl:grid-cols-5';
  }
  return 'grid-cols-2 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 xl:grid-cols-5 2xl:grid-cols-6';
};
