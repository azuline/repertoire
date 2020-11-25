import * as React from 'react';

import { GraphQLError, RequestError } from 'src/types';
import { QueryKey, QueryResult, useQuery } from 'react-query';

import { AuthorizationContext } from 'src/contexts';
import { useGQLRequest } from './request';
import { useToasts } from 'react-toast-notifications';

type Error = RequestError<GraphQLError>;

export const useGQLQuery = <T, V = undefined>(
  cacheKey: QueryKey,
  query: string,
  variables?: V,
): QueryResult<T, Error> => {
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
