import React, { useEffect, useState } from 'react';

export const SortContext = React.createContext({
  asc: true,
  setAsc: () => {},
  sortField: '',
  setSortField: () => {},
  defaultSortField: '',
});

const providerGenerator = ({ ascKey, sortFieldKey, defaultSortField }) => {
  const localAsc = localStorage.getItem(ascKey) === 'true';
  let localSortField = localStorage.getItem(sortFieldKey) ?? defaultSortField;

  // We don't start with fuzzy score since the fuzzy filter bar is initially empty.
  if (localSortField === 'fuzzyScore') {
    localSortField = defaultSortField;
  }

  return ({ children }) => {
    const [asc, setAsc] = useState(localAsc);
    const [sortField, setSortField] = useState(localSortField);

    useEffect(() => localStorage.setItem(ascKey, asc), [asc]);
    useEffect(() => localStorage.setItem(sortFieldKey, sortField), [sortField]);

    const value = { asc, setAsc, sortField, setSortField, defaultSortField };

    return <SortContext.Provider value={value}>{children}</SortContext.Provider>;
  };
};

const artistSpec = {
  ascKey: 'artists--asc',
  sortFieldKey: 'artists--sortField',
  defaultSortField: 'name',
};

export const ArtistSortContextProvider = providerGenerator(artistSpec);

const collectionSpec = {
  ascKey: 'collections--asc',
  sortFieldKey: 'collections--sortField',
  defaultSortField: 'recentlyUpdated',
};

export const CollectionSortContextProvider = providerGenerator(collectionSpec);

const releaseSpec = {
  ascKey: 'releases--asc',
  sortFieldKey: 'releases--sortField',
  defaultSortField: 'recentlyAdded',
};

export const ReleaseSortContextProvider = providerGenerator(releaseSpec);
