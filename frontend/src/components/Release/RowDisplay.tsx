import clsx from 'clsx';
import * as React from 'react';
import { Link } from 'src/components/common';
import { Image } from 'src/components/Image';
import { ArtistList, GenreList } from 'src/components/Lists';
import { ReleaseT } from 'src/types';
import { secondsToLength } from 'src/util';

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
        'flex items-center w-full py-3 cursor-pointer hover:bg-black hover:bg-opacity-5 dark:hover:bg-white dark:hover:bg-opacity-5',
      )}
    >
      <div className="relative flex-none w-12 h-12 mr-2">
        <Image
          className="absolute object-cover rounded-lg full"
          imageId={release.imageId}
          thumbnail
        />
      </div>
      <div className="flex-1 overflow-hidden">
        <div className="flex">
          <div className="flex flex-shrink mr-4 truncate">
            <div className="font-semibold truncate text-primary-alt">{release.title}</div>
            {release.releaseYear ? <div className="flex-none"> [{release.releaseYear}]</div> : null}
          </div>
          <div className="flex-none hidden ml-auto sm:block">
            <span>{release.numTracks} </span>
            <span className="text-gray-800 dark:text-gray-300">
              {release.numTracks !== 1 ? 'tracks' : 'track'}
            </span>
            <span> / {runMinutes} </span>
            <span className="text-gray-800 dark:text-gray-300">minutes</span>
          </div>
        </div>
        <div className="flex">
          <ArtistList className="mr-8 truncate max-w-3/5" elements={release.artists} />
          <div className="flex-1 hidden overflow-hidden text-right md:block rtl">
            <GenreList className="truncate" elements={release.genres} />
          </div>
        </div>
      </div>
    </Link>
  );
};
