import { QueryResult } from 'react-query';
import { useGQLQuery } from 'src/hooks';
import { GraphQLError, RequestError, UserT } from 'src/types';

const QUERY = `
  query {
    user {
      id
      username
    }
  }
`;

type ResultT = { user: UserT };

/**
 * A wrapper around react-query to fetch the current logged-in user.
 *
 * @return The react-query result.
 */
export const fetchUser = (): QueryResult<ResultT, RequestError<GraphQLError>> =>
  useGQLQuery<ResultT>('user', QUERY);
