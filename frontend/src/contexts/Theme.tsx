import React from 'react';

import { usePersistentState } from '~/hooks';

export type ITheme = 'dark' | 'light';

type IContext = {
  theme: ITheme;
  setTheme: (arg0: ITheme | ((arg0: ITheme) => ITheme), arg1?: boolean) => void;
};

export const ThemeContext = React.createContext<IContext>({
  setTheme: () => {},
  theme: 'dark',
});

type IProvider = React.FC<{ children: React.ReactNode }>;

export const ThemeProvider: IProvider = ({ children }) => {
  const [theme, setTheme] = usePersistentState<ITheme>('site--theme', 'dark');

  const value = { setTheme, theme };

  return <ThemeContext.Provider value={value}>{children}</ThemeContext.Provider>;
};
