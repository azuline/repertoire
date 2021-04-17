import * as React from 'react';

import { useRequestJson } from '~/hooks';

type IContext = {
  loggedIn: boolean;
  loading: boolean;
  setLoggedIn: (arg0: boolean) => void;
  csrf: string | null;
  setCsrf: (arg0: string | null) => void;
};

export const AuthorizationContext = React.createContext<IContext>({
  csrf: null,
  loading: false,
  loggedIn: false,
  setCsrf: () => {},
  setLoggedIn: () => {},
});

type IProvider = React.FC<{ children: React.ReactNode }>;

export const AuthorizationProvider: IProvider = ({ children }) => {
  const [loggedIn, setLoggedIn] = React.useState<boolean>(false);
  const [csrf, setCsrf] = React.useState<string | null>(null);
  const [loading, setLoading] = React.useState<boolean>(true);
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

      setLoading(false);
    })();
  }, []);

  const value = { csrf, loading, loggedIn, setCsrf, setLoggedIn };

  return (
    <AuthorizationContext.Provider value={value}>
      {children}
    </AuthorizationContext.Provider>
  );
};
