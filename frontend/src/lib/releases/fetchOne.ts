import { gql, QueryHookOptions, QueryResult, useQuery } from '@apollo/client';
import { FULL_RELEASE_FIELDS } from '~/lib/fragments';
import { ReleaseT } from '~/types';

const QUERY = gql`
  query($id: Int!) {
    release(id: $id) {
      ...FullReleaseFields
    }
  }
  ${FULL_RELEASE_FIELDS}
`;

type T = { release: ReleaseT };
type V = { id: number };

export const useFetchRelease = (
  id: number,
  options?: QueryHookOptions<T, V>,
): QueryResult<T, V> => {
  const newOptions = { ...options, variables: { id } };
  return useQuery<T, V>(QUERY, newOptions);
};
