import * as React from 'react';
import { useQueryCache } from 'react-query';
import { useGQLMutation } from 'src/hooks';
import { COLLECTION_FIELDS } from 'src/lib/fragments';
import { updateMutationConfig } from 'src/lib/util';
import { CollectionT, MutationHook } from 'src/types';

const QUERY = `
  mutation (
    $collectionId: Int!
    $releaseId: Int!
  ) {
    delReleaseFromCollection (
      collectionId: $collectionId
      releaseId: $releaseId
    ) {
      ${COLLECTION_FIELDS}
    }
  }
`;

type ResultT = { collection: CollectionT };
export type DelReleaseFromCollectionVariablesT = { collectionId: number; releaseId: number };

/**
 * A wrapper around react-query to delete a release from a collection.
 *
 * React-Query's  ``mutate`` function takes a variable of type ``DelReleaseToCollectionVariablesT``.
 *
 * @returns The react-query mutation result.
 */
export const useDelReleaseFromCollection: MutationHook<
  ResultT,
  DelReleaseFromCollectionVariablesT
> = (config = {}) => {
  const queryCache = useQueryCache();

  const onSuccess = React.useCallback(() => {
    queryCache.invalidateQueries('collections');
    queryCache.invalidateQueries('releases');
  }, [queryCache]);

  const newConfig = updateMutationConfig(config, { onSuccess });

  return useGQLMutation<ResultT, DelReleaseFromCollectionVariablesT>(QUERY, newConfig);
};
