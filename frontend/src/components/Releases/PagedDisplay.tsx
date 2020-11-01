import * as React from 'react';
import { ArtRelease } from 'src/components/Release';
import { ReleaseT } from 'src/types';

export const PagedReleases: React.FC<{ releases: ReleaseT[] }> = ({ releases }) => {
  return (
    <div className="grid">
      {releases.map((rls) => (
        <ArtRelease key={rls.id} release={rls} />
      ))}
    </div>
  );
};
