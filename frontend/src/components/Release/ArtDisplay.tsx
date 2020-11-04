import * as React from 'react';

import { ArtistT, ReleaseT } from 'src/types';

import { ArtistList } from './ArtistList';
import { CoverArt } from './CoverArt';
import clsx from 'clsx';

export const ArtRelease: React.FC<{ release: ReleaseT; className?: string }> = ({
  release,
  className = '',
}) => {
  return (
    <div className={clsx(className, 'relative h-0 pb-full')}>
      <a href={`/releases/${release.id}`}>
        <CoverArt
          className="absolute z-10 h-full w-full object-cover rounded-lg"
          release={release}
        />
      </a>
      <div
        className="h-full w-full absolute z-20 pointer-events-none flex items-end"
        style={{ background: 'linear-gradient(to bottom, rgba(0, 0, 0, 0), rgba(0, 0, 0, 0.6))' }}
      >
        <div
          className="text-white w-full p-4"
          style={{ fontFamily: 'Optimus Princeps', textShadow: '1px 1px black' }}
        >
          <a
            href={`/releases/${release.id}`}
            className="truncate-2 font-semibold text-2xl"
            title={release.title}
          >
            {release.title}
          </a>
          <ArtistList className="truncate-2 mt-2" artists={release.artists as ArtistT[]} />
        </div>
      </div>
    </div>
  );
};
