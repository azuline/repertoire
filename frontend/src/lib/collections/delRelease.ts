import { gql, MutationHookOptions, MutationTuple, useMutation } from '@apollo/client';

import { COLLECTION_FIELDS, RELEASE_FIELDS } from '~/lib/fragments';
import { CollectionT } from '~/types';

const MUTATION = gql`
  mutation($collectionId: Int!, $releaseId: Int!) {
    delReleaseFromCollection(collectionId: $collectionId, releaseId: $releaseId) {
      collection {
        ...CollectionFields
      }
      release {
        ...ReleaseFields
      }
    }
  }
  ${COLLECTION_FIELDS}
  ${RELEASE_FIELDS}
`;

type T = { collection: CollectionT };
export type V = { collectionId: number; releaseId: number };

export const useDelReleaseFromCollection = (
  options?: MutationHookOptions<T, V>,
): MutationTuple<T, V> => useMutation(MUTATION, options);
