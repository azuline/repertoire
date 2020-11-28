import { MutationConfig, MutationResultPair, QueryResult } from 'react-query';
import { GraphQLError, RequestError } from 'src/types';

export type StateValue<T> = T | ((arg0: T) => T);
export type SetValue<T> = (arg0: StateValue<T>) => void;
export type SetPersistentValue<T> = (arg0: StateValue<T>, arg1?: boolean) => void;

export type GQLReqError = RequestError<GraphQLError>;
export type QueryReturn<T> = QueryResult<T, GQLReqError>;

export type MutationHook<T, V> = (
  config?: MutationConfig<T, GQLReqError, V, unknown>,
) => MutationResultPair<T, GQLReqError, V, unknown>;
