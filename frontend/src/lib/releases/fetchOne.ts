import { QueryResult } from 'react-query';
import { useGQLQuery } from 'src/hooks';
import { RELEASE_FIELDS, TRACK_FIELDS } from 'src/lib/fragments';
import { GraphQLError, ReleaseT, RequestError } from 'src/types';

const QUERY = `
  query ($id: Int!) {
    release (id: $id) {
      ${RELEASE_FIELDS}
      artists {
        id
        name
      }
      collages {
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
      tracks {
        ${TRACK_FIELDS}
        release {
          id
          hasCover
        }
        artists {
          artist {
            id
            name
          }
          role
        }
      }
    }
  }
`;

type ResultT = { release: ReleaseT };
type VariablesT = { id: number };

/**
 * A wrapper around react-query to fetch a single release.
 *
 * @param id The ID of the release to fetch.
 * @return The react-query result.
 */
export const fetchRelease = (id: number): QueryResult<ResultT, RequestError<GraphQLError>> =>
  useGQLQuery<ResultT, VariablesT>('releases', QUERY, { id });
