import React, { useEffect, useState } from 'react';

export const SortContext = React.createContext({
  asc: true,
  setAsc: () => {},
  setSortField: () => {},
  sortField: 1,
});

const providerGenerator = ({ ascKey, sortFieldKey }) => {
  const localAsc = localStorage.getItem(ascKey) === 'true';
  const localSortField = parseInt(localStorage.getItem(sortFieldKey)) || 1;

  return ({ children }) => {
    const [asc, setAsc] = useState(localAsc);
    const [sortField, setSortField] = useState(localSortField);

    useEffect(() => localStorage.setItem(ascKey, asc), [asc]);
    useEffect(() => localStorage.setItem(sortFieldKey, sortField), [sortField]);

    const value = { asc, setAsc, setSortField, sortField };

    return <SortContext.Provider value={value}>{children}</SortContext.Provider>;
  };
};

const artistSpec = {
  ascKey: 'artists--asc',
  sortFieldKey: 'artists--sortField',
};

export const ArtistSortContextProvider = providerGenerator(artistSpec);

const collectionSpec = {
  ascKey: 'collections--asc',
  sortFieldKey: 'collections--sortField',
};

export const CollectionSortContextProvider = providerGenerator(collectionSpec);

const releaseSpec = {
  ascKey: 'releases--asc',
  sortFieldKey: 'releases--sortField',
};

export const ReleaseSortContextProvider = providerGenerator(releaseSpec);
