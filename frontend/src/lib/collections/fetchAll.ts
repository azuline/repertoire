import { CollectionType, CollectionT, GraphQLError, RequestError } from 'src/types';

import { COLLECTION_FIELDS } from 'src/lib/fragments';
import { QueryResult } from 'react-query';
import { useGQLQuery } from 'src/hooks';

const QUERY = `
  query ($types: [CollectionType]) {
		collections (types: $types) {
			results {
				${COLLECTION_FIELDS}
			}
		}
	}
`;

type Result = { collections: { results: CollectionT[] } };
type Variables = { types: CollectionType[] };
type Return = QueryResult<Result, RequestError<GraphQLError>>;

export const fetchCollections = (types: CollectionType[] = []): Return => {
  return useGQLQuery<Result, Variables>('collections', QUERY, { types });
};
