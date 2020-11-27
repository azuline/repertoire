import * as React from 'react';
import { QueryKey, QueryResult, useQuery } from 'react-query';
import { useToasts } from 'react-toast-notifications';
import { AuthorizationContext } from 'src/contexts';
import { GraphQLError, RequestError } from 'src/types';

import { useGQLRequest } from './request';

type ErrorT = RequestError<GraphQLError>;

/**
 * A small wrapper around react-query's useQuery that makes a GraphQL query to the backend.
 *
 * The final cache key passed into ``useQuery`` will be calculated using the ``cacheKey`` and
 * ``variables`` parameters.
 *
 * @param cacheKey - The root cache key for the query.
 * @param query - The string GraphQL query.
 * @param variables - Variables for the query.
 * @returns A react-query query result.
 */
export const useGQLQuery = <T, V = undefined>(
  cacheKey: QueryKey,
  query: string,
  variables?: V,
): QueryResult<T, ErrorT> => {
  const { addToast } = useToasts();
  const { loggedIn } = React.useContext(AuthorizationContext);
  const rawQuery = useGQLRequest<T, V>();

  const handler = React.useCallback(async () => {
    if (!loggedIn) {
      throw new RequestError('Not logged in.');
    }

    try {
      return await rawQuery(query, variables);
    } catch (e) {
      e.errors.forEach(({ message }: { message: string }) => {
        addToast(message, { appearance: 'error' });
      });

      throw e;
    }
  }, [variables, addToast, loggedIn, rawQuery]);

  const queryKey = React.useMemo(() => [cacheKey, variables], [cacheKey, variables]);

  return useQuery(queryKey, handler);
};
