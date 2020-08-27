import React, { useEffect, useState } from 'react';

export const SortContext = React.createContext({
  asc: true,
  defaultSortField: '',
  setAsc: () => {},
  setSortField: () => {},
  sortField: '',
});

const providerGenerator = ({ ascKey, sortFieldKey, defaultSortField }) => {
  const localAsc = localStorage.getItem(ascKey) === 'true';
  const localSortField = localStorage.getItem(sortFieldKey) ?? defaultSortField;

  return ({ children }) => {
    const [asc, setAsc] = useState(localAsc);
    const [sortField, setSortField] = useState(localSortField);

    useEffect(() => localStorage.setItem(ascKey, asc), [asc]);
    useEffect(() => localStorage.setItem(sortFieldKey, sortField), [sortField]);

    const value = { asc, defaultSortField, setAsc, setSortField, sortField };

    return <SortContext.Provider value={value}>{children}</SortContext.Provider>;
  };
};

const artistSpec = {
  ascKey: 'artists--asc',
  defaultSortField: 'Name',
  sortFieldKey: 'artists--sortField',
};

export const ArtistSortContextProvider = providerGenerator(artistSpec);

const collectionSpec = {
  ascKey: 'collections--asc',
  defaultSortField: 'Recently Updated',
  sortFieldKey: 'collections--sortField',
};

export const CollectionSortContextProvider = providerGenerator(collectionSpec);

const releaseSpec = {
  ascKey: 'releases--asc',
  defaultSortField: 'Recently Added',
  sortFieldKey: 'releases--sortField',
};

export const ReleaseSortContextProvider = providerGenerator(releaseSpec);
