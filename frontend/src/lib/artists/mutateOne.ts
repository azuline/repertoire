import * as React from 'react';

import { ArtistT, GraphQLError, RequestError } from 'src/types';

import { ARTIST_FIELDS } from 'src/lib/fragments';
import { MutationResultPair, useQueryCache } from 'react-query';
import { useGQLMutation } from 'src/hooks';

const MUTATE_ARTIST_QUERY = `
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
type Variables = { id: number; name?: string; starred?: boolean };
type Return = MutationResultPair<Result, RequestError<GraphQLError>, Variables, unknown>;

export const useMutateArtist = (): Return => {
  const queryCache = useQueryCache();

  const onSuccess = React.useCallback(() => queryCache.invalidateQueries('artists'), [queryCache]);

  return useGQLMutation<Result, Variables>(MUTATE_ARTIST_QUERY, { onSuccess });
};
