import React, { useCallback, useState } from 'react';

import { useHistory } from 'react-router-dom';
import { usePersistentState } from 'hooks';

export const SearchContext = React.createContext({
  query: '',
  setQuery: () => {},
  activeQuery: '',
  setActiveQuery: () => {},
  recentQueries: [],
});

export const SearchContextProvider = ({ children }) => {
  const history = useHistory();
  const [query, setQuery] = useState('');
  const [activeQuery, setActiveQueryRaw] = useState('');
  const [recentQueries, setRecentQueries] = usePersistentState('queries--recent', []);

  const setActiveQuery = useCallback(
    (newQuery) => {
      // Redirect to '/' if not already there.
      if (history.location.pathname !== '/') {
        history.push('/');
      }

      // Sync `query` with `activeQuery`.
      setQuery(newQuery);
      setActiveQueryRaw(newQuery);

      // Update recent queries: cap the list of recent queries at 30 entries and
      // remove previous duplicate queries.
      setRecentQueries((oldEntries) => {
        if (!newQuery) return oldEntries;

        const dedupEntries = oldEntries.filter((entry) => entry.query !== newQuery);
        const newEntry = { query: newQuery, time: Math.floor(Date.now() / 1000) };
        return [newEntry, ...dedupEntries].slice(0, 30);
      });
    },
    [history, setQuery, setActiveQueryRaw, setRecentQueries]
  );

  const value = { query, setQuery, activeQuery, setActiveQuery, recentQueries };

  return <SearchContext.Provider value={value}>{children}</SearchContext.Provider>;
};
