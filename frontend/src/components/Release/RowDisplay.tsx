import * as React from 'react';
import { secondsToLength, getWhenReleased } from 'src/common';
import { ArtistList } from './ArtistList';
import { CoverArt } from './CoverArt';
import { ReleaseT, ArtistT } from 'src/types';

export const RowRelease: React.FC<{ release: ReleaseT }> = ({ release }) => {
  const whenReleased = React.useMemo(() => getWhenReleased(release), [release]);
  const runtime = React.useMemo(() => secondsToLength(release.runtime), [release]);

  return (
    <div className="w-full flex items-center py-3">
      <div className="relative mx-2 w-12 h-12">
        <CoverArt className="absolute full object-cover rounded-lg" release={release} />
      </div>
      <div className="flex-1 overflow-hidden">
        <div className="truncate font-semibold">{release.title}</div>
        <ArtistList className="truncate" artists={release.artists as ArtistT[]} />
      </div>
      <div className="px-2 text-right">
        <div>Released {whenReleased}</div>
        <div>
          {release.numTracks} Track{release.numTracks !== 1 ? 's' : ''} :: {runtime}
        </div>
      </div>
    </div>
  );
};
