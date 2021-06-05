import * as React from 'react';

import { useId } from '~/hooks';
import { Layout } from '~/layout';

import { Artist } from './Artist';
import { ArtistChooser } from './Chooser';

export const Artists: React.FC = () => {
  const active = useId();

  return (
    <Layout tw="flex flex-1">
      <ArtistChooser active={active} tw="flex-none" />
      {active !== null && (
        <Layout padX padY scroll>
          <Artist active={active} />
        </Layout>
      )}
    </Layout>
  );
};
