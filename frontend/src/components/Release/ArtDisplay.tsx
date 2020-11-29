import clsx from 'clsx';
import * as React from 'react';
import { Link } from 'src/components/common';
import { Image } from 'src/components/Image';
import { ArtistList, GenreList } from 'src/components/Lists';
import { ReleaseT } from 'src/types';
import { secondsToLength } from 'src/util';

const textStyle = {
  textShadow: '1px black',
  background:
    'linear-gradient(to bottom, rgba(0, 0, 0, 0), rgba(0, 0, 0, 0.1), rgba(0, 0, 0, 0.4), rgba(0, 0, 0, 0.7), rgba(0, 0, 0, 0.9))',
};

export const ArtRelease: React.FC<{ release: ReleaseT; className?: string }> = ({
  release,
  className,
}) => {
  const runtime = React.useMemo(() => secondsToLength(release.runtime), [release]);

  return (
    <Link href={`/releases/${release.id}`}>
      <div className={clsx(className, 'relative h-0 pb-full')}>
        <Image
          className="absolute object-cover rounded-lg full"
          imageId={release.imageId}
          thumbnail
        />
        <div className="absolute z-10 rounded-lg full two-sided" style={textStyle}>
          <div className="flex flex-col justify-end overflow-hidden front full">
            <div className="p-3 overflow-hidden">
              <div className="text-lg font-semibold text-white truncate" title={release.title}>
                {release.title}
              </div>
              <ArtistList className="text-gray-200 truncate" elements={release.artists} />
            </div>
          </div>
          <div className="relative back full">
            <div className="absolute top-0 left-0 bg-black rounded-lg bg-opacity-75 full" />
            <div className="absolute top-0 left-0 z-10 flex flex-col items-center justify-center p-4 text-white full text-md">
              {release.releaseYear ? <div className="py-1">{release.releaseYear}</div> : null}
              <div className="py-1">
                {release.numTracks} Track{release.numTracks !== 1 && 's'} / {runtime}
              </div>
              {release.genres.length !== 0 ? (
                <GenreList className="mt-4 text-center truncate-2" elements={release.genres} />
              ) : null}
            </div>
          </div>
        </div>
      </div>
    </Link>
  );
};
