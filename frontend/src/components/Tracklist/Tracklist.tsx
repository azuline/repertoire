import 'twin.macro';

import * as React from 'react';

import { PlayQueueContext } from '~/contexts';
import { ITrack } from '~/graphql';

import { Track } from './Track';
import { checkMatchingTracklists } from './util';

type ITracklist = React.FC<{ className?: string; tracks: ITrack[] }>;

export const Tracklist: ITracklist = ({ className, tracks }) => {
  const { playQueue, setPlayQueue, curIndex, setCurIndex } = React.useContext(PlayQueueContext);

  // Check to see if the current track list matches up with the play queue--if
  // it does, we are currently playing this Tracklist.
  // prettier-ignore
  const areTrackListsMatching = React.useMemo(
    () => checkMatchingTracklists(playQueue, tracks),
    [playQueue, tracks],
  );

  const trackOnClick = (index: number): void => {
    setPlayQueue(tracks);
    setCurIndex(index);
  };

  return (
    <div className={className} tw="pb-8">
      {tracks.map((track, idx) => (
        <Track
          key={idx}
          active={areTrackListsMatching && curIndex === idx}
          index={idx}
          track={track}
          trackNumber={idx + 1}
          onClick={trackOnClick}
        />
      ))}
    </div>
  );
};
