import * as React from 'react';
import { LabelList } from './LabelList';
import { GenreList } from './GenreList';
import { secondsToLength } from 'src/common';
import { ArtistList } from './ArtistList';
import { CoverArt } from './CoverArt';
import { ReleaseT, ArtistT, CollectionT } from 'src/types';

export const RowRelease: React.FC<{ release: ReleaseT }> = ({ release }) => {
  const runMinutes = React.useMemo(() => secondsToLength(release.runtime).split(':')[0], [release]);

  return (
    <div
      className="w-full flex items-center py-3 hover:bg-black hover:bg-opacity-25 rounded cursor-pointer"
      onClick={(): void => {}}
    >
      <div className="flex-none relative mx-2 w-12 h-12">
        <CoverArt className="absolute full object-cover rounded-lg" release={release} />
      </div>
      <div className="flex-1 md:w-2/5 xl:w-1/4 overflow-hidden">
        <div className="truncate font-semibold">{release.title}</div>
        <ArtistList className="truncate" artists={release.artists as ArtistT[]} />
      </div>
      <div className="hidden lg:flex w-16 border-l-2 border-bg-embellish px-3">
        <div className="py-2">{release.releaseYear || '????'}</div>
      </div>
      <div className="hidden xl:flex w-24 border-l-2 border-bg-embellish px-3">
        <div className="py-2">
          {release.numTracks} Track{release.numTracks !== 1 ? 's' : ''}
        </div>
      </div>
      <div className="hidden 2xl:flex w-28 border-l-2 border-bg-embellish px-3">
        <div className="py-2">{runMinutes} minutes</div>
      </div>
      <div className="hidden md:flex flex-none w-1/6 max-w-20 border-l-2 border-bg-embellish px-3 py-2 overflow-hidden">
        {(release.labels as CollectionT[]).length !== 0 ? (
          <LabelList className="truncate" labels={release.labels} />
        ) : (
          'No Label'
        )}
      </div>
      <div className="hidden md:flex flex-none w-2/5 border-l-2 border-bg-embellish px-3 py-2 overflow-hidden">
        <GenreList className="truncate" genres={release.genres} />
      </div>
    </div>
  );
};
