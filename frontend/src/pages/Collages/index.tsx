import * as React from 'react';

import { CollectionChooser } from '~/components';
import { ICollectionType } from '~/graphql';
import { useId } from '~/hooks';

import { Collage } from './Collage';

const types = [ICollectionType.System, ICollectionType.Collage];

export const Collages: React.FC = () => {
  const active = useId();

  return (
    <div tw="flex flex-1">
      <CollectionChooser
        active={active}
        collectionTypes={types}
        emptyString="collages"
        tw="flex-none"
        urlPrefix="/collages"
      />
      {active !== null && <Collage active={active} />}
    </div>
  );
};
