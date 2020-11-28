import { gql, QueryHookOptions, QueryResult, useQuery } from '@apollo/client';
import * as React from 'react';
import { FULL_RELEASE_FIELDS } from 'src/lib/fragments';
import { ReleaseT } from 'src/types';

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

export const fetchRelease = (id: number, options?: QueryHookOptions<T, V>): QueryResult<T, V> => {
  const newOptions = React.useMemo(() => ({ ...options, variables: { id } }), [options, id]);

  return useQuery<T, V>(QUERY, newOptions);
};
