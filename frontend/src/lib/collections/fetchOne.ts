import { gql, QueryHookOptions, QueryResult, useQuery } from '@apollo/client';
import { COLLECTION_FIELDS } from '~/lib/fragments';
import { CollectionT } from '~/types';

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

export const useFetchCollection = (
  id: number,
  options?: QueryHookOptions<T, V>,
): QueryResult<T, V> => {
  const newOptions = { ...options, variables: { id } };
  return useQuery<T, V>(QUERY, newOptions);
};
