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

type Result = { collection: CollectionT };
type Variables = { id: number };
type Return = QueryResult<Result, RequestError<GraphQLError>>;

export const fetchCollection = (id: number): Return => {
  return useGQLQuery<Result, Variables>('collection', QUERY, { id });
};
