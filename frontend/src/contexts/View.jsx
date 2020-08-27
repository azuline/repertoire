import React, { useEffect, useState } from 'react';

export const ViewContext = React.createContext({
  expandTrackLists: false,
  setExpandTrackLists: () => {},
  setView: () => {},
  view: '',
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

  const value = { expandTrackLists, setExpandTrackLists, setView, view };

  return <ViewContext.Provider value={value}>{children}</ViewContext.Provider>;
};
