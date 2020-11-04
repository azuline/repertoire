import * as React from 'react';

import { ArtRelease } from 'src/components/Release';
import { ReleaseT } from 'src/types';

export const ScrolledReleases: React.FC<{ releases: ReleaseT[] }> = ({ releases }) => {
  return (
    <div className="flex w-full overflow-x-auto pb-2">
      {releases.map((rls) => (
        <div key={rls.id} className="w-48 flex-shrink-0 mr-4">
          <ArtRelease release={rls} />
        </div>
      ))}
    </div>
  );
};
