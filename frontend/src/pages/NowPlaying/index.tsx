import * as React from 'react';
import { Header, SectionHeader, Tracklist } from 'src/components';
import { PlayQueueContext } from 'src/contexts';

import { Info } from './Info';

export const NowPlaying: React.FC = () => {
  const { playQueue, curIndex } = React.useContext(PlayQueueContext);

  // prettier-ignore
  const curTrack = curIndex !== null ? playQueue[curIndex] : null;

  return (
    <>
      <Header />
      {playQueue.length === 0 ? (
        <SectionHeader className="my-16 text-center">nothing playing ^.~</SectionHeader>
      ) : (
        <div className="flex flex-col mt-4">
          {curTrack && <Info track={curTrack} />}
          <SectionHeader className="my-8">Play Queue</SectionHeader>
          <Tracklist tracks={playQueue} />
        </div>
      )}
    </>
  );
};
