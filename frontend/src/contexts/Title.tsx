import * as React from 'react';

export type Title = { label: string; url: string };

type TCType = {
  titles: Title[];
  setTitles: (arg0: Title[]) => void;
};

export const TitleContext = React.createContext<TCType>({
  titles: [],
  setTitles: () => {},
});

export const TitleProvider: React.FC<{ children: React.ReactNode }> = ({ children }) => {
  const [titles, setTitles] = React.useState<Title[]>([]);

  const value = { titles, setTitles };

  return <TitleContext.Provider value={value}>{children}</TitleContext.Provider>;
};
