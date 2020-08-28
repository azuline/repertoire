import React, { useState } from 'react';
import { usePersistentState } from 'hooks';

import { executeQuery } from 'lib/queries';
import { useHistory } from 'react-router-dom';

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
  const appendRecentQuery = (query) => {
    const entry = { query, time: Math.floor(Date.now() / 1000) };
    const oldEntries = recentQueries.filter((oldEntry) => oldEntry.query !== query);
    setRecentQueries([entry, ...oldEntries].slice(0, 30));
  };

  const runQuery = (query) => {
    history.push('/');
    setQuery(query);
    appendRecentQuery(query);

    const releases = executeQuery(query);
    return releases; // delete this later, should instead modify release list context.
  };

  const value = { query, setQuery, runQuery, recentQueries };

  return <SearchContext.Provider value={value}>{children}</SearchContext.Provider>;
};
