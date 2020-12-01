import { gql, QueryHookOptions, QueryResult, useQuery } from '@apollo/client';

const QUERY = gql`
  query {
    releaseYears
  }
`;

type T = { releaseYears: number[] };

export const useFetchYears = (options?: QueryHookOptions<T>): QueryResult<T> => {
  return useQuery<T>(QUERY, options);
};
