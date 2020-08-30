import React, { useContext, useEffect, useState } from 'react';

import { AuthenticationContext } from './Authentication';
import Fuse from 'fuse.js';
import { fuseOptions } from 'common/fuse';
import { useRequest } from 'hooks';

export const CollectionsContext = React.createContext({
  collections: [],
  setCollections: () => {},
  fuse: null,
});

export const CollectionsContextProvider = ({ children }) => {
  const request = useRequest();
  const [collections, setCollections] = useState([]);
  const { token } = useContext(AuthenticationContext);

  const fuse = new Fuse(collections, { ...fuseOptions, keys: ['name'] });

  useEffect(() => fuse.setCollection(collections), [fuse, collections]);

  useEffect(() => {
    if (!token) return;

    (async () => {
      const response = await request('/api/collections');
      setCollections(await response.json());
    })();
  }, [token, request, setCollections]);

  const value = { collections, setCollections, fuse };

  return (
    <CollectionsContext.Provider value={value}>{children}</CollectionsContext.Provider>
  );
};
