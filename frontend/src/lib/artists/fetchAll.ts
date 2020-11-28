import { useGQLQuery } from 'src/hooks';
import { ARTIST_FIELDS } from 'src/lib/fragments';
import { ArtistT, QueryReturn } from 'src/types';

const QUERY = `
  query {
    artists {
      results {
        ${ARTIST_FIELDS}
      }
    }
  }
`;

type ResultT = { artists: { results: ArtistT[] } };

/**
 * A wrapper around react-query to fetch all artists.
 *
 * @returns The react-query result.
 */
export const fetchArtists = (): QueryReturn<ResultT> => useGQLQuery<ResultT>('artists', QUERY);
