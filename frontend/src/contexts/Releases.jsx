import React, { useState } from 'react';

export const ReleasesContext = React.createContext({
  releases: [],
  setReleases: () => {},
});

export const ReleasesContextProvider = ({ children }) => {
  const [releases, setReleases] = useState([]);

  const value = { releases, setReleases };

  return <ReleasesContext.Provider value={value}>{children}</ReleasesContext.Provider>;
};
