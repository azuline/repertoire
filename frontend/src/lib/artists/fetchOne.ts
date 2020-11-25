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
type Return = QueryResult<Result, RequestError<GraphQLError>>;

export const fetchArtist = (variables: Variables): Return => {
  return useGQLQuery<Result, Variables>('artist', QUERY, variables);
};
