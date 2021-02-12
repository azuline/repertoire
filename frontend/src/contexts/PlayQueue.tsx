import * as React from 'react';

import { TrackT } from '~/types';

type ContextT = {
  playQueue: TrackT[];
  setPlayQueue: (arg0: TrackT[]) => void;
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
  const [playQueue, setPlayQueue] = React.useState<TrackT[]>([]);
  const [curIndex, setCurIndex] = React.useState<number | null>(null);

  const value = { curIndex, playQueue, setCurIndex, setPlayQueue };

  return <PlayQueueContext.Provider value={value}>{children}</PlayQueueContext.Provider>;
};
