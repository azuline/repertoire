import { gql, MutationHookOptions, QueryResult, useQuery } from '@apollo/client';
import { USER_FIELDS } from 'src/lib/fragments';
import { UserT } from 'src/types';

const QUERY = gql`
  query {
    user {
      ...UserFields
    }
  }
  ${USER_FIELDS}
`;

type T = { user: UserT };

export const fetchUser = (options?: MutationHookOptions<T>): QueryResult<T> =>
  useQuery<T>(QUERY, options);
