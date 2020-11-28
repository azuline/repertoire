import { gql, MutationHookOptions, MutationTuple, useMutation } from '@apollo/client';
import { COLLECTION_FIELDS } from 'src/lib/fragments';
import { CollectionT } from 'src/types';

const MUTATION = gql`
  mutation($id: Int!, $name: String, $starred: Boolean) {
    updateCollection(id: $id, name: $name, starred: $starred) {
      ...CollectionFields
    }
  }
  ${COLLECTION_FIELDS}
`;

type T = { collection: CollectionT };
type V = { id: number; name?: string; starred?: boolean };

export const useMutateCollection = (options?: MutationHookOptions<T, V>): MutationTuple<T, V> =>
  useMutation(MUTATION, options);
