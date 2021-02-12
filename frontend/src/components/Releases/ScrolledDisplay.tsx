import clsx from 'clsx';
import * as React from 'react';

import { ArtRelease } from '~/components/Release';
import { ReleaseT } from '~/types';

export const ScrolledReleases: React.FC<{
  releases: ReleaseT[];
  className?: string;
}> = ({ releases, className }) => (
  <div
    className={clsx(className, 'w-fullpad px-6 md:px-8 -mx-6 md:-mx-8 py-8 flex overflow-x-auto')}
  >
    {releases.map((rls) => (
      <div key={rls.id} className="flex-shrink-0 w-56 h-56 mr-4">
        <ArtRelease release={rls} />
      </div>
    ))}
  </div>
);
