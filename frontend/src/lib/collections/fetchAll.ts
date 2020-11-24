import { CollectionType, CollectionT, GraphQLError, RequestError } from 'src/types';

import { COLLECTION_FIELDS } from 'src/lib/fragments';
import { QueryResult } from 'react-query';
import { useGQLQuery } from 'src/hooks';

const QUERY = `
  query ($type: CollectionType) {
		collections (type: $type) {
			results {
				${COLLECTION_FIELDS}
			}
		}
	}
`;

type Result = { collections: { results: CollectionT[] } };
type Variables = { type?: CollectionType };
type Return = QueryResult<Result, RequestError<GraphQLError>>;

export const fetchCollections = (type?: CollectionType): Return => {
  return useGQLQuery<Result, Variables>('collections', QUERY, { type });
};
