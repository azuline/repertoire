import * as React from 'react';
import { usePersistentState } from 'src/hooks';

type ContextT = {
  csrfToken: string | null;
  setCsrfToken: (arg0: string | null, arg1?: boolean) => void;
};

export const CSRFContext = React.createContext<ContextT>({
  csrfToken: null,
  setCsrfToken: () => {},
});

export const CSRFProvider: React.FC<{ children: React.ReactNode }> = ({ children }) => {
  const [csrfToken, setCsrfToken] = usePersistentState<string | null>('auth--csrf', null);

  const value = { csrfToken, setCsrfToken };

  return <CSRFContext.Provider value={value}>{children}</CSRFContext.Provider>;
};
