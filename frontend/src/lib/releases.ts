import * as React from 'react';

import { GraphQLError, ReleaseSort, ReleaseT, ReleaseType, RequestError } from 'src/types';
import { PCType, RVOCType, useGQLQuery } from 'src/hooks';

import { QueryResult } from 'react-query';
import { RELEASE_FIELDS } from 'src/fragments';

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

type ResultType = { releases: { total: number; results: ReleaseT[] } };

type Variables = {
  search: string;
  collectionIds: number[];
  artistIds: number[];
  releaseTypes: ReleaseType[];
  sort: ReleaseSort;
  asc: boolean;
  page: number;
  perPage: number;
};

export const fetchReleases = (
  viewOptions: RVOCType,
  pagination: PCType,
): QueryResult<ResultType, RequestError<GraphQLError>> => {
  // prettier-ignore
  const variables = React.useMemo(
    () => extractVariables(viewOptions, pagination),
    [viewOptions, pagination]
  );

  return useGQLQuery<ResultType, Variables>('releases', QUERY, { variables });
};

const extractVariables = (
  { search, collectionIds, artistIds, releaseTypes, sort, asc }: RVOCType,
  { curPage, perPage }: PCType,
): Variables => ({
  search,
  collectionIds,
  artistIds,
  releaseTypes,
  sort,
  asc,
  perPage,
  page: curPage,
});
