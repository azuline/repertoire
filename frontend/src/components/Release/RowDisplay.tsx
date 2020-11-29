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
      className={clsx(className, 'flex items-center w-full py-3 cursor-pointer hover-emph-bg')}
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
          <div className="flex flex-shrink mb-0.5 mr-4 truncate">
            <div className="font-semibold truncate text-primary-400">{release.title}</div>
            {release.releaseYear ? (
              <div className="flex-none ml-1 text-foreground-200"> [{release.releaseYear}]</div>
            ) : null}
          </div>
          <div className="flex-none hidden ml-auto sm:block" />
          {/* TODO: Maybe show release rating here? */}
        </div>
        <div className="flex text-foreground-300">
          <ArtistList className="mr-8 truncate max-w-3/5" elements={release.artists} />
          <div className="flex-1 hidden overflow-hidden text-right md:block rtl">
            <GenreList className="truncate" elements={release.genres} />
          </div>
        </div>
      </div>
    </Link>
  );
};
