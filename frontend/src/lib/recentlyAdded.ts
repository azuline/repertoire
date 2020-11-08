import { GraphQLError, ReleaseT, RequestError } from 'src/types';

import { QueryResult } from 'react-query';
import { RELEASE_FIELDS } from './fragments';
import { useGQLQuery } from 'src/hooks';

const QUERY = `
	query {
		releases(
			sort: RECENTLY_ADDED
			asc: false
			page: 1
			perPage: 10
		) {
			results {
				${RELEASE_FIELDS}
				artists {
				  id
					name
				}
        labels {
          id
          name
        }
        genres {
          id
          name
        }
			}
		}
	}
`;

type ResultType = { releases: { results: ReleaseT[] } };

export const fetchRecentlyAdded = (): QueryResult<ResultType, RequestError<GraphQLError>> => {
  return useGQLQuery<ResultType>('recently-added', QUERY);
};
