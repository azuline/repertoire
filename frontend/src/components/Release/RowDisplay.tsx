import * as React from 'react';

import { ArtistList, GenreList } from 'src/components/Lists';
import { ArtistT, ReleaseT } from 'src/types';

import { CoverArt } from './CoverArt';
import { Link } from 'src/components/common';
import clsx from 'clsx';
import { secondsToLength } from 'src/common';

export const RowRelease: React.FC<{ release: ReleaseT; className?: string }> = ({
  release,
  className,
}) => {
  const runMinutes = React.useMemo(() => secondsToLength(release.runtime).split(':')[0], [release]);

  return (
    <Link
      href={`/releases/${release.id}`}
      className={clsx(
        className,
        'w-full flex items-center py-3 hover:bg-black hover:bg-opacity-5 dark:hover:bg-white dark:hover:bg-opacity-5 cursor-pointer',
      )}
    >
      <div className="flex-none relative w-12 h-12 mr-2">
        <CoverArt thumbnail className="absolute full object-cover rounded-lg" release={release} />
      </div>
      <div className="flex-1 overflow-hidden">
        <div className="flex">
          <div className="flex-shrink flex mr-4 truncate">
            <div className="truncate font-semibold text-primary">{release.title}</div>
            {release.releaseYear ? (
              <div className="flex-none">&nbsp;&nbsp;[{release.releaseYear}]</div>
            ) : null}
          </div>
          <div className="hidden sm:block flex-none ml-auto">
            {release.numTracks}&nbsp;
            <span className="text-gray-800 dark:text-gray-300">
              {release.numTracks !== 1 ? 'tracks' : 'track'}
            </span>
            &nbsp;/&nbsp;{runMinutes}&nbsp;
            <span className="text-gray-800 dark:text-gray-300">minutes</span>
          </div>
        </div>
        <div className="flex">
          <ArtistList className="truncate max-w-3/5 mr-8" elements={release.artists as ArtistT[]} />
          <div className="hidden md:block flex-1 overflow-hidden text-right rtl">
            <GenreList className="truncate" elements={release.genres} />
          </div>
        </div>
      </div>
    </Link>
  );
};
