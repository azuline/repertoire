import { GraphQLClient } from 'graphql-request';
import { API_URL } from 'src/constants';

export const createGQLClient = (token: string | null): GraphQLClient => {
  return new GraphQLClient(`${API_URL}/graphql`, {
    headers: { authorization: token ? `Token ${token}` : '' },
  });
};
