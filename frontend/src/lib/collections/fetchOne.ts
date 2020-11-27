import { QueryResult } from 'react-query';
import { useGQLQuery } from 'src/hooks';
import { COLLECTION_FIELDS } from 'src/lib/fragments';
import { CollectionT, GraphQLError, RequestError } from 'src/types';

const QUERY = `
  query ($id: Int!) {
    collection (id: $id) {
      ${COLLECTION_FIELDS}
    }
  }
`;

type ResultT = { collection: CollectionT };
type VariablesT = { id: number };

/**
 * A wrapper around react-query to fetch a single collection.
 *
 * @param id - The ID of the collection to fetch.
 * @returns The react-query result.
 */
export const fetchCollection = (id: number): QueryResult<ResultT, RequestError<GraphQLError>> =>
  useGQLQuery<ResultT, VariablesT>('collection', QUERY, { id });
