import clsx from 'clsx';
import * as React from 'react';
import { Header, Image, SectionHeader, Tracklist } from 'src/components';
import { PlayQueueContext } from 'src/contexts';

import { Info } from './Info';

export const NowPlaying: React.FC = () => {
  const { playQueue, curIndex } = React.useContext(PlayQueueContext);

  // prettier-ignore
  const curTrack = React.useMemo(
    () => (curIndex !== null ? playQueue[curIndex] : null),
    [playQueue, curIndex],
  );

  return (
    <div className="flex flex-col full">
      <Header />
      {playQueue.length === 0 ? (
        <SectionHeader className="px-8 my-16 text-center">nothing playing ^.~</SectionHeader>
      ) : (
        <div className="flex flex-col min-h-0 mt-4">
          {curTrack && <Info track={curTrack} />}
          <SectionHeader className="px-8 my-8">Play Queue</SectionHeader>
          <Tracklist tracks={playQueue} />
        </div>
      )}
    </div>
  );
};
