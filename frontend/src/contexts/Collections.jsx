import React, { useContext, useEffect, useState } from 'react';

import Fuse from 'fuse.js';
import { AuthenticationContext } from './Authentication';
import { fetchCollections } from 'requests';
import { fuseOptions } from 'common/fuse';

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

  const { token } = useContext(AuthenticationContext);

  useEffect(() => fuse.setCollection(collections), [fuse, collections]);

  useEffect(() => {
    (async () => {
      if (token) {
        setCollections(await fetchCollections(token));
        setFetched(true);
      }
    })();
  }, [token]);

  const value = { collections, setCollections, fuse, fetched };

  return (
    <CollectionsContext.Provider value={value}>{children}</CollectionsContext.Provider>
  );
};
