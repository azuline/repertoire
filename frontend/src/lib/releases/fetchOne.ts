import { useGQLQuery } from 'src/hooks';
import { FULL_RELEASE_FIELDS } from 'src/lib/fragments';
import { QueryReturn, ReleaseT } from 'src/types';

const QUERY = `
  query ($id: Int!) {
    release (id: $id) {
      ${FULL_RELEASE_FIELDS}
    }
  }
`;

type ResultT = { release: ReleaseT };
type VariablesT = { id: number };

/**
 * A wrapper around react-query to fetch a single release.
 *
 * @param id - The ID of the release to fetch.
 * @returns The react-query result.
 */
export const fetchRelease = (id: number): QueryReturn<ResultT> =>
  useGQLQuery<ResultT, VariablesT>('releases', QUERY, { id });
