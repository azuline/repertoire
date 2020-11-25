import * as React from 'react';
import { CollectionChooser, Header } from 'src/components';
import { useId } from 'src/hooks';
import { CollectionType } from 'src/types';

import { Label } from './Label';

const types = [CollectionType.LABEL];

export const Labels: React.FC = () => {
  const active = useId();

  return (
    <div className="full flex flex-col flex-1 min-h-0">
      {!active && <Header />}
      <div className="flex flex-1 min-h-0">
        <CollectionChooser collectionTypes={types} urlPrefix="/labels" active={active} />
        {active && <Label active={active} />}
      </div>
    </div>
  );
};
