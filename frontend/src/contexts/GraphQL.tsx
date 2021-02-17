import { ApolloClient, ApolloProvider, HttpLink, InMemoryCache } from '@apollo/client';
import * as React from 'react';

import { AuthorizationContext } from './Authorization';

const cache = new InMemoryCache();

type IProvider = React.FC<{ children: React.ReactNode }>;

export const GraphQLProvider: IProvider = ({ children }) => {
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

  const client = React.useMemo(() => new ApolloClient({ cache, link }), [link]);

  return <ApolloProvider client={client}>{children}</ApolloProvider>;
};
