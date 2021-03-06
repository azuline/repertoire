import * as React from 'react';

import { Header } from '~/components';
import { useId } from '~/hooks';

import { Artist } from './Artist';
import { ArtistChooser } from './Chooser';

export const Artists: React.FC = () => {
  const active = useId();

  return (
    <>
      {active === null && <Header />}
      <div tw="flex flex-1">
        <ArtistChooser active={active} tw="flex-none" />
        {active !== null && <Artist active={active} />}
      </div>
    </>
  );
};
