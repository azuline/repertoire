import * as React from 'react';
import { CollectionChooser, Header } from 'src/components';
import { useId } from 'src/hooks';
import { CollectionType } from 'src/types';

import { Label } from './Label';

const types = [CollectionType.LABEL];

export const Labels: React.FC = () => {
  const active = useId();

  return (
    <>
      {!active && <Header />}
      <div className="flex flex-1">
        <CollectionChooser
          active={active}
          className="flex-none"
          collectionTypes={types}
          urlPrefix="/labels"
        />
        {active && <Label active={active} />}
      </div>
    </>
  );
};
