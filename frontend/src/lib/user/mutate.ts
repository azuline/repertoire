import { gql, MutationHookOptions, MutationTuple, useMutation } from '@apollo/client';

import { USER_FIELDS } from '~/lib/fragments';
import { UserT } from '~/types';

const MUTATION = gql`
  mutation($nickname: String) {
    updateUser(nickname: $nickname) {
      ...UserFields
    }
  }
  ${USER_FIELDS}
`;

type T = { user: UserT };
type V = { nickname: string };

export const useMutateUser = (options?: MutationHookOptions<T, V>): MutationTuple<T, V> =>
  useMutation<T, V>(MUTATION, options);
