import * as React from 'react';

import { ArtRelease, RowRelease } from 'src/components/Release';
import { ReleaseT, ReleaseView } from 'src/types';

const components = {
  [ReleaseView.ARTWORK]: ArtRelease,
  [ReleaseView.ROW]: RowRelease,
};

export const PagedReleases: React.FC<{ releases: ReleaseT[]; view: ReleaseView }> = ({
  releases,
  view,
}) => {
  const ReleaseComponent = React.useMemo(() => components[view], [view]);

  return (
    <div className="grid gap-6 grid-cols-2 md:grid-cols-3 lg:grid-cols-4 xl:grid-cols-5 2xl:grid-cols-6">
      {releases.map((rls) => (
        <ReleaseComponent key={rls.id} release={rls} />
      ))}
    </div>
  );
};
