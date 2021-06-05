import * as React from 'react';

import { CollectionChooser } from '~/components';
import { ICollectionType } from '~/graphql';
import { useId } from '~/hooks';
import { Layout } from '~/layout';

import { Label } from './Label';

const types = [ICollectionType.Label];

export const Labels: React.FC = () => {
  const active = useId();

  return (
    <Layout tw="flex flex-1">
      <CollectionChooser
        filterEmpty
        active={active}
        collectionTypes={types}
        emptyString="labels"
        tw="flex-none"
        urlPrefix="/labels"
      />
      {active !== null && (
        <Layout padX padY scroll>
          <Label active={active} />
        </Layout>
      )}
    </Layout>
  );
};
