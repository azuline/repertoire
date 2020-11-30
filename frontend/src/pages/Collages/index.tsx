import * as React from 'react';
import { CollectionChooser, Header } from 'src/components';
import { useId } from 'src/hooks';
import { CollectionType } from 'src/types';

import { Collage } from './Collage';

const types = [CollectionType.SYSTEM, CollectionType.COLLAGE];

export const Collages: React.FC = () => {
  const active = useId();

  return (
    <>
      {!active && <Header />}
      <div className="flex flex-1">
        <CollectionChooser
          active={active}
          className="flex-none"
          collectionTypes={types}
          urlPrefix="/collages"
        />
        {active && <Collage active={active} />}
      </div>
    </>
  );
};
