import { gql } from '@apollo/client';
import * as React from 'react';

import { CollectionReleases, Header, SectionHeader } from '~/components';
import { BackgroundContext } from '~/contexts';
import { useGenresFetchGenreQuery } from '~/graphql';
import { ErrorPage } from '~/pages';

type IGenre = React.FC<{ active: number }>;

export const Genre: IGenre = ({ active }) => {
  const { data, error } = useGenresFetchGenreQuery({ variables: { id: active } });
  const { setBackgroundImageId } = React.useContext(BackgroundContext);

  const collection = data?.collection;

  React.useEffect(() => {
    if (!collection) {
      return;
    }

    setBackgroundImageId(collection.imageId);
    return (): void => setBackgroundImageId(null);
  }, [collection, setBackgroundImageId]);

  if (error) {
    const errors = error.graphQLErrors.map(({ message }) => message);
    return <ErrorPage errors={errors} title="Could not fetch genre." />;
  }

  if (!collection) {
    return null;
  }

  return (
    <div tw="flex flex-col w-full">
      <Header />
      <SectionHeader tw="mt-4 mb-8">{collection.name}</SectionHeader>
      <CollectionReleases active={active} />
    </div>
  );
};

/* eslint-disable */
gql`
  query GenresFetchGenre($id: Int!) {
    collection(id: $id) {
      ...CollectionFields
    }
  }
`;
