import * as React from 'react';

import { ArtistT, ReleaseT } from 'src/types';

import { ArtistList } from './ArtistList';
import { CoverArt } from './CoverArt';
import { GenreList } from './GenreList';
import clsx from 'clsx';
import { secondsToLength } from 'src/common';

export const RowRelease: React.FC<{ release: ReleaseT; className?: string | undefined }> = ({
  release,
  className,
}) => {
  const runMinutes = React.useMemo(() => secondsToLength(release.runtime).split(':')[0], [release]);

  return (
    <div
      className={clsx(
        className,
        'w-full flex items-center py-3 hover:bg-white hover:bg-opacity-5 cursor-pointer',
      )}
      onClick={(): void => {}}
    >
      <div className="flex-none relative w-12 h-12 mr-2">
        <CoverArt className="absolute full object-cover rounded-lg" release={release} />
      </div>
      <div className="flex-1 overflow-hidden">
        <div className="flex">
          <div className="flex-shrink flex mr-4 truncate">
            <div className="truncate font-semibold text-bold">{release.title}</div>
            {release.releaseYear ? (
              <div className="flex-none">&nbsp;&nbsp;[{release.releaseYear}]</div>
            ) : null}
          </div>
          <div className="hidden sm:block flex-none ml-auto">
            {release.numTracks}&nbsp;
            <span className="text-gray-300">{release.numTracks !== 1 ? 'tracks' : 'track'}</span>
            &nbsp;/&nbsp;{runMinutes}&nbsp;
            <span className="text-gray-300">minutes</span>
          </div>
        </div>
        <div className="flex">
          <ArtistList className="truncate max-w-3/5 mr-8" artists={release.artists as ArtistT[]} />
          <div className="hidden md:block flex-1 overflow-hidden text-right rtl">
            <GenreList className="truncate" genres={release.genres} />
          </div>
        </div>
      </div>
    </div>
  );
};
