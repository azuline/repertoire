import 'twin.macro';

import * as React from 'react';

import { CollectionReleases, Header, SectionHeader } from '~/components';
import { BackgroundContext } from '~/contexts';
import { useFetchCollectionQuery } from '~/graphql';
import { ErrorPage } from '~/pages';

type ILabel = React.FC<{ active: number }>;

export const Label: ILabel = ({ active }) => {
  const { data, error } = useFetchCollectionQuery({ variables: { id: active } });
  const { setBackgroundImageId } = React.useContext(BackgroundContext);

  const collection = data?.collection || null;

  React.useEffect(() => {
    if (!collection) return;

    setBackgroundImageId(collection.imageId);
    return (): void => setBackgroundImageId(null);
  }, [collection, setBackgroundImageId]);

  if (error) {
    const errors = error.graphQLErrors.map(({ message }) => message);
    return <ErrorPage errors={errors} title="Could not fetch label." />;
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
