import * as React from 'react';

import { useRequestJson } from './request';

type IResponse = {
  hasFirstUser: boolean;
};

export const useHasFirstUser = (): boolean => {
  const [has, setHas] = React.useState<boolean>(false);
  const requestJson = useRequestJson<IResponse>();

  React.useEffect(() => {
    (async (): Promise<void> => {
      const res = await requestJson('/api/register/has-first-user');
      setHas(res.hasFirstUser);
    })();
  }, []);

  return has;
};
