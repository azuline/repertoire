import React, { useEffect, useState } from 'react';

import Fuse from 'fuse.js';
import { fuseOptions } from 'common/fuse';
import { mockCollections } from 'mockData';

export const CollectionsContext = React.createContext({
  collections: [],
  fuse: null,
  setCollections: () => {},
});

export const CollectionsContextProvider = ({ children }) => {
  const [collections, setCollections] = useState(mockCollections);
  const fuse = new Fuse(collections, { ...fuseOptions, keys: ['name'] });

  useEffect(() => fuse.setCollection(collections), [fuse, collections]);

  const value = { collections, fuse, setCollections };

  return (
    <CollectionsContext.Provider value={value}>{children}</CollectionsContext.Provider>
  );
};
