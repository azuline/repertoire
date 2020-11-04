import { GraphQLError, UserT, RequestError } from 'src/types';
import { useGQLQuery } from 'src/hooks';

import { QueryResult } from 'react-query';

const QUERY = `
  query {
    user {
      id
      username
    }
  }
`;

type ResultType = { user: UserT };

export const fetchUser = (): QueryResult<ResultType, RequestError<GraphQLError>> => {
  return useGQLQuery<ResultType>('releases', QUERY);
};
