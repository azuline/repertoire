import { gql, MutationHookOptions, QueryResult, useQuery } from '@apollo/client';
import { RELEASE_FIELDS } from 'src/lib/fragments';
import { ReleaseT } from 'src/types';

const QUERY = gql`
  query {
    releases(sort: RECENTLY_ADDED, asc: false, page: 1, perPage: 10) {
      results {
        ...ReleaseFields
        artists {
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
  ${RELEASE_FIELDS}
`;

type T = { releases: { results: ReleaseT[] } };

export const fetchRecentlyAdded = (options?: MutationHookOptions<T>): QueryResult<T> =>
  useQuery<T>(QUERY, options);
