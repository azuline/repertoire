import * as React from 'react';

import { Header } from 'src/components/Header';
import { CollectionType } from 'src/types';
import { Genre } from './Genre';
import { CollectionChooser } from 'src/components/Chooser';
import { useId } from 'src/hooks';

export const Genres: React.FC = () => {
  const active = useId();

  return (
    <div className="full flex flex-col flex-1 min-h-0">
      {!active && <Header />}
      <div className="flex flex-1 min-h-0">
        <CollectionChooser collectionType={CollectionType.GENRE} active={active} />
        {active && <Genre active={active} />}
      </div>
    </div>
  );
};
