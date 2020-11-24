import * as React from 'react';

import { usePersistentState } from 'src/hooks';

type SCType = {
  isSidebarOpen: boolean;
  setSidebarOpen: (arg0: boolean | ((arg0: boolean) => boolean), arg1?: boolean) => void;
};

export const SidebarContext = React.createContext<SCType>({
  isSidebarOpen: true,
  setSidebarOpen: () => {},
});

export const SidebarProvider: React.FC<{ children: React.ReactNode }> = ({ children }) => {
  const [isSidebarOpen, setSidebarOpen] = usePersistentState<boolean>('sidebar--open', true);

  const value = { isSidebarOpen, setSidebarOpen };

  return <SidebarContext.Provider value={value}>{children}</SidebarContext.Provider>;
};
