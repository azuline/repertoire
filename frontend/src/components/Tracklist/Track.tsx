import * as React from 'react';
import clsx from 'clsx';
import { TrackT, TrackArtistT } from 'src/types';
import { Icon } from 'src/components/common/Icon';
import { secondsToLength, arrangeArtists } from 'src/common';
import { ArtistList } from 'src/components/Lists';
import { SidebarContext } from 'src/contexts';

export const Track: React.FC<{ track: TrackT }> = ({ track }) => {
  const { isSidebarOpen } = React.useContext(SidebarContext);

  return (
    <div className="py-1.5 px-2 w-full rounded hover:bg-black hover:bg-opacity-5 dark:hover:bg-white dark:hover:bg-opacity-5 cursor-pointer">
      <div className="flex items-center">
        <Icon className="flex-none w-5 mr-3 text-primary cursor-pointer" icon="play-medium" />
        <div className="w-72 mr-2 truncate" title={track.title}>
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
