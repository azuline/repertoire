import * as React from 'react';

import { ArtRelease } from 'src/components/Release';
import { ReleaseT } from 'src/types';

export const PagedReleases: React.FC<{ releases: ReleaseT[] }> = ({ releases }) => {
  return (
    <div className="grid gap-6 grid-cols-2 md:grid-cols-3 lg:grid-cols-4 xl:grid-cols-5 2xl:grid-cols-6">
      {releases.map((rls) => (
        <ArtRelease key={rls.id} release={rls} />
      ))}
    </div>
  );
};
