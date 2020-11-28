import { gql, QueryHookOptions, QueryResult, useQuery } from '@apollo/client';
import * as React from 'react';
import { COLLECTION_FIELDS } from 'src/lib/fragments';
import { CollectionT } from 'src/types';

const QUERY = gql`
  query($id: Int!) {
    collection(id: $id) {
      ...CollectionFields
    }
  }
  ${COLLECTION_FIELDS}
`;

type T = { collection: CollectionT };
type V = { id: number };

export const fetchCollection = (
  id: number,
  options?: QueryHookOptions<T, V>,
): QueryResult<T, V> => {
  const newOptions = React.useMemo(() => ({ ...options, variables: { id } }), [options, id]);

  return useQuery<T, V>(QUERY, newOptions);
};
