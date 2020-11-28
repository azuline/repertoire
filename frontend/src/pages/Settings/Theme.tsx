import * as React from 'react';
import { ThemeContext } from 'src/contexts';

export const ThemeSettings: React.FC = () => {
  const { theme, setTheme } = React.useContext(ThemeContext);

  // prettier-ignore
  const toggleTheme = React.useCallback(
    () => setTheme((t) => (t === 'light' ? 'dark' : 'light')),
    [setTheme],
  );

  return (
    <div className="flex items-center my-4">
      <div className="w-32">Toggle theme:</div>
      <button type="button" onClick={toggleTheme}>
        {theme}
      </button>
    </div>
  );
};
