import * as React from 'react';
import { Header, SectionHeader } from 'src/components';
import { ThemeContext, ThemeT } from 'src/contexts';

export const Settings: React.FC = () => {
  const { theme, setTheme } = React.useContext(ThemeContext);

  const toggleTheme = React.useCallback(
    () => setTheme((innerTheme: ThemeT) => (innerTheme === 'light' ? 'dark' : 'light')),
    [setTheme],
  );

  return (
    <>
      <Header searchbar={false} />
      <div className="px-8">
        <SectionHeader className="mt-4 mb-8">Settings</SectionHeader>
        <div>
          Toggle theme:
          <button type="button" onClick={toggleTheme}>
            {theme}
          </button>
        </div>
      </div>
    </>
  );
};
