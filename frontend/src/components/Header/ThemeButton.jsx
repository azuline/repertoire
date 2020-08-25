import React, { useEffect, useState } from 'react';

import { Button } from '@blueprintjs/core';

export const ThemeButton = () => {
  const localDark = localStorage.getItem('theme-dark');
  const [dark, setDark] = useState(localDark === 'true');

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
      onClick={() => setDark(!dark)}
    />
  );
};
