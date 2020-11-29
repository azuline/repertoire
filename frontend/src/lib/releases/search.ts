import { gql, QueryHookOptions, QueryResult, useQuery } from '@apollo/client';
import * as React from 'react';
import { PaginationT, ViewOptionsT } from 'src/hooks';
import { RELEASE_FIELDS } from 'src/lib/fragments';
import { ReleaseSort, ReleaseT, ReleaseType } from 'src/types';

const QUERY = gql`
  query(
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

type T = { releases: { total: number; results: ReleaseT[] } };
type V = {
  search: string;
  collectionIds: number[];
  artistIds: number[];
  releaseTypes: ReleaseType[];
  sort: ReleaseSort;
  asc: boolean;
  page: number;
  perPage: number;
};

export const useSearchReleases = (
  viewOptions: ViewOptionsT,
  pagination: PaginationT,
  options?: QueryHookOptions<T, V>,
): QueryResult<T, V> => {
  const newOptions = React.useMemo(
    () => ({ ...options, variables: extractVariables(viewOptions, pagination) }),
    [options, viewOptions, pagination],
  );

  return useQuery<T, V>(QUERY, newOptions);
};

/**
 * Extract variables from viewOptions and pagination to form the query variables.
 */
const extractVariables = (
  { search, collectionIds, artistIds, releaseTypes, sort, asc }: ViewOptionsT,
  { curPage, perPage }: PaginationT,
): V => ({
  artistIds,
  asc,
  collectionIds,
  page: curPage,
  perPage,
  releaseTypes,
  search,
  sort,
});
