import * as React from 'react';

import { CollectionChooser, Header } from '~/components';
import { ICollectionType } from '~/graphql';
import { useId } from '~/hooks';

import { Genre } from './Genre';

const types = [ICollectionType.Genre];

export const Genres: React.FC = () => {
  const active = useId();

  return (
    <>
      {active === null && <Header />}
      <div tw="flex flex-1">
        <CollectionChooser
          filterEmpty
          active={active}
          collectionTypes={types}
          tw="flex-none"
          urlPrefix="/genres"
        />
        {active !== null && <Genre active={active} />}
      </div>
    </>
  );
};
