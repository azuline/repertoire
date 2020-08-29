import React, { useEffect, useState } from 'react';

import Fuse from 'fuse.js';
import { fuseOptions } from 'common/fuse';
import { fetchCollections } from 'requests';

export const CollectionsContext = React.createContext({
  collections: [],
  setCollections: () => {},
  fuse: null,
  fetched: false,
});

export const CollectionsContextProvider = ({ children }) => {
  const [collections, setCollections] = useState([]);
  const [fetched, setFetched] = useState(false);
  const fuse = new Fuse(collections, { ...fuseOptions, keys: ['name'] });

  useEffect(() => fuse.setCollection(collections), [fuse, collections]);

  useEffect(() => {
    (async () => {
      setCollections(await fetchCollections());
      setFetched(true);
    })();
  }, []);

  const value = { collections, setCollections, fuse, fetched };

  return (
    <CollectionsContext.Provider value={value}>{children}</CollectionsContext.Provider>
  );
};
