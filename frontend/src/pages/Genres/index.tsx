import * as React from 'react';

import { Header } from 'src/components/Header';
import { CollectionType } from 'src/types';
import { Genre } from './Genre';
import { CollectionChooser } from 'src/components/collection';
import { useId } from 'src/hooks';

const types = [CollectionType.GENRE];
export const Genres: React.FC = () => {
  const active = useId();

  return (
    <div className="full flex flex-col flex-1 min-h-0">
      {!active && <Header />}
      <div className="flex flex-1 min-h-0">
        <CollectionChooser collectionTypes={types} urlPrefix="/genres" active={active} />
        {active && <Genre active={active} />}
      </div>
    </div>
  );
};
