import { RequestError, GraphQLError, ArtistT } from 'src/types';
import { useGQLQuery } from 'src/hooks';

import { QueryResult } from 'react-query';
import { ARTIST_FIELDS } from 'src/fragments';

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
