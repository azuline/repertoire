import * as React from 'react';
import { useQueryCache } from 'react-query';
import { useGQLMutation } from 'src/hooks';
import { ARTIST_FIELDS } from 'src/lib/fragments';
import { updateMutationConfig } from 'src/lib/util';
import { ArtistT, GraphQLError, MutationHook, RequestError } from 'src/types';

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
export const useMutateArtist: MutationHook<Result, MutateOneArtistVariablesT> = (config = {}) => {
  const queryCache = useQueryCache();

  const onSuccess = React.useCallback(() => {
    queryCache.invalidateQueries('artists');
  }, [queryCache]);

  const newConfig = updateMutationConfig(config, { onSuccess });

  return useGQLMutation<Result, MutateOneArtistVariablesT>(QUERY, newConfig);
};
