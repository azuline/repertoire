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
      {!active && <Header />}
      <div className="flex flex-1">
        <CollectionChooser
          active={active}
          className="flex-none"
          collectionTypes={types}
          urlPrefix="/genres"
        />
        {active && <Genre active={active} />}
      </div>
    </>
  );
};
