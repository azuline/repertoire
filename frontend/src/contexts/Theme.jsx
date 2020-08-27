import React, { useEffect, useState } from 'react';

export const ThemeContext = React.createContext({
  dark: false,
  setDark: () => {},
});

const localDark = localStorage.getItem('theme-dark') === 'true';

export const ThemeContextProvider = ({ children }) => {
  const [dark, setDark] = useState(localDark);

  useEffect(() => {
    if (dark === true) {
      document.body.className = 'bp3-dark';
      localStorage.setItem('theme-dark', 'true');
    } else {
      document.body.className = 'bp3-body';
      localStorage.removeItem('theme-dark');
    }
  }, [dark]);

  const value = { dark, setDark };

  return <ThemeContext.Provider value={value}>{children}</ThemeContext.Provider>;
};
