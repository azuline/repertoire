import React from 'react';
import { usePersistentState } from 'hooks';

export const SortContext = React.createContext({
  asc: true,
  setAsc: () => {},
  sortField: '',
  setSortField: () => {},
  defaultSortField: '',
});

const providerGenerator = ({ ascKey, sortFieldKey, defaultSortField }) => {
  const transformFuzzySortField = (sortField) => {
    return sortField === 'fuzzyScore' ? defaultSortField : sortField;
  };

  return ({ children }) => {
    const [asc, setAsc] = usePersistentState(ascKey, true);
    const [sortField, setSortField] = usePersistentState(
      sortFieldKey,
      defaultSortField,
      transformFuzzySortField
    );

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

const querySpec = {
  ascKey: 'queries--asc',
  sortFieldKey: 'queries--sortField',
  defaultSortField: 'recentlyAdded',
};

export const QuerySortContextProvider = providerGenerator(querySpec);
