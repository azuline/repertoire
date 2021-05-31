import * as React from 'react';

import { CollectionChooser } from '~/components';
import { ICollectionType } from '~/graphql';
import { useId } from '~/hooks';

import { Genre } from './Genre';

const types = [ICollectionType.Genre];

export const Genres: React.FC = () => {
  const active = useId();

  return (
    <div tw="flex flex-1">
      <CollectionChooser
        filterEmpty
        active={active}
        collectionTypes={types}
        emptyString="genres"
        tw="flex-none"
        urlPrefix="/genres"
      />
      {active !== null && <Genre active={active} />}
    </div>
  );
};
