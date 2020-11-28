import * as React from 'react';
import { useQueryCache } from 'react-query';
import { useGQLMutation } from 'src/hooks';
import { COLLECTION_FIELDS } from 'src/lib/fragments';
import { updateMutationConfig } from 'src/lib/util';
import { CollectionT, MutationHook } from 'src/types';

const QUERY = `
  mutation (
    $id: Int!
    $name: String
    $starred: Boolean
  ) {
    updateCollection (
      id: $id
      name: $name
      starred: $starred
    ) {
      ${COLLECTION_FIELDS}
    }
  }
`;

type ResultT = { collection: CollectionT };
export type MutateOneCollectionVariablesT = { id: number; name?: string; starred?: boolean };

/**
 * A wrapper around react-query to mutate a single collection.
 *
 * React-Query's  ``mutate`` function takes a variable of type ``MutateOneCollectionVariablesT``.
 *
 * @returns The react-query mutation result.
 */
export const useMutateCollection: MutationHook<ResultT, MutateOneCollectionVariablesT> = (
  config = {},
) => {
  const queryCache = useQueryCache();

  const onSuccess = React.useCallback(() => {
    queryCache.invalidateQueries('collections');
  }, [queryCache]);

  const newConfig = updateMutationConfig(config, { onSuccess });

  return useGQLMutation<ResultT, MutateOneCollectionVariablesT>(QUERY, newConfig);
};
