import * as React from 'react';
import { MutationResultPair, useQueryCache } from 'react-query';
import { useGQLMutation } from 'src/hooks';
import { COLLECTION_FIELDS } from 'src/lib/fragments';
import { CollectionT, GraphQLError, RequestError } from 'src/types';

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
 * @return The react-query mutation result.
 */
export const useMutateCollection = (): MutationResultPair<
  ResultT,
  RequestError<GraphQLError>,
  MutateOneCollectionVariablesT,
  unknown
> => {
  const queryCache = useQueryCache();

  const onSuccess = React.useCallback(() => queryCache.invalidateQueries('collections'), [
    queryCache,
  ]);

  return useGQLMutation<ResultT, MutateOneCollectionVariablesT>(QUERY, { onSuccess });
};
