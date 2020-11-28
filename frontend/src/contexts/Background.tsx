import * as React from 'react';
import { SetValue } from 'src/types';

type ContextT = {
  backgroundImageId: number | null;
  setBackgroundImageId: SetValue<number | null>;
};

export const BackgroundContext = React.createContext<ContextT>({
  backgroundImageId: null,
  setBackgroundImageId: () => {},
});

export const BackgroundProvider: React.FC<{ children: React.ReactNode }> = ({ children }) => {
  const [backgroundImageId, setBackgroundImageId] = React.useState<number | null>(null);

  const value = { backgroundImageId, setBackgroundImageId };

  return <BackgroundContext.Provider value={value}>{children}</BackgroundContext.Provider>;
};
