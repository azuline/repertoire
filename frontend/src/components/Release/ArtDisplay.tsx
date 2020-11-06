import * as React from 'react';

import { ArtistT, ReleaseT } from 'src/types';

import { ArtistList } from './ArtistList';
import { CoverArt } from './CoverArt';
import { GenreList } from './GenreList';
import { Link } from 'src/components/common/Link';
import clsx from 'clsx';
import { secondsToLength } from 'src/common';

const textStyle = {
  textShadow: '1px 1px black',
  background:
    'linear-gradient(to bottom, rgba(0, 0, 0, 0), rgba(0, 0, 0, 0.2), rgba(0, 0, 0, 0.8))',
};

export const ArtRelease: React.FC<{ release: ReleaseT; className?: string }> = ({
  release,
  className = '',
}) => {
  const runtime = React.useMemo(() => secondsToLength(release.runtime), [release]);

  return (
    <Link href={`/releases/${release.id}`}>
      <div className={clsx(className, 'relative h-0 pb-full text-white')}>
        <CoverArt className="absolute full object-cover rounded-lg" release={release} />
        <div className="two-sided rounded-lg full absolute z-10" style={textStyle}>
          <div className="front flex flex-col full justify-end overflow-hidden">
            <div className="p-4 overflow-hidden">
              <div className="truncate font-medium text-xl" title={release.title}>
                {release.title}
              </div>
              <ArtistList
                className="truncate mt-2 text-lg"
                artists={release.artists as ArtistT[]}
              />
            </div>
          </div>
          <div className="back relative full">
            <div className="absolute rounded-lg top-0 left-0 full bg-black bg-opacity-75" />
            <div className="absolute top-0 left-0 full z-10 p-4 flex flex-col justify-center items-center text-lg">
              {release.releaseYear && <div className="py-1">Released in {release.releaseYear}</div>}
              <div className="py-1 overflow-hidden mb-4">
                {release.numTracks} Track{release.numTracks !== 1 ? 's' : ''} / {runtime}
              </div>
              <GenreList
                className="py-1 text-center truncate-2 max-w-full"
                genres={release.genres}
              />
            </div>
          </div>
        </div>
      </div>
    </Link>
  );
};
