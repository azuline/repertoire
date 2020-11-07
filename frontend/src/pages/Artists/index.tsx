import * as React from 'react';

import { Artist } from './Artist';
import { ArtistChooser } from './Chooser';

export const Artists: React.FC = () => {
  const [active, setActive] = React.useState<number | null>(null);

  return (
    <div className="flex-1 w-full pr-8 flex">
      <ArtistChooser active={active} setActive={setActive} />
      {active && <Artist active={active} setActive={setActive} />}
    </div>
  );
};
