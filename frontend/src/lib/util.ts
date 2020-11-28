import * as React from 'react';
import { MutationConfig, useQueryCache } from 'react-query';
import { GraphQLError, RequestError } from 'src/types';

type MutCfg<T, V> = MutationConfig<T, RequestError<GraphQLError>, V, unknown>;

export const updateMutationConfig = <T, V>(
  config?: MutCfg<T, V>,
  newConfig?: MutCfg<T, V>,
): MutCfg<T, V> => {
  const queryCache = useQueryCache();

  const newOnSuccess = React.useCallback(
    (data, variables) => {
      if (config?.onSuccess) config.onSuccess(data, variables);
      if (newConfig?.onSuccess) newConfig.onSuccess(data, variables);
    },
    [queryCache, config],
  );

  return React.useMemo(() => ({ ...config, onSuccess: newOnSuccess }), [config, newOnSuccess]);
};
