import clsx from 'clsx';
import * as React from 'react';
import { PlayQueueContext } from 'src/contexts';
import { TrackT } from 'src/types';

import { Track } from './Track';
import { checkMatchingTracklists } from './util';

export const Tracklist: React.FC<{ className?: string; tracks: TrackT[] }> = ({
  className,
  tracks,
}) => {
  const { playQueue, setPlayQueue, curIndex, setCurIndex } = React.useContext(PlayQueueContext);

  // Check to see if the current track list matches up with the play queue--if
  // it does, we are currently playing this Tracklist.
  // prettier-ignore
  const areTrackListsMatching = React.useMemo(
    () => checkMatchingTracklists(playQueue, tracks),
    [playQueue, tracks],
  );

  const trackOnClick = React.useCallback(
    (index: number): void => {
      setPlayQueue(tracks);
      setCurIndex(index);
    },
    [setPlayQueue, setCurIndex, tracks],
  );

  return (
    <div className={clsx(className, 'mx-8')}>
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
