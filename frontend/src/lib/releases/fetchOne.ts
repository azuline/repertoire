import { GraphQLError, ReleaseT, RequestError } from 'src/types';
import { useGQLQuery } from 'src/hooks';

import { QueryResult } from 'react-query';
import { RELEASE_FIELDS, TRACK_FIELDS } from 'src/lib/fragments';

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

type Result = { release: ReleaseT };
type Variables = { id: number };
type Return = QueryResult<Result, RequestError<GraphQLError>>;

export const fetchRelease = (id: number): Return => {
  return useGQLQuery<Result, Variables>('releases', QUERY, { id });
};
