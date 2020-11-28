import * as React from 'react';
import { useQueryCache } from 'react-query';
import { useGQLMutation } from 'src/hooks';
import { FULL_RELEASE_FIELDS } from 'src/lib/fragments';
import { updateMutationConfig } from 'src/lib/util';
import { MutationHook, ReleaseT, ReleaseType } from 'src/types';

const QUERY = `
  mutation (
    $id: Int!
    $title: String
    $releaseType: ReleaseType
    $releaseYear: Int
    $releaseDate: String
  ) {
    updateRelease (
      id: $id
      title: $title
      releaseType: $releaseType
      releaseYear: $releaseYear
      releaseDate: $releaseDate
    ) {
      ${FULL_RELEASE_FIELDS}
    }
  }
`;

type ResultT = { release: ReleaseT };
export type MutateOneReleaseVariablesT = {
  id: number;
  title?: string;
  releaseType?: ReleaseType;
  releaseYear?: number;
  releaseDate?: string;
};

/**
 * A wrapper around react-query to mutate a single release.
 *
 * React-Query's  ``mutate`` function takes a variable of type ``MutateOneReleaseVariablesT``.
 *
 * @returns The react-query mutation result.
 */
export const useMutateRelease: MutationHook<ResultT, MutateOneReleaseVariablesT> = (
  config = {},
) => {
  const queryCache = useQueryCache();

  const onSuccess = React.useCallback(() => {
    queryCache.invalidateQueries('releases');
  }, [queryCache]);

  const newConfig = updateMutationConfig(config, { onSuccess });

  return useGQLMutation<ResultT, MutateOneReleaseVariablesT>(QUERY, newConfig);
};
