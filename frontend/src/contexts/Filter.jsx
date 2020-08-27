import React, { useEffect, useState } from 'react';

export const FilterContext = React.createContext({
  filter: '',
  selection: '',
  setFilter: () => {},
  setSelection: () => {},
});

const providerGenerator = ({ filterKey, selectionKey }) => {
  const localFilter = localStorage.getItem(filterKey) ?? '';
  const localSelection = localStorage.getItem(selectionKey) ?? 'All';

  return ({ children }) => {
    const [filter, setFilter] = useState(localFilter);
    const [selection, setSelection] = useState(localSelection);

    useEffect(() => localStorage.setItem(filterKey, filter), [filter]);
    useEffect(() => localStorage.setItem(selectionKey, selection), [selection]);

    const value = { filter, selection, setFilter, setSelection };

    return <FilterContext.Provider value={value}>{children}</FilterContext.Provider>;
  };
};

const artistSpec = {
  filterKey: 'artists--filter',
  selectionKey: 'artists--artistType',
};

export const ArtistFilterContextProvider = providerGenerator(artistSpec);

const collectionSpec = {
  filterKey: 'collections--filter',
  selectionKey: 'collections--collectionType',
};

export const CollectionFilterContextProvider = providerGenerator(collectionSpec);
