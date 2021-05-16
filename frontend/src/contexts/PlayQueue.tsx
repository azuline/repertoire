import * as React from 'react';

import { ITrackFieldsFragment } from '~/graphql';

type IContext = {
  playQueue: ITrackFieldsFragment[];
  setPlayQueue: React.Dispatch<React.SetStateAction<ITrackFieldsFragment[]>>;
  curIndex: number | null;
  setCurIndex: React.Dispatch<React.SetStateAction<number | null>>;
};

export const PlayQueueContext = React.createContext<IContext>({
  curIndex: null,
  playQueue: [],
  setCurIndex: () => {},
  setPlayQueue: () => {},
});

type IProvider = React.FC<{ children: React.ReactNode }>;

export const PlayQueueProvider: IProvider = ({ children }) => {
  const [playQueue, setPlayQueue] = React.useState<ITrackFieldsFragment[]>([]);
  const [curIndex, setCurIndex] = React.useState<number | null>(null);

  const value = { curIndex, playQueue, setCurIndex, setPlayQueue };

  return (
    <PlayQueueContext.Provider value={value}>{children}</PlayQueueContext.Provider>
  );
};
