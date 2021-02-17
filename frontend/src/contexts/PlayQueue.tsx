import * as React from 'react';

import { ITrack } from '~/graphql';

type IContext = {
  playQueue: ITrack[];
  setPlayQueue: (arg0: ITrack[]) => void;
  curIndex: number | null;
  setCurIndex: (arg0: number | null | ((arg0: number | null) => number | null)) => void;
};

export const PlayQueueContext = React.createContext<IContext>({
  curIndex: null,
  playQueue: [],
  setCurIndex: () => {},
  setPlayQueue: () => {},
});

type IProvider = React.FC<{ children: React.ReactNode }>;

export const PlayQueueProvider: IProvider = ({ children }) => {
  const [playQueue, setPlayQueue] = React.useState<ITrack[]>([]);
  const [curIndex, setCurIndex] = React.useState<number | null>(null);

  const value = { curIndex, playQueue, setCurIndex, setPlayQueue };

  return <PlayQueueContext.Provider value={value}>{children}</PlayQueueContext.Provider>;
};
