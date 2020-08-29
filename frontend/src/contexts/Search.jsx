import React, { useState, useCallback } from 'react';

import { queryReleases } from 'requests';
import { useHistory } from 'react-router-dom';
import { usePersistentState } from 'hooks';

export const SearchContext = React.createContext({
  query: '',
  setQuery: () => {},
  runQuery: () => {},
  recentQueries: [],
});

export const SearchContextProvider = ({ children }) => {
  const history = useHistory();
  const [query, setQuery] = useState('');
  const [recentQueries, setRecentQueries] = usePersistentState('queries--recent', []);

  // Cap the list of recent queries at 30 entries and remove previous duplicate queries.
  const appendRecentQuery = useCallback(
    (query) => {
      const entry = { query, time: Math.floor(Date.now() / 1000) };
      const oldEntries = recentQueries.filter((oldEntry) => oldEntry.query !== query);
      setRecentQueries([entry, ...oldEntries].slice(0, 30));
    },
    [recentQueries, setRecentQueries]
  );

  const runQuery = useCallback(
    (query) => {
      history.push('/');
      setQuery(query);
      appendRecentQuery(query);

      const releases = queryReleases(query);
      return releases; // delete this later, should instead modify release list context.
    },
    [history, setQuery, appendRecentQuery]
  );

  const value = { query, setQuery, runQuery, recentQueries };

  return <SearchContext.Provider value={value}>{children}</SearchContext.Provider>;
};
