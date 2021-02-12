import clsx from 'clsx';
import * as React from 'react';
import { Icon } from '~/components/common';
import { TrackArtistList } from '~/components/Lists';
import { TrackT } from '~/types';
import { secondsToLength } from '~/util';

export const Track: React.FC<{
  track: TrackT;
  trackNumber: number;
  index: number;
  onClick?: (arg0: number) => void;
  active?: boolean;
}> = ({ track, trackNumber, index, onClick, active = false }) => {
  const trackOnClick = (): void => onClick && onClick(index);

  return (
    <div
      className={clsx(
        'py-1.5 px-3 -mx-3 rounded',
        active && 'font-bold',
        onClick && 'cursor-pointer hover-emph-bg',
      )}
      style={{ width: 'calc(100% + 1.5rem)' }}
      onClick={trackOnClick}
    >
      <div className="flex items-center">
        <Icon className="flex-none w-5 mr-3 cursor-pointer text-primary-500" icon="play-medium" />
        <div className="flex-1 mr-2 truncate md:flex-none w-1/3" title={track.title}>
          <span>{trackNumber}. </span>
          {track.title}
        </div>
        <TrackArtistList
          artists={track.artists}
          className="flex-1 hidden truncate text-foreground-400 md:block"
        />
        <div className="flex-none ml-2 text-foreground-400">{secondsToLength(track.duration)}</div>
      </div>
      <TrackArtistList
        artists={track.artists}
        className="mt-1 ml-8 truncate text-foreground-400 md:hidden"
      />
    </div>
  );
};
