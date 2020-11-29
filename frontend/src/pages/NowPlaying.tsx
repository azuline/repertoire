import * as React from 'react';
import { Header, SectionHeader, Tracklist } from 'src/components';
import { PlayQueueContext } from 'src/contexts';

export const NowPlaying: React.FC = () => {
  const { playQueue } = React.useContext(PlayQueueContext);

  return (
    <div>
      <Header />
      {playQueue.length === 0 ? (
        <SectionHeader className="px-8 my-8 text-center">Now Playing Nothing ^.~</SectionHeader>
      ) : (
        <Tracklist tracks={playQueue} />
      )}
    </div>
  );
};
