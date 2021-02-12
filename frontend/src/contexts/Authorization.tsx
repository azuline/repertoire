import * as React from 'react';
import { usePersistentState, useRequestJson } from '~/hooks';

type ContextT = {
  loggedIn: boolean;
  setLoggedIn: (arg0: boolean) => void;
  csrf: string | null;
  setCsrf: (arg0: string | null) => void;
};

export const AuthorizationContext = React.createContext<ContextT>({
  csrf: null,
  loggedIn: false,
  setCsrf: () => {},
  setLoggedIn: () => {},
});

export const AuthorizationProvider: React.FC<{ children: React.ReactNode }> = ({ children }) => {
  const [loggedIn, setLoggedIn] = usePersistentState<boolean>('auth--loggedIn', false);
  const [csrf, setCsrf] = usePersistentState<string | null>('auth--csrfToken', null);
  const requestJson = useRequestJson<{ csrfToken: string }>();

  const value = { csrf, loggedIn, setCsrf, setLoggedIn };

  React.useEffect(() => {
    (async (): Promise<void> => {
      try {
        const { csrfToken } = await requestJson('/session', { method: 'POST' });
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
  }, [requestJson, setCsrf, setLoggedIn]);

  return <AuthorizationContext.Provider value={value}>{children}</AuthorizationContext.Provider>;
};
