import { gql, QueryHookOptions, QueryResult, useQuery } from '@apollo/client';
import { ARTIST_FIELDS } from '~/lib/fragments';
import { ArtistT } from '~/types';

const QUERY = gql`
  query($id: Int!) {
    artist(id: $id) {
      ...ArtistFields
    }
  }
  ${ARTIST_FIELDS}
`;

type T = { artist: ArtistT };
type V = { id: number };

export const useFetchArtist = (id: number, options?: QueryHookOptions<T, V>): QueryResult<T, V> => {
  const newOptions = { ...options, variables: { id } };
  return useQuery<T, V>(QUERY, newOptions);
};
