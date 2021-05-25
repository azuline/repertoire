import * as React from 'react';

import { useRequestJson } from './request';

type IResponse = {
  hasFirstUser: boolean;
};

type IReturn = {
  hasFirstUser: boolean;
  loading: boolean;
  error: boolean;
  refetch: () => Promise<void>;
};

export const useHasFirstUser = (): IReturn => {
  const [hasFirstUser, setHasFirstUser] = React.useState<boolean>(false);
  const [loading, setLoading] = React.useState<boolean>(true);
  const [error, setError] = React.useState<boolean>(false);
  const requestJson = useRequestJson<IResponse>();

  const fetchHasFirstUser = React.useCallback(async (): Promise<void> => {
    try {
      const res = await requestJson('/api/register/has-first-user');
      setHasFirstUser(res.hasFirstUser);
      setLoading(false);
    } catch {
      setLoading(false);
      setError(true);
    }
  }, [requestJson]);

  React.useEffect(() => {
    fetchHasFirstUser();
  }, [fetchHasFirstUser]);

  return { error, hasFirstUser, loading, refetch: fetchHasFirstUser };
};
