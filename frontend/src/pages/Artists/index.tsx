import * as React from 'react';

import { Header } from '~/components';
import { useId } from '~/hooks';

import { Artist } from './Artist';
import { ArtistChooser } from './Chooser';

export const Artists: React.FC = () => {
  const active = useId();

  return (
    <>
      {!active && <Header />}
      <div className="flex flex-1">
        <ArtistChooser active={active} className="flex-none" />
        {active && <Artist active={active} />}
      </div>
    </>
  );
};
