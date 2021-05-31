import * as React from 'react';

import { useId } from '~/hooks';

import { Artist } from './Artist';
import { ArtistChooser } from './Chooser';

export const Artists: React.FC = () => {
  const active = useId();

  return (
    <div tw="flex flex-1">
      <ArtistChooser active={active} tw="flex-none" />
      {active !== null && <Artist active={active} />}
    </div>
  );
};
