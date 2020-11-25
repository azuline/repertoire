import * as React from 'react';

import { Header } from 'src/components/Header';
import { CollectionType } from 'src/types';
import { Collage } from './Collage';
import { CollectionChooser } from 'src/components/collection';
import { useId } from 'src/hooks';

const types = [CollectionType.SYSTEM, CollectionType.COLLAGE];

export const Collages: React.FC = () => {
  const active = useId();

  return (
    <div className="full flex flex-col flex-1 min-h-0">
      {!active && <Header />}
      <div className="flex flex-1 min-h-0">
        <CollectionChooser collectionTypes={types} urlPrefix="/collages" active={active} />
        {active && <Collage active={active} />}
      </div>
    </div>
  );
};
