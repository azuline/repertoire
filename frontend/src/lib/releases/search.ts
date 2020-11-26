import * as React from 'react';
import { QueryResult } from 'react-query';
import { PaginationT, useGQLQuery, ViewOptionsT } from 'src/hooks';
import { RELEASE_FIELDS } from 'src/lib/fragments';
import { GraphQLError, ReleaseSort, ReleaseT, ReleaseType, RequestError } from 'src/types';

const QUERY = `
  query (
    $search: String
    $collectionIds: [Int]
    $artistIds: [Int]
    $releaseTypes: [ReleaseType]
    $page: Int
    $perPage: Int
    $sort: ReleaseSort
    $asc: Boolean
  ) {
    releases(
      search: $search
      collectionIds: $collectionIds
      artistIds: $artistIds
      releaseTypes: $releaseTypes
      page: $page
      perPage: $perPage
      sort: $sort
      asc: $asc
    ) {
      total
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

type ResultT = { releases: { total: number; results: ReleaseT[] } };
type VariablesT = {
  search: string;
  collectionIds: number[];
  artistIds: number[];
  releaseTypes: ReleaseType[];
  sort: ReleaseSort;
  asc: boolean;
  page: number;
  perPage: number;
};

/**
 * A wrapper around react-query to search for releases on the backend.
 *
 * @param viewOptions The view options parameters for the query.
 * @param pagination The pagination for the query.
 * @returns The react-query result.
 */
export const searchReleases = (
  viewOptions: ViewOptionsT,
  pagination: PaginationT,
): QueryResult<ResultT, RequestError<GraphQLError>> => {
  // prettier-ignore
  const variables = React.useMemo(
    () => extractVariables(viewOptions, pagination),
    [viewOptions, pagination]
  );

  return useGQLQuery<ResultT, VariablesT>('releases', QUERY, variables);
};

/**
 * Extract variables from viewOptions and pagination to form the query variables.
 *
 * @param root0
 * @param root0.search
 * @param root0.collectionIds
 * @param root0.artistIds
 * @param root0.releaseTypes
 * @param root0.sort
 * @param root0.asc
 * @param root1
 * @param root1.curPage
 * @param root1.perPage
 */
const extractVariables = (
  { search, collectionIds, artistIds, releaseTypes, sort, asc }: ViewOptionsT,
  { curPage, perPage }: PaginationT,
): VariablesT => ({
  search,
  collectionIds,
  artistIds,
  releaseTypes,
  sort,
  asc,
  perPage,
  page: curPage,
});
