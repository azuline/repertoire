import { ArtistT, GraphQLError, RequestError } from 'src/types';

import { ARTIST_FIELDS } from 'src/fragments';
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

type ResultType = { artists: { results: ArtistT[] } };

export const fetchArtists = (): QueryResult<ResultType, RequestError<GraphQLError>> => {
  return useGQLQuery<ResultType>('artists', QUERY);
};
