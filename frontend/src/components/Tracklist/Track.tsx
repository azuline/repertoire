import clsx from 'clsx';
import * as React from 'react';
import { Icon } from 'src/components/common';
import { TrackArtistList } from 'src/components/Lists';
import { SidebarContext } from 'src/contexts';
import { TrackT } from 'src/types';
import { secondsToLength } from 'src/util';

export const Track: React.FC<{
  track: TrackT;
  trackNumber: number;
  index: number;
  onClick?: (arg0: number) => void;
  active?: boolean;
}> = ({ track, trackNumber, index, onClick, active = false }) => {
  const { isSidebarOpen } = React.useContext(SidebarContext);
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
        <div
          className={clsx(
            'flex-1 mr-2 truncate',
            isSidebarOpen ? 'md:flex-none w-1/3' : 'w-1/3 sm:flex-none',
          )}
          title={track.title}
        >
          <span>{trackNumber}. </span>
          {track.title}
        </div>
        <TrackArtistList
          artists={track.artists}
          className={clsx(
            'flex-1 hidden truncate text-foreground-400',
            isSidebarOpen ? 'md:block' : 'sm:block',
          )}
        />
        <div className="flex-none ml-2 text-foreground-400">{secondsToLength(track.duration)}</div>
      </div>
      <TrackArtistList
        artists={track.artists}
        className={clsx(
          'mt-1 ml-8 truncate text-foreground-400',
          isSidebarOpen ? 'md:hidden' : 'sm:hidden',
        )}
      />
    </div>
  );
};
