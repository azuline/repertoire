import React, { useCallback, useState } from 'react';

import { useHistory } from 'react-router-dom';
import { useParseQuery, usePersistentState } from 'hooks';

export const SearchContext = React.createContext({
  query: '',
  setQuery: () => {},
  activeQuery: '',
  setActiveQuery: () => {},
  recentQueries: [],
});

export const SearchContextProvider = ({ children }) => {
  const history = useHistory();
  const parseQuery = useParseQuery();
  const [query, setQuery] = useState('');
  const [search, setSearch] = useState('');
  const [collections, setCollections] = useState([]);
  const [artists, setArtists] = useState([]);
  const [recentQueries, setRecentQueries] = usePersistentState('queries--recent', []);

  const setActiveQuery = useCallback(
    (newQuery) => {
      // Redirect to '/' if not already there.
      if (history.location.pathname !== '/') {
        history.push('/');
      }

      // Sync `query` with `activeQuery`.
      setQuery(newQuery);

      // Parse query and update parsed values.
      const [newSearch, newCollections, newArtists] = parseQuery(newQuery);
      setSearch(newSearch);
      setCollections(newCollections);
      setArtists(newArtists);

      // Update recent queries: cap the list of recent queries at 30 entries and
      // remove previous duplicate queries.
      setRecentQueries((oldEntries) => {
        if (!newQuery) return oldEntries;

        const dedupEntries = oldEntries.filter((entry) => entry.query !== newQuery);
        const newEntry = { query: newQuery, time: Math.floor(Date.now() / 1000) };
        return [newEntry, ...dedupEntries].slice(0, 30);
      });
    },
    [
      history,
      setQuery,
      parseQuery,
      setSearch,
      setCollections,
      setArtists,
      setRecentQueries,
    ]
  );

  const value = {
    query,
    setQuery,
    search,
    collections,
    artists,
    setActiveQuery,
    recentQueries,
  };

  return <SearchContext.Provider value={value}>{children}</SearchContext.Provider>;
};
