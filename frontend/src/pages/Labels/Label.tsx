import { gql } from '@apollo/client';
import * as React from 'react';

import { CollectionReleases, Header, SectionHeader } from '~/components';
import { BackgroundContext } from '~/contexts';
import { useLabelFetchLabelQuery } from '~/graphql';
import { AuthenticatedError } from '~/pages';

type ILabel = React.FC<{ active: number }>;

export const Label: ILabel = ({ active }) => {
  const { data, error } = useLabelFetchLabelQuery({ variables: { id: active } });
  const { setBackgroundImageId } = React.useContext(BackgroundContext);

  const collection = data?.collection;

  React.useEffect(() => {
    if (!collection) {
      return;
    }

    setBackgroundImageId(collection.imageId);
    return (): void => setBackgroundImageId(null);
  }, [collection]);

  if (error) {
    const errors = error.graphQLErrors.map(({ message }) => message);
    return <AuthenticatedError errors={errors} title="Could not fetch label." />;
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
  query LabelFetchLabel($id: Int!) {
    collection(id: $id) {
      ...CollectionFields
    }
  }
`;
