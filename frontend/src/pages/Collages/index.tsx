import * as React from 'react';
import { CollectionChooser, Header } from 'src/components';
import { useId } from 'src/hooks';
import { CollectionType } from 'src/types';

import { Collage } from './Collage';

const types = [CollectionType.SYSTEM, CollectionType.COLLAGE];

export const Collages: React.FC = () => {
  const active = useId();

  return (
    <div className="flex flex-col flex-1 min-h-0 full">
      {!active && <Header />}
      <div className="flex flex-1 min-h-0">
        <CollectionChooser collectionTypes={types} urlPrefix="/collages" active={active} />
        {active && <Collage active={active} />}
      </div>
    </div>
  );
};
