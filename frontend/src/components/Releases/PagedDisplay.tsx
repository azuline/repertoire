import * as React from 'react';
import clsx from 'clsx';

import { ArtRelease, RowRelease } from 'src/components/Release';
import { ReleaseT, ReleaseView } from 'src/types';

const fullGridCss =
  'grid-cols-2 sm:grid-cols-3 md:grid-cols-4 lg:grid-cols-5 xl:grid-cols-6 2xl:grid-cols-7';
const partialGridCss = 'grid-cols-2 md:grid-cols-3 lg:grid-cols-4 xl:grid-cols-5 2xl:grid-cols-6';

export const PagedReleases: React.FC<{
  releases: ReleaseT[];
  view: ReleaseView;
  partial?: boolean;
}> = ({ releases, view, partial = false }) => {
  switch (view) {
    case ReleaseView.ROW:
      return (
        <div className="flex divide-y-2 divide-bg-embellish flex-col bg-bg">
          {releases.map((rls) => (
            <div key={rls.id}>
              <RowRelease release={rls} className="px-4 py-4 rounded" />
            </div>
          ))}
        </div>
      );
    case ReleaseView.ARTWORK:
    default:
      return (
        <div className={clsx('grid gap-6', partial ? partialGridCss : fullGridCss)}>
          {releases.map((rls) => (
            <ArtRelease key={rls.id} release={rls} />
          ))}
        </div>
      );
  }
};
