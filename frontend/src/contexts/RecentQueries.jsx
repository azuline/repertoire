import React, { useEffect, useState } from 'react';

export const RecentQueriesContext = React.createContext({
  recentQueries: [],
  appendRecentQuery: () => {},
});

const localRecentQueries = JSON.parse(localStorage.getItem('queries--recent') ?? '[]');

export const RecentQueriesContextProvider = ({ children }) => {
  const [recentQueries, setRecentQueries] = useState(localRecentQueries);

  useEffect(() => {
    localStorage.setItem('queries--recent', JSON.stringify(recentQueries));
  }, [recentQueries]);

  // Cap the list of recent queries at 30 entries and remove previous duplicate queries.
  const appendRecentQuery = (query) => {
    const entry = { query, time: Math.floor(Date.now() / 1000) };
    const oldEntries = recentQueries.filter((oldEntry) => oldEntry.query !== query);
    setRecentQueries([entry, ...oldEntries].slice(0, 30));
  };

  const value = { appendRecentQuery, recentQueries };

  return (
    <RecentQueriesContext.Provider value={value}>
      {children}
    </RecentQueriesContext.Provider>
  );
};
