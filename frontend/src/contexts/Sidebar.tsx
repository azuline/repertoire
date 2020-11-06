import * as React from 'react';

import { usePersistentState } from 'src/hooks';

type SCType = {
  openBar: boolean;
  setOpenBar: (arg0: boolean | ((arg0: boolean) => boolean), arg1?: boolean) => void;
};

export const SidebarContext = React.createContext<SCType>({
  openBar: true,
  setOpenBar: () => {},
});

export const SidebarProvider: React.FC<{ children: React.ReactNode }> = ({ children }) => {
  const [openBar, setOpenBar] = usePersistentState<boolean>('sidebar--open', true);

  const value = { openBar, setOpenBar };

  return <SidebarContext.Provider value={value}>{children}</SidebarContext.Provider>;
};
