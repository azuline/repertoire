import 'twin.macro';

import * as React from 'react';

import { CollectionChooser, Header } from '~/components';
import { ICollectionType } from '~/graphql';
import { useId } from '~/hooks';

import { Label } from './Label';

const types = [ICollectionType.Label];

export const Labels: React.FC = () => {
  const active = useId();

  return (
    <>
      {!active && <Header />}
      <div tw="flex flex-1">
        <CollectionChooser
          active={active}
          collectionTypes={types}
          tw="flex-none"
          urlPrefix="/labels"
        />
        {active && <Label active={active} />}
      </div>
    </>
  );
};
