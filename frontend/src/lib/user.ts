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

type ResultType = { user: UserT };

export const fetchUser = (): QueryResult<ResultType, RequestError<GraphQLError>> => {
  return useGQLQuery<ResultType>('releases', QUERY);
};
