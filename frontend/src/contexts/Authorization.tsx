import * as React from 'react';

import { usePersistentState } from 'src/hooks';

type ACType = {
  token: string | null;
  setToken: (arg0: string | null, arg1?: boolean) => void;
};

export const AuthorizationContext = React.createContext<ACType>({
  token: null,
  setToken: () => {},
});

export const AuthorizationProvider: React.FC<{ children: React.ReactNode }> = ({ children }) => {
  const [token, setToken] = usePersistentState<string>('auth--token', null);

  const value = { token, setToken };

  return <AuthorizationContext.Provider value={value}>{children}</AuthorizationContext.Provider>;
};
