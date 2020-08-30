import React, { useState, useEffect } from 'react';
import { usePersistentState } from 'hooks';
import { useHistory } from 'react-router-dom';

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
  const [activeQuery, setActiveQuery] = useState('');
  const [recentQueries, setRecentQueries] = usePersistentState('queries--recent', []);

  // On a new `activeQuery`, redirect to '/', sync the state of `query` to
  // `activeQuery`, and update the list of recent queries.
  useEffect(() => {
    history.push('/');
    setQuery(activeQuery);

    // Cap the list of recent queries at 30 entries and remove previous
    // duplicate queries.
    setRecentQueries((oldEntries) => {
      const dedupEntries = oldEntries.filter((entry) => entry.query !== activeQuery);
      const newEntry = { activeQuery, time: Math.floor(Date.now() / 1000) };
      return [newEntry, ...dedupEntries].slice(0, 30);
    });
  }, [history, setQuery, activeQuery, setRecentQueries]);

  const value = { query, setQuery, activeQuery, setActiveQuery, recentQueries };

  return <SearchContext.Provider value={value}>{children}</SearchContext.Provider>;
};
