import React, { useContext, useState } from 'react';

import { RecentQueriesContext } from './RecentQueries';
import { executeQuery } from 'lib/queries';
import { useHistory } from 'react-router-dom';

export const SearchContext = React.createContext({
  query: '',
  setQuery: () => {},
  runQuery: () => {},
});

export const SearchContextProvider = ({ children }) => {
  const history = useHistory();
  const [query, setQuery] = useState('');
  const { appendRecentQuery } = useContext(RecentQueriesContext);

  const runQuery = (query) => {
    history.push('/');
    setQuery(query);
    appendRecentQuery(query);

    const releases = executeQuery(query);
    return releases; // delete this later, should instead modify release list context.
  };

  const value = { query, setQuery, runQuery };

  return <SearchContext.Provider value={value}>{children}</SearchContext.Provider>;
};
