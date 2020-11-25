import { ArtistT, GraphQLError, RequestError } from 'src/types';

import { ARTIST_FIELDS } from 'src/lib/fragments';
import { QueryResult } from 'react-query';
import { useGQLQuery } from 'src/hooks';

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

export const fetchArtists = (): Return => {
  return useGQLQuery<Result>('artists', QUERY);
};
