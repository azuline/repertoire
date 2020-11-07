import { ArtistT, GraphQLError, RequestError } from 'src/types';

import { ARTIST_FIELDS } from './fragments';
import { QueryResult } from 'react-query';
import { useGQLQuery } from 'src/hooks';

const QUERY = `
  query ($id: Int!) {
		artist (id: $id) {
      ${ARTIST_FIELDS}
		}
	}
`;

type ResultType = { artist: ArtistT };

type Variables = { id: number };

export const fetchArtist = (id: number): QueryResult<ResultType, RequestError<GraphQLError>> => {
  return useGQLQuery<ResultType, Variables>('artist', QUERY, { variables: { id } });
};
