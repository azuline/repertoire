import React, { useCallback, useContext, useEffect, useState } from 'react';

import { AuthenticationContext } from './Authentication';
import Fuse from 'fuse.js';
import { fuseOptions } from 'common/fuse';
import { useRequest } from 'hooks';

export const QueriesContext = React.createContext({
  queries: [],
  setQueries: () => {},
  saveQuery: () => {},
  fuse: null,
});

export const QueriesContextProvider = ({ children }) => {
  const request = useRequest();
  const [queries, setQueries] = useState([]);
  const { token } = useContext(AuthenticationContext);

  const fuse = new Fuse(queries, { ...fuseOptions, keys: ['name'] });

  useEffect(() => fuse.setCollection(queries), [fuse, queries]);

  useEffect(() => {
    if (!token) return;

    (async () => {
      const response = await request('/api/queries');
      setQueries(await response.json());
    })();
  }, [token, request, setQueries]);

  const saveQuery = useCallback(
    (query, name) => {
      (async () => {
        const submittedQuery = await request('/api/queries', {
          method: 'POST',
          body: JSON.stringify({ query, name }),
        });
        setQueries((queries) => [submittedQuery, ...queries]);
      })();
    },
    [request, setQueries]
  );

  const value = { queries, setQueries, saveQuery, fuse };

  return <QueriesContext.Provider value={value}>{children}</QueriesContext.Provider>;
};
