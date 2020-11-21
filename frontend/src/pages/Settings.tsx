import * as React from 'react';
import { ThemeT, ThemeContext } from 'src/contexts';

export const Settings: React.FC = () => {
  const { theme, setTheme } = React.useContext(ThemeContext);

  const toggleTheme = React.useCallback(
    () => setTheme((theme: ThemeT) => (theme === 'light' ? 'dark' : 'light')),
    [setTheme],
  );

  return (
    <div>
      Toggle theme: <button onClick={toggleTheme}>{theme}</button>
    </div>
  );
};
