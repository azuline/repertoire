import * as React from 'react';
import { MutationConfig, MutationResultPair, useMutation } from 'react-query';
import { useToasts } from 'react-toast-notifications';
import { AuthorizationContext } from 'src/contexts';
import { GraphQLError, RequestError } from 'src/types';

import { useGQLRequest } from './request';

type ErrorT = RequestError<GraphQLError>;
type ConfigT<T, V> = MutationConfig<T, ErrorT, V, unknown>;

/**
 * A wrapper around react-query's useMutation that makes a GraphQL mutation request to the backend.
 *
 * @param mutation - The GraphQL mutation.
 * @param config - The Config object to pass into react-query's ``useMutation``.
 * @returns The react-query mutation result pair.
 */
export const useGQLMutation = <T, V>(
  mutation: string,
  config?: ConfigT<T, V>,
): MutationResultPair<T, ErrorT, V, unknown> => {
  const { addToast } = useToasts();
  const { loggedIn } = React.useContext(AuthorizationContext);
  const rawQuery = useGQLRequest<T, V>();

  const handler = React.useCallback(
    async (variables) => {
      if (!loggedIn) {
        throw new RequestError('Not logged in.');
      }

      try {
        return await rawQuery(mutation, variables);
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
