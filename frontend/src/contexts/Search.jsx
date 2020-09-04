import React, { useEffect, useState } from 'react';
import { useParseQuery, usePersistentState } from 'hooks';

import { useHistory } from 'react-router-dom';

export const SearchContext = React.createContext({
  query: '',
  setQuery: () => {},
  activeQuery: '',
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

  useEffect(
    (newQuery) => {
      // Redirect to '/' if not already there.
      if (history.location.pathname !== '/') {
        history.push('/');
      }

      // Parse query and update parsed values.
      const [newSearch, newCollections, newArtists] = parseQuery(query);
      setSearch(newSearch);
      setCollections(newCollections);
      setArtists(newArtists);

      // Update recent queries: cap the list of recent queries at 30 entries and
      // remove previous duplicate queries.
      setRecentQueries((oldEntries) => {
        if (!newQuery) return oldEntries;

        const dedupEntries = oldEntries.filter((entry) => entry.query !== query);
        const newEntry = { query, time: Date.now() };
        return [newEntry, ...dedupEntries].slice(0, 30);
      });
    },
    [
      history,
      query,
      parseQuery,
      setSearch,
      setCollections,
      setArtists,
      setRecentQueries,
    ]
  );

  const value = {
    query,
    search,
    collections,
    artists,
    setQuery,
    recentQueries,
  };

  return <SearchContext.Provider value={value}>{children}</SearchContext.Provider>;
};
