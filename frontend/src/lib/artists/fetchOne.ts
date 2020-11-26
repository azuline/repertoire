import { QueryResult } from 'react-query';
import { useGQLQuery } from 'src/hooks';
import { ARTIST_FIELDS } from 'src/lib/fragments';
import { ArtistT, GraphQLError, RequestError } from 'src/types';

const QUERY = `
  query ($id: Int!) {
    artist (id: $id) {
      ${ARTIST_FIELDS}
    }
  }
`;

type Result = { artist: ArtistT };
type Variables = { id: number };

/**
 * A wrapper around react-query to fetch a single artist.
 *
 * @param id The ID of the artist to fetch.
 * @return The react-query result.
 */
export const fetchArtist = (
  variables: Variables,
): QueryResult<Result, RequestError<GraphQLError>> =>
  useGQLQuery<Result, Variables>('artist', QUERY, variables);
