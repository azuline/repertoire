import * as React from 'react';
import tw from 'twin.macro';

import { SectionHeader } from '~/components/common';
import { PlayQueueContext } from '~/contexts';
import { ITrack, ITrackFieldsFragment } from '~/graphql';
import { stringNumberCompare } from '~/util';

import { Track } from './Track';
import { checkMatchingTracklists } from './util';

type IDisclist = React.FC<{
  className?: string;
  tracks: ITrackFieldsFragment[];
}>;

export const Disclist: IDisclist = ({ className, tracks }) => {
  const { playQueue, setPlayQueue, curIndex, setCurIndex } =
    React.useContext(PlayQueueContext);

  const discs = React.useMemo(() => sortTracksIntoDiscs(tracks), [tracks]);
  const multiDisc = Object.keys(discs).length !== 1;

  const sortedTracklist = React.useMemo(() => sortDiscsIntoTracklist(discs), [discs]);

  // Check to see if the current track list matches up with the play queue--if
  // it does, we are currently playing this Disclist.
  const areTrackListsMatching = React.useMemo(
    () => checkMatchingTracklists(playQueue, sortedTracklist),
    [playQueue, sortedTracklist],
  );

  const trackOnClick = (index: number): void => {
    if (!areTrackListsMatching) {
      setPlayQueue(sortedTracklist);
    }

    setCurIndex(index);
  };

  let trackIndex = -1;

  return (
    <div className={className} tw="pb-8">
      {Object.entries(discs).map(([discNumber, discTracks], i) => (
        <React.Fragment key={discNumber}>
          {multiDisc && (
            <SectionHeader css={[tw`text-foreground-300`, i > 0 ? tw`my-4` : tw`mb-4`]}>
              Disc {discNumber}
            </SectionHeader>
          )}
          {discTracks.map((track, trackNumber) => {
            trackIndex += 1;
            return (
              <Track
                key={trackIndex}
                active={areTrackListsMatching && curIndex === trackIndex}
                index={trackIndex}
                track={track}
                trackNumber={trackNumber + 1}
                onClick={trackOnClick}
              />
            );
          })}
        </React.Fragment>
      ))}
    </div>
  );
};

type ITrackWithNumbers = Pick<ITrack, 'trackNumber' | 'discNumber'>;

const sortTracksIntoDiscs = <T extends ITrackWithNumbers>(
  tracks: T[],
): Record<string, T[]> => {
  const discs = tracks.reduce<Record<string, T[]>>((acc, track) => {
    const discNumber = track.discNumber || '1';

    acc[discNumber] = acc[discNumber] ?? [];
    acc[discNumber].push(track);

    return acc;
  }, {});

  Object.keys(discs).forEach((dn) => {
    discs[dn].sort((a, b) => stringNumberCompare(a.trackNumber, b.trackNumber));
  });

  return discs;
};

const sortDiscsIntoTracklist = <T extends ITrackWithNumbers>(
  discs: Record<string, T[]>,
): T[] => {
  const discKeys = Object.keys(discs);
  discKeys.sort(stringNumberCompare);

  return discKeys.reduce<T[]>((acc, disc) => {
    acc.push(...discs[disc]);
    return acc;
  }, []);
};
