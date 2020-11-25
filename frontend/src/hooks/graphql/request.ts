import * as React from 'react';
import { AuthorizationContext } from 'src/contexts';
import { GraphQLError, RequestError } from 'src/types';

type GQLRequest<T, V> = (query: string, variables?: V) => Promise<T>;

export const useGQLRequest = <T, V = undefined>(): GQLRequest<T, V> => {
  const { csrf } = React.useContext(AuthorizationContext);
  const { loggedIn, setLoggedIn } = React.useContext(AuthorizationContext);

  const rawGqlQuery = React.useCallback(
    async (query: string, variables?: V): Promise<T> => {
      if (!loggedIn) {
        throw new RequestError('Not logged in.');
      }

      const response = await fetch('/graphql', {
        method: 'POST',
        credentials: 'same-origin',
        body: JSON.stringify({
          query: query,
          variables: variables,
        }),
        headers: new Headers({
          'X-CSRF-Token': csrf ?? '',
          'Content-Type': 'application/json',
        }),
      });

      if (response.status == 401) {
        setLoggedIn(false);
        throw new RequestError('Failed to authenticate.');
      }

      const gqlData = await response.json();

      if (gqlData.errors) {
        throw new RequestError<GraphQLError>('GraphQL Error', gqlData.errors);
      }

      return gqlData.data;
    },
    [csrf, loggedIn, setLoggedIn],
  );

  return rawGqlQuery;
};
