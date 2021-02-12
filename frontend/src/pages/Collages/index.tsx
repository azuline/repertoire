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
      <div className="flex flex-1">
        <CollectionChooser
          active={active}
          className="flex-none"
          collectionTypes={types}
          urlPrefix="/collages"
        />
        {active && <Collage active={active} />}
      </div>
    </>
  );
};
