import React, { useEffect, useContext } from 'react';

import { Button } from '@blueprintjs/core';
import { ThemeContext } from 'contexts';

export const ThemeButton = () => {
  const { dark, updateDark } = useContext(ThemeContext);

  useEffect(() => {
    if (dark === true) {
      document.body.className = 'bp3-dark';
      localStorage.setItem('theme-dark', 'true');
    } else {
      document.body.className = 'bp3-body';
      localStorage.removeItem('theme-dark');
    }
  }, [dark]);

  return (
    <Button
      className="bp3-minimal"
      icon="lightbulb"
      text={dark ? 'Light' : 'Dark'}
      onClick={() => updateDark(!dark)}
    />
  );
};
