import * as React from 'react';

import { Artist } from './Artist';
import { ArtistChooser } from './Chooser';
import { useId } from 'src/hooks';

export const Artists: React.FC = () => {
  const active = useId();

  return (
    <div className="flex flex-1 min-h-0">
      <ArtistChooser active={active} />
      {active && <Artist active={active} />}
    </div>
  );
};
