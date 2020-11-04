import * as React from 'react';

import { ArtistT, ReleaseT } from 'src/types';
import { secondsToLength } from 'src/common';

import { ArtistList } from './ArtistList';
import { LabelList } from './LabelList';
import { GenreList } from './GenreList';
import { CoverArt } from './CoverArt';
import clsx from 'clsx';

const textStyle = {
  fontFamily: 'Optimus Princeps',
  textShadow: '1px 1px black',
  background:
    'linear-gradient(to bottom, rgba(0, 0, 0, 0), rgba(0, 0, 0, 0.2), rgba(0, 0, 0, 0.8))',
};

export const ArtRelease: React.FC<{ release: ReleaseT; className?: string }> = ({
  release,
  className = '',
}) => {
  const whenReleased = React.useMemo(() => {
    if (release.releaseDate) {
      return `on ${release.releaseDate}`;
    } else if (release.releaseYear) {
      return `in ${release.releaseYear}`;
    } else {
      return null;
    }
  }, [release]);

  const runtime = React.useMemo(() => secondsToLength(release.runtime), [release]);

  return (
    <a href={`/releases/${release.id}`}>
      <div className={clsx(className, 'relative h-0 pb-full text-white')}>
        <CoverArt className="absolute full object-cover rounded-lg" release={release} />
        <div className="two-sided full absolute z-10" style={textStyle}>
          <div className="front flex flex-col full justify-end">
            <div className="p-4">
              <a className="truncate-2 font-semibold text-2xl" title={release.title}>
                {release.title}
              </a>
              <ArtistList
                className="truncate-2 mt-2 text-xl"
                artists={release.artists as ArtistT[]}
              />
            </div>
          </div>
          <div className="back relative flex flex-col full justify-center items-center">
            <div className="absolute rounded-lg top-0 left-0 bg-black bg-opacity-70 full" />
            <div className="z-10 p-4 text-center">
              {whenReleased && <div className="py-1">Released {whenReleased}</div>}
              <div className="py-1">
                {release.numTracks} Track{release.numTracks !== 1 ? 's' : ''} :: {runtime}
              </div>
              <div className="mt-4">
                <LabelList
                  className="py-1 truncate-2 text-xl"
                  prefix="Labels:"
                  labels={release.labels}
                />
                <GenreList className="py-1 truncate-2 text-xl" genres={release.genres} />
              </div>
            </div>
          </div>
        </div>
      </div>
    </a>
  );
};
