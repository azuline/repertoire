import * as React from 'react';
import clsx from 'clsx';
import { ArtistT, ReleaseT } from 'src/types';
import { CoverArt } from './CoverArt';
import { ArtistList } from './ArtistList';

export const ArtRelease: React.FC<{ className: string; release: ReleaseT }> = ({
  className,
  release,
}) => {
  return (
    <div className={clsx(className, 'flex flex-col flex-no-wrap h-full')}>
      <CoverArt className="flex-0" release={release} />
      <div className="flex-1 mt-1">
        <span className="truncate-2 font-medium">{release.title}</span>
        <ArtistList className="truncate-2" artists={release.artists as ArtistT[]} />
      </div>
    </div>
  );
};
