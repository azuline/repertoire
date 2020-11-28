import * as React from 'react';
import { useQueryCache } from 'react-query';
import { useGQLMutation } from 'src/hooks';
import { USER_FIELDS } from 'src/lib/fragments';
import { updateMutationConfig } from 'src/lib/util';
import { MutationHook, UserT } from 'src/types';

const QUERY = `
  mutation (
    $nickname: String
  ) {
    updateUser (
      nickname: $nickname
    ) {
      ${USER_FIELDS}
    }
  }
`;

type ResultT = { user: UserT };
export type MutateUserVariablesT = { nickname: string };

/**
 * A wrapper around react-query to mutate a single user.
 *
 * React-Query's  ``mutate`` function takes a variable of type ``MutateUserVariablesT``.
 *
 * @returns The react-query mutation result.
 */
export const useMutateUser: MutationHook<ResultT, MutateUserVariablesT> = (config = {}) => {
  const queryCache = useQueryCache();

  const onSuccess = React.useCallback(() => {
    queryCache.invalidateQueries('user');
  }, [queryCache]);

  const newConfig = updateMutationConfig(config, { onSuccess });

  return useGQLMutation<ResultT, MutateUserVariablesT>(QUERY, newConfig);
};
