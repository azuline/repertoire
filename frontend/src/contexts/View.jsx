import React, { useEffect, useState } from 'react';

export const ViewContext = React.createContext({
  view: '',
  setView: () => {},
  expandTrackLists: false,
  setExpandTrackLists: () => {},
});

const localView = localStorage.getItem('releases--view') ?? 'Detailed';
const localExpandTrackLists =
  localStorage.getItem('releases--expandTrackLists') === 'true';

export const ViewContextProvider = ({ children }) => {
  const [view, setView] = useState(localView);
  const [expandTrackLists, setExpandTrackLists] = useState(localExpandTrackLists);

  useEffect(() => localStorage.setItem('releases--view', view), [view]);
  useEffect(
    () => localStorage.setItem('releases--expandTrackLists', expandTrackLists),
    [expandTrackLists]
  );

  const value = { view, setView, expandTrackLists, setExpandTrackLists };

  return <ViewContext.Provider value={value}>{children}</ViewContext.Provider>;
};
