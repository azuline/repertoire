import { gql } from '@apollo/client';
import * as React from 'react';

import { Chooser, IToggleStarFactory } from '~/components/Chooser';
import {
  ICollectionType,
  useCollectionChooserFetchCollectionsQuery,
  useCollectionChooserUpdateCollectionStarredMutation,
} from '~/graphql';

import { NoChooserOption } from '../NoChooserOption';

type ICollectionChooser = React.FC<{
  collectionTypes: ICollectionType[];
  urlPrefix: string;
  active: number | null;
  className?: string;
  emptyString: string;
  filterEmpty?: boolean;
}>;

export const CollectionChooser: ICollectionChooser = ({
  collectionTypes,
  urlPrefix,
  active,
  className,
  emptyString,
  filterEmpty = false,
}) => {
  const { data, error, loading } = useCollectionChooserFetchCollectionsQuery({
    variables: { types: collectionTypes },
  });
  const [mutateCollection] = useCollectionChooserUpdateCollectionStarredMutation();

  const urlFactory = (id: number): string => `${urlPrefix}/${id}`;

  const toggleStarFactory: IToggleStarFactory = ({ id, starred, type }) => {
    if (type === 'SYSTEM') {
      return;
    }

    return async (): Promise<void> => {
      await mutateCollection({ variables: { id, starred: starred !== true } });
    };
  };

  if (!data || loading || error) {
    return null;
  }

  const { results } = data.collections;

  const collections = filterEmpty
    ? results.filter((col) => col.numReleases !== 0)
    : results;

  if (collections.length === 0) {
    return <NoChooserOption>No {emptyString} :(</NoChooserOption>;
  }

  return (
    <Chooser
      active={active}
      className={className}
      results={collections}
      toggleStarFactory={toggleStarFactory}
      urlFactory={urlFactory}
    />
  );
};

/* eslint-disable */
gql`
  query CollectionChooserFetchCollections($types: [CollectionType!]) {
    collections(types: $types) {
      results {
        ...CollectionFields
      }
    }
  }

  mutation CollectionChooserUpdateCollectionStarred($id: Int!, $starred: Boolean) {
    updateCollection(id: $id, starred: $starred) {
      id
      starred
    }
  }
`;
