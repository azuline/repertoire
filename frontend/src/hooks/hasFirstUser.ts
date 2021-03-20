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
      const { hasFirstUser: x } = await requestJson('/api/has_first_user');
      setHas(x);
    })();
  }, []);

  return has;
};
