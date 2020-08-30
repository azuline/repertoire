import React, { useEffect, useState, useCallback, useContext } from 'react';

import { queryReleases } from 'requests';
import { useHistory } from 'react-router-dom';
import { usePersistentState } from 'hooks';
import { parseQuery } from 'common/queries';
import { SortContext } from './Sort';
import { ReleasesContext } from './Releases';
import { PaginationContext } from './Pagination';
export { ViewContext } from './View';

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

  const { asc, sortField } = useContext(SortContext);
  const { page, perPage } = useContext(PaginationContext);
  const { setReleases } = useContext(ReleasesContext);

  // Cap the list of recent queries at 30 entries and remove previous duplicate queries.
  const appendRecentQuery = useCallback(
    (query) => {
      const entry = { query, time: Math.floor(Date.now() / 1000) };
      const oldEntries = recentQueries.filter((oldEntry) => oldEntry.query !== query);
      setRecentQueries([entry, ...oldEntries].slice(0, 30));
    },
    [recentQueries, setRecentQueries]
  );

  // Function to query the backend for releases.
  const runQuery = useCallback(
    (query) => {
      history.push('/');
      setQuery(query);
      appendRecentQuery(query);

      (async () => {
        const [search, collections, artists] = parseQuery(query);
        const releases = await queryReleases(
          search,
          collections,
          artists,
          page,
          perPage,
          sortField,
          asc
        );
        setReleases(releases);
      })();
    },
    [history, setQuery, appendRecentQuery, setReleases, page, perPage, sortField, asc]
  );

  // Execute `runQuery` on changes to release view options.
  useEffect(() => runQuery(query), [page, perPage, sortField, asc]);

  const value = { query, setQuery, runQuery, recentQueries };

  return <SearchContext.Provider value={value}>{children}</SearchContext.Provider>;
};
