import * as React from 'react';

import { usePersistentState } from 'src/hooks';

export type ThemeT = 'dark' | 'light';

type TCType = {
  theme: ThemeT;
  setTheme: (arg0: ThemeT | ((arg0: ThemeT) => ThemeT), arg1?: boolean) => void;
};

export const ThemeContext = React.createContext<TCType>({
  theme: 'dark',
  setTheme: () => {},
});

export const ThemeProvider: React.FC<{ children: React.ReactNode }> = ({ children }) => {
  const [theme, setTheme] = usePersistentState<ThemeT>('site--theme', 'dark');

  const value = { theme, setTheme };

  return <ThemeContext.Provider value={value}>{children}</ThemeContext.Provider>;
};
