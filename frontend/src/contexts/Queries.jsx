import React, { useEffect, useState } from 'react';

import Fuse from 'fuse.js';
import { fuseOptions } from 'common/fuse';
import { mockQueries } from 'mockData';

export const QueriesContext = React.createContext({
  queries: [],
  setQueries: () => {},
  fuse: null,
});

export const QueriesContextProvider = ({ children }) => {
  const [queries, setQueries] = useState(mockQueries);
  const fuse = new Fuse(queries, { ...fuseOptions, keys: ['name'] });

  useEffect(() => fuse.setCollection(queries), [fuse, queries]);

  const value = { queries, setQueries, fuse };

  return <QueriesContext.Provider value={value}>{children}</QueriesContext.Provider>;
};
