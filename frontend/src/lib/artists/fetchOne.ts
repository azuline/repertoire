import { useGQLQuery } from 'src/hooks';
import { ARTIST_FIELDS } from 'src/lib/fragments';
import { ArtistT, QueryReturn } from 'src/types';

const QUERY = `
  query ($id: Int!) {
    artist (id: $id) {
      ${ARTIST_FIELDS}
    }
  }
`;

type ResultT = { artist: ArtistT };
type VariablesT = { id: number };

/**
 * A wrapper around react-query to fetch a single artist.
 *
 * @param id - The ID of the artist to fetch.
 * @returns The react-query result.
 */
export const fetchArtist = (id: number): QueryReturn<ResultT> =>
  useGQLQuery<ResultT, VariablesT>('artist', QUERY, { id });
