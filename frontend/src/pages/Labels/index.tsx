import * as React from 'react';

import { CollectionChooser, Header } from '~/components';
import { useId } from '~/hooks';
import { CollectionType } from '~/types';

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
