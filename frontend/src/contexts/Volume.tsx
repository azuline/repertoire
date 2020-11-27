import * as React from 'react';
import { usePersistentState } from 'src/hooks';
import { SetPersistentValue } from 'src/types';

type ContextT = {
  volume: number;
  setVolume: SetPersistentValue<number>;
  isMuted: boolean;
  setIsMuted: SetPersistentValue<boolean>;
};

export const VolumeContext = React.createContext<ContextT>({
  volume: 100,
  setVolume: () => {},
  isMuted: false,
  setIsMuted: () => {},
});

export const VolumeProvider: React.FC<{ children: React.ReactNode }> = ({ children }) => {
  const [volume, setVolume] = usePersistentState<number>('volume--volume', 100);
  const [isMuted, setIsMuted] = usePersistentState<boolean>('volume--muted', false);

  const value = { volume, setVolume, isMuted, setIsMuted };

  return <VolumeContext.Provider value={value}>{children}</VolumeContext.Provider>;
};
