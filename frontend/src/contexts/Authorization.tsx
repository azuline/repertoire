import * as React from 'react';
import { usePersistentState } from 'src/hooks';
import { User } from 'src/types';
import { LocalKeys } from 'src/constants';

type ACType = {
  token: string | null;
  setToken: (arg0: string | null, arg1?: boolean) => void;
  user: User | null;
  setUser: (arg0: User | null, arg1?: boolean) => void;
};

export const AuthorizationContext = React.createContext<ACType>({
  token: null,
  setToken: () => {},
  user: null,
  setUser: () => {},
});

export const AuthorizationProvider: React.FC<{ children: React.ReactNode }> = ({
  children,
}) => {
  const [token, setToken] = usePersistentState<string>(LocalKeys.AuthToken, null);
  const [user, setUser] = usePersistentState<User>(LocalKeys.AuthUser, null);

  const value = { token, setToken, user, setUser };

  return (
    <AuthorizationContext.Provider value={value}>
      {children}
    </AuthorizationContext.Provider>
  );
};
