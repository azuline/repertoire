import * as React from 'react';

import { SectionHeader, Tracklist } from '~/components';
import { PlayQueueContext } from '~/contexts';

import { Info } from './Info';

export const NowPlaying: React.FC = () => {
  const { playQueue, curIndex } = React.useContext(PlayQueueContext);

  const curTrack = curIndex !== null ? playQueue[curIndex] : null;

  // Only show covers if the play queue isn't a single homogenous release.
  const showCovers =
    playQueue.length > 0 &&
    !playQueue.every((t) => t.release.id === playQueue[0].release.id);

  if (playQueue.length === 0) {
    return <SectionHeader tw="my-16 text-center">nothing playing ^.~</SectionHeader>;
  }

  return (
    <div tw="flex flex-col mt-4">
      {curTrack && <Info track={curTrack} />}
      <SectionHeader tw="my-8">Play Queue</SectionHeader>
      <Tracklist showCovers={showCovers} tracks={playQueue} />
    </div>
  );
};
