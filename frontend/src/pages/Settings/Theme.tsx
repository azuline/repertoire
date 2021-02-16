import * as React from 'react';

import { Button } from '~/components';
import { ThemeContext } from '~/contexts';

export const ThemeSettings: React.FC = () => {
  const { theme, setTheme } = React.useContext(ThemeContext);

  const toggleTheme = (): void => setTheme((t) => (t === 'light' ? 'dark' : 'light'));

  return (
    <div className="flex items-center my-4">
      <div className="w-28">Theme:</div>
      <Button type="button" onClick={toggleTheme}>
        {theme}
      </Button>
    </div>
  );
};
