import { gql, MutationHookOptions, QueryResult, useQuery } from '@apollo/client';

import { USER_FIELDS } from '~/lib/fragments';
import { UserT } from '~/types';

const QUERY = gql`
  query {
    user {
      ...UserFields
    }
  }
  ${USER_FIELDS}
`;

type T = { user: UserT };

export const useFetchUser = (options?: MutationHookOptions<T>): QueryResult<T> =>
  useQuery<T>(QUERY, options);
