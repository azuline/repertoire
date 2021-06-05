import * as React from 'react';

import { useId } from '~/hooks';
import { Layout } from '~/layout';

import { PlaylistChooser } from './Chooser';
import { Playlist } from './Playlist';

export const Playlists: React.FC = () => {
  const active = useId();

  return (
    <Layout tw="flex flex-1">
      <PlaylistChooser active={active} tw="flex-none" />
      {active !== null && (
        <Layout padX padY scroll>
          <Playlist active={active} />
        </Layout>
      )}
    </Layout>
  );
};
