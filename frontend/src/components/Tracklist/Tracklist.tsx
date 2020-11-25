import * as React from 'react';

import { PlayQueueContext } from 'src/contexts';
import { Track } from './Track';
import { TrackT } from 'src/types';
import clsx from 'clsx';
import { checkMatchingTracklists } from './util';

export const Tracklist: React.FC<{ className?: string; tracks: TrackT[] }> = ({
  className,
  tracks,
}) => {
  const { playQueue, setPlayQueue, curIndex, setCurIndex } = React.useContext(PlayQueueContext);

  // Check to see if the current track list matches up with the play queue--if
  // it does, we are currently playing this Disclist.
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

  let trackIndex = 0;

  return (
    <div className={clsx(className, 'mx-8')}>
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
    </div>
  );
};
