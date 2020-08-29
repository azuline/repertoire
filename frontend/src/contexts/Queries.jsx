import React, { useEffect, useState } from 'react';

import Fuse from 'fuse.js';
import { fuseOptions } from 'common/fuse';
import { submitQuery } from 'requests';
import { fetchQueries } from 'requests';

export const QueriesContext = React.createContext({
  queries: [],
  setQueries: () => {},
  saveQuery: () => {},
  fuse: null,
  fetched: false,
});

export const QueriesContextProvider = ({ children }) => {
  const [queries, setQueries] = useState([]);
  const [fetched, setFetched] = useState(false);
  const fuse = new Fuse(queries, { ...fuseOptions, keys: ['name'] });

  useEffect(() => fuse.setCollection(queries), [fuse, queries]);

  useEffect(() => {
    (async () => {
      setQueries(await fetchQueries());
      setFetched(true);
    })();
  }, []);

  const saveQuery = (query, name) => {
    const submittedQuery = submitQuery(query, name);
    setQueries([submittedQuery, ...queries]);
  };

  const value = { queries, setQueries, saveQuery, fuse, fetched };

  return <QueriesContext.Provider value={value}>{children}</QueriesContext.Provider>;
};
