import { QueryResult } from 'react-query';
import { useGQLQuery } from 'src/hooks';
import { GraphQLError, ReleaseT, RequestError } from 'src/types';

import { RELEASE_FIELDS } from './fragments';

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

type ResultT = { releases: { results: ReleaseT[] } };

/**
 * A wrapper around react-query to fetch the 10 most recently added releases.
 *
 * @return The react-query result.
 */
export const fetchRecentlyAdded = (): QueryResult<ResultT, RequestError<GraphQLError>> =>
  useGQLQuery<ResultT>('recently-added', QUERY);
