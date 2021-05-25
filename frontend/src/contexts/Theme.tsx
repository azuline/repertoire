import * as React from 'react';

import { ISetPersistentValue, usePersistentState } from '~/hooks';

export type ITheme = 'dark' | 'light';

type IContext = {
  theme: ITheme;
  setTheme: ISetPersistentValue<ITheme>;
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
