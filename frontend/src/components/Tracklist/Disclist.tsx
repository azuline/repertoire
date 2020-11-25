import * as React from 'react';
import clsx from 'clsx';
import { TrackT } from 'src/types';
import { SectionHeader } from 'src/components/common/SectionHeader';
import { Track } from './Track';

type Discs = { [dn in string]: TrackT[] };

export const Disclist: React.FC<{ className?: string; tracks: TrackT[] }> = ({
  className,
  tracks,
}) => {
  const discs = React.useMemo(() => sortTracksIntoDiscs(tracks), [tracks]);
  const multiDisc = React.useMemo(() => Object.keys(discs).length !== 1, [discs]);

  return (
    <div className={clsx(className, 'mx-8')}>
      {Object.entries(discs).map(([discNumber, tracks], i) => (
        <>
          {multiDisc && (
            <SectionHeader className={i > 0 ? 'my-4' : 'mb-4'}>Disc {discNumber}</SectionHeader>
          )}
          <div>
            {tracks.map((track, i) => (
              <Track key={i} track={track} />
            ))}
          </div>
        </>
      ))}
    </div>
  );
};

const sortTracksIntoDiscs = (tracks: TrackT[]): Discs => {
  const discs = tracks.reduce<Discs>((discs, track) => {
    const discNumber = track.discNumber || '1';

    discs[discNumber] = discs[discNumber] ?? [];
    discs[discNumber].push(track);

    return discs;
  }, {});

  Object.keys(discs).forEach((dn) => {
    discs[dn].sort((a, b) => {
      const aTn = a.trackNumber.padStart(3, '0');
      const bTn = b.trackNumber.padStart(3, '0');

      if (aTn < bTn) return -1;
      if (aTn > bTn) return 1;
      return 0;
    });
  });

  return discs;
};
