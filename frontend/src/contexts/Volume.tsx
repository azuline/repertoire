import * as React from 'react';

import { ISetPersistentValue, usePersistentState } from '~/hooks';

type IContext = {
  volume: number;
  setVolume: ISetPersistentValue<number>;
  isMuted: boolean;
  setIsMuted: ISetPersistentValue<boolean>;
};

export const VolumeContext = React.createContext<IContext>({
  isMuted: false,
  setIsMuted: () => {},
  setVolume: () => {},
  volume: 100,
});

type IProvider = React.FC<{ children: React.ReactNode }>;

export const VolumeProvider: IProvider = ({ children }) => {
  const [volume, setVolume] = usePersistentState<number>('volume--volume', 100);
  const [isMuted, setIsMuted] = usePersistentState<boolean>('volume--muted', false);

  const value = { isMuted, setIsMuted, setVolume, volume };

  return <VolumeContext.Provider value={value}>{children}</VolumeContext.Provider>;
};
