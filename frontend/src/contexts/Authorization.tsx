import * as React from 'react';
import { useRequestJson } from 'src/hooks';

type ACType = {
  loggedIn: boolean | null;
  setLoggedIn: (arg0: boolean | null) => void;
  csrf: string | null;
  setCsrf: (arg0: string | null) => void;
};

export const AuthorizationContext = React.createContext<ACType>({
  loggedIn: false,
  setLoggedIn: () => {},
  csrf: null,
  setCsrf: () => {},
});

export const AuthorizationProvider: React.FC<{ children: React.ReactNode }> = ({ children }) => {
  const [loggedIn, setLoggedIn] = React.useState<boolean | null>(null);
  const [csrf, setCsrf] = React.useState<string | null>(null);
  const requestJson = useRequestJson<{ csrfToken: string }>();

  const value = { loggedIn, setLoggedIn, csrf, setCsrf };

  React.useEffect(() => {
    (async (): Promise<void> => {
      try {
        const { csrfToken } = await requestJson('/session/create', { method: 'POST' });
        if (csrfToken) {
          setLoggedIn(true);
          setCsrf(csrfToken);
        } else {
          setLoggedIn(false);
        }
      } catch (e) {
        setLoggedIn(false);
        return;
      }
    })();
  }, []);

  return <AuthorizationContext.Provider value={value}>{children}</AuthorizationContext.Provider>;
};
