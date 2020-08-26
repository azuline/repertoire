import './index.scss';

import React, { useEffect } from 'react';

import { Input } from './Input';
import { RecentQueriesContext } from 'contexts';
import { useRecentQueriesContext } from 'hooks';

const initialRecentQueries = JSON.parse(
  localStorage.getItem('queries--recent') ?? '[]'
);

export const SearchBar = () => {
  const [recentQueries, recentQueriesValue] = useRecentQueriesContext(
    initialRecentQueries
  );

  useEffect(() => {
    localStorage.setItem('queries--recent', JSON.stringify(recentQueries));
  }, [recentQueries]);

  return (
    <div className="SearchBar">
      <RecentQueriesContext.Provider value={recentQueriesValue}>
        <Input />
      </RecentQueriesContext.Provider>
    </div>
  );
};
