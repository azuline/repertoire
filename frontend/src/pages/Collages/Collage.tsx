import 'twin.macro';

import { gql } from '@apollo/client';
import * as React from 'react';

import { CollectionReleases, Header, SectionHeader } from '~/components';
import { BackgroundContext } from '~/contexts';
import { useCollageFetchCollageQuery } from '~/graphql';

type ICollage = React.FC<{ active: number }>;

export const Collage: ICollage = ({ active }) => {
  const { data } = useCollageFetchCollageQuery({ variables: { id: active } });
  const { setBackgroundImageId } = React.useContext(BackgroundContext);

  const collection = data?.collection;

  React.useEffect(() => {
    if (!collection) return;

    setBackgroundImageId(collection.imageId);
    return (): void => setBackgroundImageId(null);
  }, [collection, setBackgroundImageId]);

  if (!collection) return null;

  return (
    <div tw="flex flex-col w-full">
      <Header />
      <div>
        <SectionHeader tw="mt-4 mb-8">{collection.name}</SectionHeader>
        <CollectionReleases active={active} />
      </div>
    </div>
  );
};

/* eslint-disable */
gql`
  query CollageFetchCollage($id: Int!) {
    collection(id: $id) {
      ...CollectionFields
    }
  }
`;
