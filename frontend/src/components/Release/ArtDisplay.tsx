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
        <div className="rounded-lg bg-black absolute h-full w-full" />
        <CoverArt
          className="absolute z-10 opacity-70 hover:opacity-50 h-full w-full object-cover rounded-lg"
          release={release}
        />
      </a>
      <div className="h-full w-full absolute z-20 pointer-events-none flex items-center justify-center">
        <div
          className="text-center text-white p-4"
          style={{
            fontFamily: 'Optimus Princeps',
            textShadow: '#000000 2px 2px, #000000 2px 2px 4px',
          }}
        >
          <a
            href={`/releases/${release.id}`}
            className="truncate-2 font-semibold text-2xl self-end w-full"
            title={release.title}
          >
            {release.title}
          </a>
          <ArtistList className="truncate-2" artists={release.artists as ArtistT[]} />
        </div>
      </div>
    </div>
  );
};
