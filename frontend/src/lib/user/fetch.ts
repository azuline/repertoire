import { useGQLQuery } from 'src/hooks';
import { USER_FIELDS } from 'src/lib/fragments';
import { QueryReturn, UserT } from 'src/types';

const QUERY = `
  query {
    user {
      ${USER_FIELDS}
    }
  }
`;

type ResultT = { user: UserT };

/**
 * A wrapper around react-query to fetch the current logged-in user.
 *
 * @returns The react-query result.
 */
export const fetchUser = (): QueryReturn<ResultT> => useGQLQuery<ResultT>('user', QUERY);
