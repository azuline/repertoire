import React, { useEffect } from 'react';
import { usePersistentState } from 'hooks';

export const ThemeContext = React.createContext({
  dark: false,
  setDark: () => {},
});

export const ThemeContextProvider = ({ children }) => {
  const [dark, setDark] = usePersistentState('theme-dark', true);

  useEffect(() => {
    document.body.className = dark ? 'bp3-dark' : 'bp3-body';
  }, [dark]);

  const value = { dark, setDark };

  return <ThemeContext.Provider value={value}>{children}</ThemeContext.Provider>;
};
