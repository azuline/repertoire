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
type Return = QueryResult<Result, RequestError<GraphQLError>>;

export const fetchArtists = (): Return => useGQLQuery<Result>('artists', QUERY);
