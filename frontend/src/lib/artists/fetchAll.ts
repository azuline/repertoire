import { QueryResult } from 'react-query';
import { useGQLQuery } from 'src/hooks';
import { ARTIST_FIELDS } from 'src/lib/fragments';
import { ArtistT, GraphQLError, RequestError } from 'src/types';

const QUERY = `
  query {
    artists {
      results {
        ${ARTIST_FIELDS}
      }
    }
  }
`;

type Result = { artists: { results: ArtistT[] } };

/**
 * A wrapper around react-query to fetch all artists.
 *
 * @returns The react-query result.
 */
export const fetchArtists = (): QueryResult<Result, RequestError<GraphQLError>> =>
  useGQLQuery<Result>('artists', QUERY);
