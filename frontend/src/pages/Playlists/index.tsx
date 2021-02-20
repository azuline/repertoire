import * as React from 'react';

import { Header } from '~/components';
import { useId } from '~/hooks';

import { PlaylistChooser } from './Chooser';
import { Playlist } from './Playlist';

export const Playlists: React.FC = () => {
  const active = useId();

  return (
    <>
      {!active && <Header />}
      <div tw="flex flex-1">
        <PlaylistChooser active={active} tw="flex-none" />
        {active && <Playlist active={active} />}
      </div>
    </>
  );
};
