import { QueryResult } from 'react-query';
import { useGQLQuery } from 'src/hooks';
import { COLLECTION_FIELDS } from 'src/lib/fragments';
import { CollectionT, CollectionType, GraphQLError, RequestError } from 'src/types';

const QUERY = `
  query ($types: [CollectionType]) {
    collections (types: $types) {
      results {
        ${COLLECTION_FIELDS}
      }
    }
  }
`;

type ResultT = { collections: { results: CollectionT[] } };
type VariablesT = { types: CollectionType[] };

/**
 * A wrapper around react-query to fetch all collections (of one or more types).
 *
 * @param types - The types of collections to fetch. Leave empty to fetch all.
 * @returns The react-query result.
 */
export const fetchCollections = (
  types: CollectionType[] = [],
): QueryResult<ResultT, RequestError<GraphQLError>> =>
  useGQLQuery<ResultT, VariablesT>('collections', QUERY, { types });
