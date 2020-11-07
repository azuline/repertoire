import * as React from 'react';

import { ArtRelease } from 'src/components/Release';
import { ReleaseT } from 'src/types';
import clsx from 'clsx';

export const ScrolledReleases: React.FC<{
  releases: ReleaseT[];
  className?: string | undefined;
}> = ({ releases, className }) => {
  return (
    <div className={clsx(className, 'flex w-full overflow-x-auto')}>
      {releases.map((rls) => (
        <div key={rls.id} className="w-56 h-56 flex-shrink-0 mr-4">
          <ArtRelease release={rls} />
        </div>
      ))}
    </div>
  );
};
