import * as React from 'react';
import { RequestError, GraphQLError, ReleaseT, ReleaseType, ReleaseSort } from 'src/types';
import { PCType, RVOCType } from 'src/contexts';
import { QueryResult } from 'react-query';
import { RELEASE_FIELDS } from 'src/fragments';
import { useGQLQuery } from 'src/hooks';

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
			results {
				${RELEASE_FIELDS}
				artists {
				  id
					name
				}
			}
		}
	}
`;

type ResultType = { releases: { results: ReleaseT[] } };

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
    [viewOptions, pagination,]
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
