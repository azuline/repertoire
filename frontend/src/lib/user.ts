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

type Result = { user: UserT };
type Return = QueryResult<Result, RequestError<GraphQLError>>;

export const fetchUser = (): Return => useGQLQuery<Result>('releases', QUERY);
