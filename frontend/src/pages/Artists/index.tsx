import * as React from 'react';
import { Header } from 'src/components';
import { useId } from 'src/hooks';

import { Artist } from './Artist';
import { ArtistChooser } from './Chooser';

export const Artists: React.FC = () => {
  const active = useId();

  return (
    <div className="flex flex-col flex-1 min-h-0 full">
      {!active && <Header />}
      <div className="flex flex-1 min-h-0">
        <ArtistChooser active={active} className="flex-none" />
        {active && <Artist active={active} />}
      </div>
    </div>
  );
};
