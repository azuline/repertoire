import * as React from 'react';

import { Header } from 'src/components/Header';
import { CollectionType } from 'src/types';
import { Label } from './Label';
import { CollectionChooser } from 'src/components/collection';
import { useId } from 'src/hooks';

export const Labels: React.FC = () => {
  const active = useId();

  return (
    <div className="full flex flex-col flex-1 min-h-0">
      {!active && <Header />}
      <div className="flex flex-1 min-h-0">
        <CollectionChooser
          collectionType={CollectionType.LABEL}
          urlPrefix="/labels"
          active={active}
        />
        {active && <Label active={active} />}
      </div>
    </div>
  );
};
