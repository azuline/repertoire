import { gql, QueryHookOptions, QueryResult, useQuery } from '@apollo/client';
import * as React from 'react';
import { ARTIST_FIELDS } from 'src/lib/fragments';
import { ArtistT } from 'src/types';

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
  const newOptions = React.useMemo(() => ({ ...options, variables: { id } }), [options, id]);

  return useQuery<T, V>(QUERY, newOptions);
};
