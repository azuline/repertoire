import { gql, QueryHookOptions, QueryResult, useQuery } from '@apollo/client';
import { COLLECTION_FIELDS } from 'src/lib/fragments';
import { CollectionT, CollectionType } from 'src/types';

const QUERY = gql`
  query($types: [CollectionType]) {
    collections(types: $types) {
      results {
        ...CollectionFields
      }
    }
  }
  ${COLLECTION_FIELDS}
`;

type T = { collections: { results: CollectionT[] } };
type V = { types: CollectionType[] };

export const useFetchCollections = (
  types: CollectionType[] = [],
  options?: QueryHookOptions<T, V>,
): QueryResult<T, V> => {
  const newOptions = { ...options, variables: { types } };
  return useQuery<T, V>(QUERY, newOptions);
};
