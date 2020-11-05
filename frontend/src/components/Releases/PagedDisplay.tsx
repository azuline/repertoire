import * as React from 'react';

import { ArtRelease, RowRelease } from 'src/components/Release';
import { ReleaseT, ReleaseView } from 'src/types';

export const PagedReleases: React.FC<{ releases: ReleaseT[]; view: ReleaseView }> = ({
  releases,
  view,
}) => {
  switch (view) {
    case ReleaseView.ROW:
      return (
        <div className="flex flex-col divide-y divide-highlight">
          {releases.map((rls) => (
            <RowRelease key={rls.id} release={rls} />
          ))}
        </div>
      );
    case ReleaseView.ARTWORK:
    default:
      return (
        <div className="grid gap-6 grid-cols-2 md:grid-cols-3 lg:grid-cols-4 xl:grid-cols-5 2xl:grid-cols-6">
          {releases.map((rls) => (
            <ArtRelease key={rls.id} release={rls} />
          ))}
        </div>
      );
  }
};
