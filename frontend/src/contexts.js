import React from 'react';

export const SearchContext = React.createContext({
  query: '',
  updateQuery: () => {},
});

export const RecentQueriesContext = React.createContext({
  recentQueries: [],
  updateRecentQueries: () => {},
});

export const SortContext = React.createContext({
  asc: true,
  sortField: 1,
  updateSort: () => {},
});

export const ViewContext = React.createContext({
  expandTrackLists: false,
  updateView: () => {},
  view: '',
});

export const FilterContext = React.createContext({
  filter: '',
  selection: '',
  updateFilter: () => {},
});
