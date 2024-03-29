import * as React from 'react';

type IContext = {
  backgroundImageId: number | null;
  setBackgroundImageId: React.Dispatch<React.SetStateAction<number | null>>;
};

export const BackgroundContext = React.createContext<IContext>({
  backgroundImageId: null,
  setBackgroundImageId: () => {},
});

type IProvider = React.FC<{ children: React.ReactNode }>;

export const BackgroundProvider: IProvider = ({ children }) => {
  const [backgroundImageId, setBackgroundImageId] = React.useState<number | null>(null);

  const value = { backgroundImageId, setBackgroundImageId };

  return (
    <BackgroundContext.Provider value={value}>{children}</BackgroundContext.Provider>
  );
};
