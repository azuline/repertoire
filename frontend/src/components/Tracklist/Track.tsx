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
  const trackOnClick = React.useCallback(() => onClick && onClick(index), [index, onClick]);

  return (
    <div
      className={clsx(
        'py-1.5 px-2 w-full rounded',
        active && 'font-bold',
        onClick &&
          'cursor-pointer hover:bg-black hover:bg-opacity-5 dark:hover:bg-white dark:hover:bg-opacity-5',
      )}
      onClick={trackOnClick}
    >
      <div className="flex items-center">
        <Icon className="flex-none w-5 mr-3 cursor-pointer text-primary-alt" icon="play-medium" />
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
            'flex-1 hidden truncate text-gray-800 dark:text-gray-400',
            isSidebarOpen ? 'md:block' : 'sm:block',
          )}
        />
        <div className="flex-none mx-2">{secondsToLength(track.duration)}</div>
      </div>
      <TrackArtistList
        artists={track.artists}
        className={clsx(
          'mt-1 ml-8 truncate text-gray-800 dark:text-gray-400',
          isSidebarOpen ? 'md:hidden' : 'sm:hidden',
        )}
      />
    </div>
  );
};
