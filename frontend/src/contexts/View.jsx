import React from 'react';
import { usePersistentState } from 'hooks';

export const ViewContext = React.createContext({
  view: '',
  setView: () => {},
  expandTrackLists: false,
  setExpandTrackLists: () => {},
});

export const ViewContextProvider = ({ children }) => {
  const [view, setView] = usePersistentState('releases--view', 'Detailed');
  const [expandTrackLists, setExpandTrackLists] = usePersistentState(
    'releases--expandTrackLists',
    false
  );

  const value = { view, setView, expandTrackLists, setExpandTrackLists };

  return <ViewContext.Provider value={value}>{children}</ViewContext.Provider>;
};
