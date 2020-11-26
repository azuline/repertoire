import * as React from 'react';
import { CollectionChooser, Header } from 'src/components';
import { useId } from 'src/hooks';
import { CollectionType } from 'src/types';

import { Genre } from './Genre';

const types = [CollectionType.GENRE];
export const Genres: React.FC = () => {
  const active = useId();

  return (
    <div className="flex flex-col flex-1 min-h-0 full">
      {!active && <Header />}
      <div className="flex flex-1 min-h-0">
        <CollectionChooser collectionTypes={types} urlPrefix="/genres" active={active} />
        {active && <Genre active={active} />}
      </div>
    </div>
  );
};
