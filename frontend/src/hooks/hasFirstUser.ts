import * as React from 'react';

import { useRequestJson } from './request';

type IResponse = {
  hasFirstUser: boolean;
};

type IReturn = {
  hasFirstUser: boolean;
  loading: boolean;
};

export const useHasFirstUser = (): IReturn => {
  const [hasFirstUser, setHasFirstUser] = React.useState<boolean>(false);
  const [loading, setLoading] = React.useState<boolean>(true);
  const requestJson = useRequestJson<IResponse>();

  React.useEffect(() => {
    (async (): Promise<void> => {
      const res = await requestJson('/api/register/has-first-user');
      setHasFirstUser(res.hasFirstUser);
      setLoading(false);
    })();
  }, []);

  return { hasFirstUser, loading };
};
