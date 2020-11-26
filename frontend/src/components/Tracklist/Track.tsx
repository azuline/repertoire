import clsx from 'clsx';
import * as React from 'react';
import { Icon } from 'src/components/common';
import { ArtistList } from 'src/components/Lists';
import { SidebarContext } from 'src/contexts';
import { TrackArtistT, TrackT } from 'src/types';
import { arrangeArtists, secondsToLength } from 'src/util';

export const Track: React.FC<{
  track: TrackT;
  index: number;
  onClick?: (arg0: number) => void;
  active?: boolean;
}> = ({ track, index, onClick, active = false }) => {
  const { isSidebarOpen } = React.useContext(SidebarContext);
  const trackOnClick = React.useCallback(() => onClick && onClick(index), [index, onClick]);

  return (
    <div
      className={clsx(
        'py-1.5 px-2 w-full rounded',
        active && 'font-bold',
        onClick &&
          'hover:bg-black hover:bg-opacity-5 dark:hover:bg-white dark:hover:bg-opacity-5 cursor-pointer',
      )}
      onClick={trackOnClick}
    >
      <div className="flex items-center">
        <Icon className="flex-none w-5 mr-3 cursor-pointer text-primary" icon="play-medium" />
        <div
          className={clsx(
            'flex-1 mr-2 truncate',
            isSidebarOpen ? 'md:flex-none w-1/3' : 'sm:flex-none w-1/3',
          )}
          title={track.title}
        >
          {track.trackNumber && <span>{track.trackNumber}. </span>}
          {track.title}
        </div>
        <ArtistList
          elements={arrangeArtists(track.artists as TrackArtistT[])}
          className={clsx('flex-1 truncate hidden', isSidebarOpen ? 'md:block' : 'sm:block')}
          elementClassName="text-gray-800 dark:text-gray-400"
        />
        <div className="flex-none mx-2">{secondsToLength(track.duration)}</div>
      </div>
      <ArtistList
        elements={arrangeArtists(track.artists as TrackArtistT[])}
        className={clsx('ml-8 mt-1 truncate', isSidebarOpen ? 'md:hidden' : 'sm:hidden')}
        elementClassName="text-gray-800 dark:text-gray-400"
      />
    </div>
  );
};
