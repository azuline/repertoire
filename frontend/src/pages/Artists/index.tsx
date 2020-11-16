import * as React from 'react';

import { Artist } from './Artist';
import { ArtistChooser } from './Chooser';
import { useId } from 'src/hooks';

export const Artists: React.FC = () => {
  const active = useId();

  return (
    <div className="flex-1 full px-8 lg:px-12 flex">
      <ArtistChooser active={active} />
      {active && <Artist active={active} />}
    </div>
  );
};
