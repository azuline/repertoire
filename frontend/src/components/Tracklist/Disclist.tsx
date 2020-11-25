import * as React from 'react';

import { PlayQueueContext } from 'src/contexts';
import { SectionHeader } from 'src/components/common';
import { Track } from './Track';
import { TrackT } from 'src/types';
import clsx from 'clsx';
import { stringNumberCompare } from 'src/common';

type Discs = { [dn in string]: TrackT[] };

export const Disclist: React.FC<{ className?: string; tracks: TrackT[] }> = ({
  className,
  tracks,
}) => {
  const { playQueue, setPlayQueue, curIndex, setCurIndex } = React.useContext(PlayQueueContext);

  // The tracks arranged into discs.
  const discs = React.useMemo(() => sortTracksIntoDiscs(tracks), [tracks]);
  // The tracks sorted first by disc number and then by track number.
  const sortedTracklist = React.useMemo(() => sortDiscsIntoTracklist(discs), [discs]);
  const multiDisc = React.useMemo(() => Object.keys(discs).length !== 1, [discs]);

  // Check to see if the current track list matches up with the play queue--if
  // it does, we are currently playing this Disclist.
  const areTrackListsMatching = React.useMemo(() => {
    if (playQueue.length !== sortedTracklist.length) return false;

    for (let i = 0; i < playQueue.length; i++) {
      if (playQueue[i] !== sortedTracklist[i]) return false;
    }

    return true;
  }, [playQueue, sortedTracklist]);

  const trackOnClick = React.useCallback(
    (index: number): void => {
      setPlayQueue(sortedTracklist);
      setCurIndex(index);
    },
    [setPlayQueue, setCurIndex, sortedTracklist],
  );

  let trackIndex = 0;

  return (
    <div className={clsx(className, 'mx-8')}>
      {Object.entries(discs).map(([discNumber, tracks], i) => (
        <>
          {multiDisc && (
            <SectionHeader className={i > 0 ? 'my-4' : 'mb-4'}>Disc {discNumber}</SectionHeader>
          )}
          {tracks.map((track) => {
            trackIndex++;
            return (
              <Track
                key={trackIndex}
                track={track}
                index={trackIndex}
                onClick={trackOnClick}
                active={areTrackListsMatching && curIndex === trackIndex}
              />
            );
          })}
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
    discs[dn].sort((a, b) => stringNumberCompare(a.trackNumber, b.trackNumber));
  });

  return discs;
};

const sortDiscsIntoTracklist = (discs: Discs): TrackT[] => {
  const discKeys = Object.keys(discs);
  discKeys.sort(stringNumberCompare);

  return discKeys.reduce<TrackT[]>((acc, disc) => {
    acc.push(...discs[disc]);
    return acc;
  }, []);
};
