import * as React from 'react';
import { usePersistentState } from 'src/hooks';

export type ThemeT = 'dark' | 'light';

type ContextT = {
  theme: ThemeT;
  setTheme: (arg0: ThemeT | ((arg0: ThemeT) => ThemeT), arg1?: boolean) => void;
};

export const ThemeContext = React.createContext<ContextT>({
  setTheme: () => {},
  theme: 'dark',
});

export const ThemeProvider: React.FC<{ children: React.ReactNode }> = ({ children }) => {
  const [theme, setTheme] = usePersistentState<ThemeT>('site--theme', 'dark');

  const value = { setTheme, theme };

  return <ThemeContext.Provider value={value}>{children}</ThemeContext.Provider>;
};
