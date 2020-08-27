import React, { useContext } from 'react';

import { Button } from '@blueprintjs/core';
import { ThemeContext } from 'contexts';

export const ThemeButton = () => {
  const { dark, setDark } = useContext(ThemeContext);

  return (
    <Button
      className="bp3-minimal"
      icon="lightbulb"
      text={dark ? 'Light' : 'Dark'}
      onClick={() => setDark(!dark)}
    />
  );
};
