import { gql, QueryHookOptions, QueryResult, useQuery } from '@apollo/client';
import { ARTIST_FIELDS } from 'src/lib/fragments';
import { ArtistT } from 'src/types';

const QUERY = gql`
  query {
    artists {
      results {
        ...ArtistFields
      }
    }
  }
  ${ARTIST_FIELDS}
`;

type T = { artists: { results: ArtistT[] } };

export const useFetchArtists = (options?: QueryHookOptions<T>): QueryResult<T> =>
  useQuery<T>(QUERY, options);
