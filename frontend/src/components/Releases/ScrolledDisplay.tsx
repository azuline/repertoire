import * as React from 'react';
import { ReleaseT } from 'src/types';
import { ArtRelease } from 'src/components/Release';

export const ScrolledReleases: React.FC<{ releases: ReleaseT[] }> = ({ releases }) => {
  return (
    <div className="whitespace-no-wrap w-full overflow-x-auto pb-2">
      {releases.map((rls) => (
        <ArtRelease key={rls.id} className="inline-block w-48 mr-4" release={rls} />
      ))}
    </div>
  );
};
