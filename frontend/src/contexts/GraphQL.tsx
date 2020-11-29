import { ApolloClient, ApolloProvider, HttpLink, InMemoryCache } from '@apollo/client';
import * as React from 'react';

import { AuthorizationContext } from './Authorization';

export const GraphQLProvider: React.FC<{ children: React.ReactNode }> = ({ children }) => {
  const { csrf } = React.useContext(AuthorizationContext);

  const link = React.useMemo(
    () =>
      new HttpLink({
        credentials: 'same-origin',
        headers: { 'X-CSRF-Token': csrf as string },
        uri: '/graphql',
      }),
    [csrf],
  );

  const cache = React.useMemo(() => new InMemoryCache(), []);

  const client = React.useMemo(() => new ApolloClient({ cache, link }), [link, cache]);

  return <ApolloProvider client={client}>{children}</ApolloProvider>;
};
