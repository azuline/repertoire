import * as React from 'react';

import { CollectionChooser } from '~/components';
import { ICollectionType } from '~/graphql';
import { useId } from '~/hooks';

import { Label } from './Label';

const types = [ICollectionType.Label];

export const Labels: React.FC = () => {
  const active = useId();

  return (
    <div tw="flex flex-1">
      <CollectionChooser
        filterEmpty
        active={active}
        collectionTypes={types}
        emptyString="labels"
        tw="flex-none"
        urlPrefix="/labels"
      />
      {active !== null && <Label active={active} />}
    </div>
  );
};
