import * as React from 'react';

import { GraphQLError, RequestError } from 'src/types';
import { MutationConfig, MutationResultPair, useMutation } from 'react-query';

import { AuthorizationContext } from 'src/contexts';
import { useGQLRequest } from './request';
import { useToasts } from 'react-toast-notifications';

type Error = RequestError<GraphQLError>;
type Return<T, V> = MutationResultPair<T, Error, V, unknown>;
type Config<T, V> = MutationConfig<T, Error, V, unknown>;

export const useGQLMutation = <T, V>(query: string, config?: Config<T, V>): Return<T, V> => {
  const { addToast } = useToasts();
  const { loggedIn } = React.useContext(AuthorizationContext);
  const rawQuery = useGQLRequest<T, V>();

  const handler = React.useCallback(
    async (variables) => {
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
    },
    [addToast, loggedIn, rawQuery],
  );

  return useMutation(handler, config);
};
