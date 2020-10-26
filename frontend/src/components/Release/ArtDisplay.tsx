import * as React from 'react';
import clsx from 'clsx';
import { ReleaseT } from 'src/types';
import { CoverArt } from './CoverArt';

export const ArtRelease: React.FC<{ className: string; release: ReleaseT }> = ({
  className,
  release,
}) => {
  return (
    <div className={clsx(className, 'flex flex-col flex-no-wrap h-full')}>
      <CoverArt className="flex-0" release={release} />
      <span className="flex-1 mt-1 font-medium text-center truncate">
        {release.title}
      </span>
    </div>
  );
};
