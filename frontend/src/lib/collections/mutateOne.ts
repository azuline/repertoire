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

type Result = { collection: CollectionT };
type Variables = { id: number; name?: string; starred?: boolean };
type Return = MutationResultPair<Result, RequestError<GraphQLError>, Variables, unknown>;

export const useMutateCollection = (): Return => {
  const queryCache = useQueryCache();

  const onSuccess = React.useCallback(() => queryCache.invalidateQueries('collections'), [
    queryCache,
  ]);

  return useGQLMutation<Result, Variables>(QUERY, { onSuccess });
};
