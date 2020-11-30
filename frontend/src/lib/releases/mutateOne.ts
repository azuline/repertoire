import { gql, MutationHookOptions, MutationTuple, useMutation } from '@apollo/client';
import { FULL_RELEASE_FIELDS } from 'src/lib/fragments';
import { ReleaseT, ReleaseType } from 'src/types';

const MUTATION = gql`
  mutation(
    $id: Int!
    $title: String
    $releaseType: ReleaseType
    $releaseYear: Int
    $releaseDate: String
    $rating: Int
  ) {
    updateRelease(
      id: $id
      title: $title
      releaseType: $releaseType
      releaseYear: $releaseYear
      releaseDate: $releaseDate
      rating: $rating
    ) {
      ...FullReleaseFields
    }
  }
  ${FULL_RELEASE_FIELDS}
`;

type T = { release: ReleaseT };
type V = {
  id: number;
  title?: string;
  releaseType?: ReleaseType;
  releaseYear?: number;
  releaseDate?: string;
  rating?: number;
};

export const useMutateRelease = (options?: MutationHookOptions<T, V>): MutationTuple<T, V> =>
  useMutation<T, V>(MUTATION, options);
