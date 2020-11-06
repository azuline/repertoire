import * as React from 'react';

import { ArtRelease, RowRelease } from 'src/components/Release';
import { ReleaseT, ReleaseView } from 'src/types';

import clsx from 'clsx';

export const PagedReleases: React.FC<{ releases: ReleaseT[]; view: ReleaseView }> = ({
  releases,
  view,
}) => {
  switch (view) {
    case ReleaseView.ROW:
      return (
        <div className="flex flex-col bg-bg rounded round-children">
          {releases.map((rls, i) => (
            <RowRelease
              key={rls.id}
              release={rls}
              className={clsx('px-4 bg-white', i % 2 === 1 ? 'bg-opacity-2' : 'bg-opacity-4')}
            />
          ))}
        </div>
      );
    case ReleaseView.ARTWORK:
    default:
      return (
        <div className="grid gap-6 grid-cols-2 sm:grid-cols-3 md:grid-cols-4 lg:grid-cols-5 xl:grid-cols-6 2xl:grid-cols-7">
          {releases.map((rls) => (
            <ArtRelease key={rls.id} release={rls} />
          ))}
        </div>
      );
  }
};
