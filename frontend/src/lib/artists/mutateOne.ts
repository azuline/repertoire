import * as React from 'react';
import { MutationResultPair, useQueryCache } from 'react-query';
import { useGQLMutation } from 'src/hooks';
import { ARTIST_FIELDS } from 'src/lib/fragments';
import { ArtistT, GraphQLError, RequestError } from 'src/types';

const QUERY = `
  mutation (
    $id: Int!
    $name: String
    $starred: Boolean
  ) {
    updateArtist (
      id: $id
      name: $name
      starred: $starred
    ) {
      ${ARTIST_FIELDS}
    }
  }
`;

type Result = { artist: ArtistT };
export type MutateOneArtistVariablesT = { id: number; name?: string; starred?: boolean };

/**
 * A wrapper around react-query to mutate a single artist.
 *
 * React-Query's  ``mutate`` function takes a variable of type ``MutateOneArtistVariablesT``.
 *
 * @returns The react-query mutation result.
 */
export const useMutateArtist = (): MutationResultPair<
  Result,
  RequestError<GraphQLError>,
  MutateOneArtistVariablesT,
  unknown
> => {
  const queryCache = useQueryCache();

  const onSuccess = React.useCallback(() => queryCache.invalidateQueries('artists'), [queryCache]);

  return useGQLMutation<Result, MutateOneArtistVariablesT>(QUERY, { onSuccess });
};
