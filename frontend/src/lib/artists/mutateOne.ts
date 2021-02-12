import { gql, MutationHookOptions, MutationTuple, useMutation } from '@apollo/client';
import { ARTIST_FIELDS } from '~/lib/fragments';
import { ArtistT } from '~/types';

const MUTATION = gql`
  mutation($id: Int!, $name: String, $starred: Boolean) {
    updateArtist(id: $id, name: $name, starred: $starred) {
      ...ArtistFields
    }
  }
  ${ARTIST_FIELDS}
`;

type T = { artist: ArtistT };
type V = { id: number; name?: string; starred?: boolean };

export const useMutateArtist = (options?: MutationHookOptions<T, V>): MutationTuple<T, V> =>
  useMutation(MUTATION, options);
