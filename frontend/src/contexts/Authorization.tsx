import * as React from 'react';

import { usePersistentState, useRequestJson } from '~/hooks';

type IContext = {
  loggedIn: boolean;
  setLoggedIn: (arg0: boolean) => void;
  csrf: string | null;
  setCsrf: (arg0: string | null) => void;
};

export const AuthorizationContext = React.createContext<IContext>({
  csrf: null,
  loggedIn: false,
  setCsrf: () => {},
  setLoggedIn: () => {},
});

type IProvider = React.FC<{ children: React.ReactNode }>;

export const AuthorizationProvider: IProvider = ({ children }) => {
  const [loggedIn, setLoggedIn] = usePersistentState<boolean>('auth--loggedIn', false);
  const [csrf, setCsrf] = usePersistentState<string | null>('auth--csrfToken', null);
  const requestJson = useRequestJson<{ csrfToken: string }>();

  React.useEffect(() => {
    (async (): Promise<void> => {
      try {
        const { csrfToken } = await requestJson('/api/session', { method: 'POST' });
        if (csrfToken) {
          setLoggedIn(true);
          setCsrf(csrfToken);
        } else {
          setLoggedIn(false);
        }
      } catch (e) {
        setLoggedIn(false);
      }
    })();
  }, []);

  const value = { csrf, loggedIn, setCsrf, setLoggedIn };

  return <AuthorizationContext.Provider value={value}>{children}</AuthorizationContext.Provider>;
};
