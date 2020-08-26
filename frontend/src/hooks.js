import { useState } from 'react';

export const useSortContext = (asc, sortField) => {
  // Create the sort context value.
  const [ascState, setAsc] = useState(asc === 'true');
  const [sortFieldState, setSortField] = useState(parseInt(sortField) || 1);

  const sortValue = {
    asc: ascState,
    sortField: sortFieldState,
    updateSort: ({ asc, sortField }) => {
      if (asc !== undefined) setAsc(asc);
      if (sortField !== undefined) setSortField(sortField);
    },
  };

  return [ascState, sortFieldState, sortValue];
};

export const useReleaseViewContext = (view, expandTrackLists) => {
  const [viewState, setView] = useState(view ?? 'Detailed');
  const [expandTrackListsState, setExpandTrackLists] = useState(
    expandTrackLists === 'true'
  );

  const releaseViewValue = {
    expandTrackLists: expandTrackListsState,
    updateView: ({ view, expandTrackLists }) => {
      if (view !== undefined) setView(view);
      if (expandTrackLists !== undefined) setExpandTrackLists(expandTrackLists);
    },
    view: viewState,
  };

  return [viewState, expandTrackListsState, releaseViewValue];
};

export const useFilterContext = (filter, collectionType) => {
  // Create the filter context value.
  const [filterState, setFilter] = useState(filter ?? '');
  const [collectionTypeState, setCollectionType] = useState(collectionType ?? 'All');

  const filterValue = {
    filter: filterState,
    selection: collectionTypeState,
    updateFilter: ({ selection, filter }) => {
      if (filter !== undefined) setFilter(filter);
      if (selection !== undefined) setCollectionType(selection);
    },
  };

  return [filterState, collectionTypeState, filterValue];
};

export const useRecentQueriesContext = (recentQueries) => {
  const [recentQueriesState, setRecentQueries] = useState(recentQueries);

  // For the updater, remove duplicate entries in the old list.
  const recentQueriesValue = {
    recentQueries: recentQueriesState,
    updateRecentQueries: (query) => {
      const time = Math.floor(Date.now() / 1000);
      const filteredOldQueries = recentQueriesState.filter((oldQuery) => {
        return oldQuery.query !== query;
      });
      setRecentQueries([{ query, time }, ...filteredOldQueries].slice(0, 30));
    },
  };

  return [recentQueriesState, recentQueriesValue];
};
