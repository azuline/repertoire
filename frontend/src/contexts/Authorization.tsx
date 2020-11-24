import * as React from 'react';

type ACType = {
  loggedIn: boolean;
  setLoggedIn: (arg0: boolean) => void;
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
  const [loggedIn, setLoggedIn] = React.useState<boolean>(false);
  const [csrf, setCsrf] = React.useState<string | null>(null);

  const value = { loggedIn, setLoggedIn, csrf, setCsrf };

  return <AuthorizationContext.Provider value={value}>{children}</AuthorizationContext.Provider>;
};
