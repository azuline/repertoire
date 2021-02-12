import * as React from 'react';

import { ITrack } from '~/graphql';

type ContextT = {
  playQueue: ITrack[];
  setPlayQueue: (arg0: ITrack[]) => void;
  curIndex: number | null;
  setCurIndex: (arg0: number | null | ((arg0: number | null) => number | null)) => void;
};

export const PlayQueueContext = React.createContext<ContextT>({
  curIndex: null,
  playQueue: [],
  setCurIndex: () => {},
  setPlayQueue: () => {},
});

export const PlayQueueProvider: React.FC<{ children: React.ReactNode }> = ({ children }) => {
  const [playQueue, setPlayQueue] = React.useState<ITrack[]>([]);
  const [curIndex, setCurIndex] = React.useState<number | null>(null);

  const value = { curIndex, playQueue, setCurIndex, setPlayQueue };

  return <PlayQueueContext.Provider value={value}>{children}</PlayQueueContext.Provider>;
};
