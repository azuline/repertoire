import { gql, MutationHookOptions, MutationTuple, useMutation } from '@apollo/client';
import { COLLECTION_FIELDS } from 'src/lib/fragments';
import { CollectionT } from 'src/types';

const MUTATION = gql`
  mutation($collectionId: Int!, $releaseId: Int!) {
    addReleaseToCollection(collectionId: $collectionId, releaseId: $releaseId) {
      ...CollectionFields
    }
  }
  ${COLLECTION_FIELDS}
`;

type T = { collection: CollectionT };
type V = { collectionId: number; releaseId: number };

export const useAddReleaseToCollection = (
  options?: MutationHookOptions<T, V>,
): MutationTuple<T, V> => useMutation<T, V>(MUTATION, options);
