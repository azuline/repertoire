import * as React from 'react';

import { CollectionChooser } from '~/components';
import { ICollectionType } from '~/graphql';
import { useId } from '~/hooks';
import { Layout } from '~/layout';

import { Genre } from './Genre';

const types = [ICollectionType.Genre];

export const Genres: React.FC = () => {
  const active = useId();

  return (
    <Layout tw="flex flex-1">
      <CollectionChooser
        filterEmpty
        active={active}
        collectionTypes={types}
        emptyString="genres"
        tw="flex-none"
        urlPrefix="/genres"
      />
      {active !== null && (
        <Layout pad scroll>
          <Genre active={active} />
        </Layout>
      )}
    </Layout>
  );
};
