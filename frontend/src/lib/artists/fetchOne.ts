import { ArtistT, GraphQLError, RequestError } from 'src/types';

import { ARTIST_FIELDS } from 'src/lib/fragments';
import { QueryResult } from 'react-query';
import { useGQLQuery } from 'src/hooks';

const FETCH_ARTIST_QUERY = `
  query ($id: Int!) {
		artist (id: $id) {
      ${ARTIST_FIELDS}
		}
	}
`;

type Result = { artist: ArtistT };
type Variables = { id: number };
type Return = QueryResult<Result, RequestError<GraphQLError>>;

export const fetchArtist = (variables: Variables): Return => {
  return useGQLQuery<Result, Variables>('artist', FETCH_ARTIST_QUERY, variables);
};
