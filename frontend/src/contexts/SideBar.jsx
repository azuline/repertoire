import React, { useMemo } from 'react';
import { usePersistentState } from 'hooks';

export const SideBarContext = React.createContext({
  hideCollection: true,
  setHideCollection: () => {},
  hideArtist: true,
  setHideArtist: () => {},
});

export const SideBarContextProvider = ({ children }) => {
  const [hideCollection, setHideCollection] = usePersistentState(
    'sidebar--hide-collection',
    true
  );
  const [hideArtist, setHideArtist] = usePersistentState('sidebar--hide-artist', true);

  const numVisible = useMemo(() => {
    if (hideCollection && hideArtist) {
      return 0;
    } else if (!hideCollection && !hideArtist) {
      return 2;
    } else {
      return 1;
    }
  }, [hideCollection, hideArtist]);

  const value = {
    hideCollection,
    setHideCollection,
    hideArtist,
    setHideArtist,
    numVisible,
  };

  return <SideBarContext.Provider value={value}>{children}</SideBarContext.Provider>;
};
