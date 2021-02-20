import * as React from 'react';

import { CollectionChooser, Header } from '~/components';
import { ICollectionType } from '~/graphql';
import { useId } from '~/hooks';

import { Collage } from './Collage';

const types = [ICollectionType.System, ICollectionType.Collage];

export const Collages: React.FC = () => {
  const active = useId();

  return (
    <>
      {!active && <Header />}
      <div tw="flex flex-1">
        <CollectionChooser
          active={active}
          collectionTypes={types}
          tw="flex-none"
          urlPrefix="/collages"
        />
        {active && <Collage active={active} />}
      </div>
    </>
  );
};
